'''
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
'''


import sys
import os
import re

sys.path.append('/usr/share/inkscape/extensions')
sys.path.append('/Applications/Inkscape.app/Contents/Resources/extensions') 

import subprocess
import math

import inkex
import png
import array


class GcodeExport(inkex.Effect):

######## 	Richiamata da _main()
	def __init__(self):
		"""init the effetc library and get options from gui"""
		inkex.Effect.__init__(self)
				
		self.OptionParser.add_option("","--bg_color",action="store",type="string",dest="bg_color",default="",help="")
		self.OptionParser.add_option("","--resolution",action="store", type="int", dest="resolution", default="5",help="")
		self.OptionParser.add_option("","--BW_threshold",action="store", type="int", dest="BW_threshold", default="128",help="") 
		
		# Speed
		self.OptionParser.add_option("","--travel-speed",action="store", type="int", dest="travel_speed", default="1200",help="")
		self.OptionParser.add_option("","--laser-speed",action="store", type="int", dest="laser_speed", default="480",help="")

		# Mirror Y
		self.OptionParser.add_option("","--flip_y",action="store", type="inkbool", dest="flip_y", default=False,help="")
		
		# add command of power on laser
		self.OptionParser.add_option("","--add-turn-on-laser-message", action="store", type="inkbool", dest="add_turn_on_laser_message", default=True,help="Add turn on laser message")            

		# Commands
		self.OptionParser.add_option("","--laser-control", action="store", type="string", dest="lasercontrol", default="M106", help="")
		self.OptionParser.add_option("","--laser-Phase", action="store", type="inkbool", dest="laserphase", default=False, help="")
		self.OptionParser.add_option("","--laser-power", action="store", type="int", dest="laserpower", default="255", help="")
		self.OptionParser.add_option("","--poweron-delay", action="store", type="int", dest="powerondelay", default="20", help="")
		self.OptionParser.add_option("","--poweroff-delay", action="store", type="int", dest="poweroffdelay", default="100", help="")
		
		# Z offset
		self.OptionParser.add_option("","--z-offset",action="store", type="int", dest="zoffset", default="10",help="")
		self.OptionParser.add_option("-d", "--directory",action="store", type="string", dest="directory", default="/home/",help="Directory for files") ####check_dir
		self.OptionParser.add_option("-f", "--filename", action="store", type="string", dest="filename", default="output", help="File name")            
		self.OptionParser.add_option("","--add-numeric-suffix-to-filename", action="store", type="inkbool", dest="add_numeric_suffix_to_filename", default=True,help="Add numeric suffix to filename")
		
		# Anteprima = Solo immagine BN 
		self.OptionParser.add_option("","--preview_only",action="store", type="inkbool", dest="preview_only", default=False,help="") 

		#inkex.errormsg("BLA BLA BLA Messaggio da visualizzare") #DEBUG


		
		
######## 	Richiamata da __init__()
########	Qui si svolge tutto
	def effect(self):
		

		current_file = self.args[-1]
		bg_color = self.options.bg_color
		
		
		##Implementare check_dir
		
		if (os.path.isdir(self.options.directory)) == True:					
			
			##CODICE SE ESISTE LA DIRECTORY
			#inkex.errormsg("OK") #DEBUG

			
			#Aggiungo un suffisso al nomefile per non sovrascrivere dei file
			if self.options.add_numeric_suffix_to_filename :
				dir_list = os.listdir(self.options.directory) #List di tutti i file nella directory di lavoro
				temp_name =  self.options.filename
				max_n = 0
				for s in dir_list :
					r = re.match(r"^%s_0*(\d+)%s$"%(re.escape(temp_name),'.png' ), s)
					if r :
						max_n = max(max_n,int(r.group(1)))	
				self.options.filename = temp_name + "_" + ( "0"*(4-len(str(max_n+1))) + str(max_n+1) )


			pos_file_png_exported = os.path.join(self.options.directory,self.options.filename+".png") 
			pos_file_png_BW = os.path.join(self.options.directory,self.options.filename+"_preview.png") 
			pos_file_gcode = os.path.join(self.options.directory,self.options.filename+".gcode") 
			

			#Esporto l'immagine in PNG
			self.exportPage(pos_file_png_exported,current_file,bg_color)


			
			#DA FARE
			#Manipolo l'immagine PNG per generare il file Gcode
			self.PNGtoGcode(pos_file_png_exported,pos_file_png_BW,pos_file_gcode)
						
			
		else:
			inkex.errormsg("Directory does not exist! Please specify existing directory!")
            

            
            
########	ESPORTA L IMMAGINE IN PNG		
######## 	Richiamata da effect()
		
	def exportPage(self,pos_file_png_exported,current_file,bg_color):		
		######## CREAZIONE DEL FILE PNG ########
		#Crea l'immagine dentro la cartella indicata  da "pos_file_png_exported"
		# -d 127 = risoluzione 127DPI  =>  5 pixel/mm  1pixel = 0.2mm
		###command="inkscape -C -e \"%s\" -b\"%s\" %s -d 127" % (pos_file_png_exported,bg_color,current_file) 

		if self.options.resolution == 1:
			DPI = 25.4
		elif self.options.resolution == 2:
			DPI = 50.8
		elif self.options.resolution == 5:
			DPI = 127
		elif self.options.resolution == 10:
			DPI = 254
		elif self.options.resolution == 20:
			DPI = 508
		else:
			DPI = 1016

		command="inkscape -C -e \"%s\" -b\"%s\" %s -d %s" % (pos_file_png_exported,bg_color,current_file,DPI) #Comando da linea di comando per esportare in PNG
					
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		return_code = p.wait()
		f = p.stdout
		err = p.stderr


########	CREA IMMAGINE IN B/N E POI GENERA GCODE
######## 	Richiamata da effect()

	def PNGtoGcode(self,pos_file_png_exported,pos_file_png_BW,pos_file_gcode):
		
		######## GENERO IMMAGINE IN SCALA DI GRIGI ########
		#Scorro l immagine e la faccio diventare una matrice composta da list


		reader = png.Reader(pos_file_png_exported)#File PNG generato
		
		w, h, pixels, metadata = reader.read_flat()
		
		
		matrice = [[255 for i in range(w)]for j in range(h)]  #List al posto di un array
		
		#0.21R + 0.71G + 0.07B
		for y in range(h): # y varia da 0 a h-1
			for x in range(w): # x varia da 0 a w-1
			  pixel_position = (x + y * w)*4 if metadata['alpha'] else (x + y * w)*3
			  matrice[y][x] = int(pixels[pixel_position]*0.21 + pixels[(pixel_position+1)]*0.71 + pixels[(pixel_position+2)]*0.07)

		######## GENERO IMMAGINE IN BIANCO E NERO ########
		#Scorro matrice e genero matrice_BN
		B=255
		N=0 
		
		matrice_BN = [[255 for i in range(w)]for j in range(h)]
		#B/W fixed threshold               
		soglia = self.options.BW_threshold 
		for y in range(h):                 
		  for x in range(w):               
			  if matrice[y][x] >= soglia :   
				  matrice_BN[y][x] = B         
			  else:                          
				  matrice_BN[y][x] = N         
		

		#### SALVO IMMAGINE IN BIANCO E NERO ####
		file_img_BN = open(pos_file_png_BW, 'wb') #Creo il file
		Costruttore_img = png.Writer(w, h, greyscale=True, bitdepth=8) #Impostazione del file immagine
		Costruttore_img.write(file_img_BN, matrice_BN) #Costruttore del file immagine
		file_img_BN.close()	#Chiudo il file


		#### GENERO IL FILE GCODE ####
		if self.options.preview_only == False: #Genero Gcode solo se devo
		
			if self.options.flip_y == False: #Inverto asse Y solo se flip_y = False     
				#-> coordinate Cartesiane (False) Coordinate "informatiche" (True)
				matrice_BN.reverse()				

			
			Laser_ON = False
			F_G0 = self.options.travel_speed
			F_G1 = self.options.laser_speed
			Scala = self.options.resolution

			file_gcode = open(pos_file_gcode, 'w')  #Creo il file
			
			#Configurazioni iniziali standard Gcode
			file_gcode.write('; Generated with "ZONESTAR Laser Engraving Gcode generator V3"\n;\n')
						
			#laser off
			#file_gcode.write(self.options.laseroff + '\n')
			if self.options.laserphase == True:
				file_gcode.write(self.options.lasercontrol + ' S0 ' + '; turn off laser\n')
			else:
				file_gcode.write(self.options.lasercontrol + ' S255 '+ '; turn off laser\n')
						
			#HOMING
			file_gcode.write('G21; Set units to millimeters\n')			
			file_gcode.write('G90; Use absolute coordinates\n')
			file_gcode.write('G28; home all axes\n')
			file_gcode.write('G92 X-5 Y0 Z0; Coordinate Offset\n')
			
			#wait for turn on laser power
			if self.options.add_turn_on_laser_message :
				file_gcode.write('M0 turn on laser power and press knob ;Wait for laser turn on\n;\n')
			
			#Z offset
			file_gcode.write('G1 Z' + str(self.options.zoffset) + ' F400 ;Move up Z axis before engraving\n;\n')

			#Creazione del Gcode
			
			#allargo la matrice per lavorare su tutta l'immagine
			for y in range(h):
				matrice_BN[y].append(B)
			w = w+1
			
			for y in range(h):
				if y % 2 == 0 :
					for x in range(w):
						if matrice_BN[y][x] == N :
							if Laser_ON == False :
								file_gcode.write('G0 X' + str(float(x)/Scala) + ' Y' + str(float(y)/Scala) + ' F' + str(F_G0) + '\n')
								#file_gcode.write(self.options.laseron + '\n')		
								if self.options.laserphase == True:
									file_gcode.write(self.options.lasercontrol + ' S' + str(self.options.laserpower) +'\n' + 'G4 P' + str(self.options.powerondelay) + '\n')
								else:
									file_gcode.write(self.options.lasercontrol + ' S' + str(255-self.options.laserpower) +'\n' + 'G4 P' + str(self.options.powerondelay) + '\n')
								Laser_ON = True
							if  Laser_ON == True :   #DEVO evitare di uscire dalla matrice
								if x == w-1 :
									file_gcode.write('G1 X' + str(float(x)/Scala) + ' Y' + str(float(y)/Scala) +' F' + str(F_G1) + '\n')
									#file_gcode.write(self.options.laseroff + '\n')
									if self.options.laserphase == True:
										file_gcode.write(self.options.lasercontrol + ' S0\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
									else:
										file_gcode.write(self.options.lasercontrol + ' S255\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
									Laser_ON = False
								else: 
									if matrice_BN[y][x+1] != N :
										file_gcode.write('G1 X' + str(float(x)/Scala) + ' Y' + str(float(y)/Scala) + ' F' + str(F_G1) +'\n')
										#file_gcode.write(self.options.laseroff + '\n')
										if self.options.laserphase == True:
											file_gcode.write(self.options.lasercontrol + ' S0\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
										else:
											file_gcode.write(self.options.lasercontrol + ' S255\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
										Laser_ON = False
				else:
					for x in reversed(range(w)):
						if matrice_BN[y][x] == N :
							if Laser_ON == False :
								file_gcode.write('G0 X' + str(float(x)/Scala) + ' Y' + str(float(y)/Scala) + ' F' + str(F_G0) + '\n')
								#file_gcode.write(self.options.laseron + '\n')			
								if self.options.laserphase == True:
									file_gcode.write(self.options.lasercontrol + ' S' + str(self.options.laserpower) +'\n' + 'G4 P' + str(self.options.powerondelay) + '\n')
								else:
									file_gcode.write(self.options.lasercontrol + ' S' + str(255-self.options.laserpower) +'\n' + 'G4 P' + str(self.options.powerondelay) + '\n')
								Laser_ON = True
							if  Laser_ON == True :   #DEVO evitare di uscire dalla matrice
								if x == 0 :
									file_gcode.write('G1 X' + str(float(x)/Scala) + ' Y' + str(float(y)/Scala) +' F' + str(F_G1) + '\n')
									#file_gcode.write(self.options.laseroff + '\n')
									if self.options.laserphase == True:
										file_gcode.write(self.options.lasercontrol + ' S0\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
									else:
										file_gcode.write(self.options.lasercontrol + ' S255\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
									Laser_ON = False
								else: 
									if matrice_BN[y][x-1] != N :
										file_gcode.write('G1 X' + str(float(x)/Scala) + ' Y' + str(float(y)/Scala) + ' F' + str(F_G1) +'\n')
										#file_gcode.write(self.options.laseroff + '\n')
										if self.options.laserphase == True:
											file_gcode.write(self.options.lasercontrol + ' S0\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
										else:
											file_gcode.write(self.options.lasercontrol + ' S255\n' + 'G4 P' + str(self.options.poweroffdelay) + '\n')
										Laser_ON = False				

			#Configurazioni finali standard Gcode
			file_gcode.write('G28 X0 Y0; home\n')
			
			file_gcode.close() #Chiudo il file


######## 	######## 	######## 	######## 	######## 	######## 	######## 	######## 	######## 	


def _main():
	e=GcodeExport()
	e.affect()
	
	exit()

if __name__=="__main__":
	_main()




