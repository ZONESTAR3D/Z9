[LCD_MENU]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/LCDMENU_Description.md
[PRUSA_SLICER]: https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer

----
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](./step_by_step.md)
[![](../lanpic/ES.png)](./step_by_step-es.md)
[![](../lanpic/PT.png)](./step_by_step-pt.md)
[![](../lanpic/FR.png)](./step_by_step-fr.md)
[![](../lanpic/DE.png)](./step_by_step-de.md)
[![](../lanpic/IT.png)](./step_by_step-it.md)
[![](../lanpic/RU.png)](./step_by_step-ru.md)
[![](../lanpic/JP.png)](./step_by_step-jp.md)
[![](../lanpic/KR.png)](./step_by_step-kr.md)

----
## ステップバイステップガイド
つまり、マシンを受け取った瞬間から独自の 3D モデル ファイルを印刷できるようになるまで、合計 5 つのステップが必要です: **設置 - ベッドの水平調整 - フィラメントのロード - テスト gcode ファイルの印刷 - スライスと 独自の 3D ファイルを印刷します**。
###### 
[![](https://img.youtube.com/vi/GrCOZ4ADHeA/0.jpg)](https://www.youtube.com/watch?v=GrCOZ4ADHeA)

### <a id ="a1">ステップ 1. インストール</a>
- 1.1 **インストール**。 [:book: **インストール ガイド**](./1.installation/installation.md) および [:clapper: **インストール ビデオ チュートリアル**](https://youtu.be/pdr8nLl3T3w) を参照してください。 マシンの設置を完了します。
- 1.2 **配線**。 配線のプロセスは基本的に、対応するソケットにプラグを挿入することです。 注意する必要があるのは、**コネクタがしっかり差し込まれていることを確認する**ことです (特に 2PIN ドッキング ソケットの場合)。 また、プリントヘッド（ホットエンド）の配線は、同色で異なる色のソケットが複数ありますので、ソケットの色に合わせて差し込んでください。
- 1.3 **電源をオン**。 配線が完了したら、[:clapper: **Z9V5 をオンにする**](https://youtu.be/xTlMHtxkGoY) ことができます。 特に、Z9V5 には電源スイッチが 2 つあることに注意してください。 1 つは ***AC スイッチ*** (マシンの背面にある赤いスイッチ) で、もう 1 つは ***DC スイッチ*** (マシンのコントロール ボックスの前面にある丸い金属製の押しボタン スイッチ) です。 Z9V5 の電源をオンにするには、最初に AC スイッチをオンにしてから、**DC スイッチを約 5 秒間押し続ける**必要があります。
- 1.4 **単純なテスト**。 電源を入れた後、LCD 画面上のメニュー ([:book: **LCD メニューの説明**](./2.Operation/LCDMENU_Description.md)) を操作して、マシンが正常に動作するかどうかを確認できます。 通常、これにはいくつかの手順が必要です。
   - 1.4.1 **準備>>オートホーム>>すべてホーム**。 本機のプリントヘッドを原点復帰させる作業です。
   - 1.4.2 **準備>>温度>>PLAを予熱**。 このステップは、ホットエンドとホットベッドが正常に加熱できることを確認するためのものです。このステップでは、ノズルの温度が 60 度を超えると、プリントヘッド (ホットエンド) の右側にあるファンが回転するのが見えるはずです。 、これはホットエンド冷却ファンです。
   - 1.4.3 **準備>>温度>>ファン速度:**。 ノブを押してファン速度 (255 に設定) を設定すると、ファン (M4V6 ホットエンドの左側) も上げることができるようになります。
   これら 3 つのステップの後、基本的にマシンが正常に動作していると判断され、次のステップに進むことができます。 部品が正常に動作していない場合は、配線を再確認するか、[:clapper: **機械自動テスト ビデオ チュートリアル**](https://youtu.be/Mf92BlmKA0A) を参照して自動機械テストを行ってください。 テスト中。

### <a id ="a2">ステップ 2. ベッドを水平にする</a>
印刷を開始する前に、フィラメントをベッドにうまく貼り付けることができるように、ノズルとベッド (印刷プラットフォーム) の間の高さを設定する簡単なベッド レベリングを行う必要があります。 これを行うには、[:clapper: **ベッド レベリング ビデオ チュートリアル**](https://youtu.be/nxzB7ho1kNo) を参照してください。

### <a id ="a3">ステップ 3. フィラメントをロードする</a>
4 本のフィラメントすべてを押出機とホットエンドにロードするには、この [:clapper: ビデオ チュートリアル](https://youtu.be/KZQdL7Rgy1s) を参照してください。
#### :warning: 注意してください :warning:
1. **単色または多色の 3D プリントを印刷する場合は、4 本のフィラメントすべてをホットエンドにロードする必要があります。**
2. **フィラメントがホットエンドの底部まで装着されていることを確認してください。そうしないと、ホットエンドが詰まる可能性があります。**


### <a id ="a4">ステップ 4. テスト gcode ファイルを印刷する</a>
FDM 3D プリンタは gcode ファイルのみを認識できるため、gcode ファイルを SD カードにコピーし、SD カードを 3D プリンタの SD カード ソケットに挿入して、印刷を開始する必要があります。
Z9V5Pro は 4 つの押出機を備えた 3D プリンターであるため、1 色の 3D モデルと 4 色の 3D モデルを印刷して、機械が適切に動作するかどうかをテストすることをお勧めします。
#### 1 色の 3D プリントを印刷する
- **gcode ファイルを準備します**。 SD カードから **xyz_cube.gcode** ファイルを見つけるか、[:arrow_down: ここをクリックしてダウンロード](./3.Test_gcode/xyz_cube.zip) を PC 上で解凍し、**xyz_cube をコピーします。 .gcode** を SD カードにコピーするには、SD カードをマシンの SD ソケットに接続します。
- **SD カードから印刷**。 LCD 画面上の **印刷** 項目にカーソルを移動し、ノブをクリックして **xyz_cube** ファイルを選択し、ノブをクリックして印刷を開始します。
- **ノズルの高さを微調整します**。 ノズルとホットベッドの加熱を待ち、最初の層の印刷を開始するときに、LCD 画面のノブをダブルクリックしてノズルからベッドまでの距離を微調整し (ノズルはステッカーより約 0.4 mm 高くなります)、印刷が完了するまで待ちます。 終了した。
#### 4 色の 3D プリントを印刷する
- **gcode ファイルを準備します**。 SD カードから **M4_4CTest.gcode** ファイルを見つけるか、[:arrow_down: ここをクリックしてダウンロード](./3.Test_gcode/M4_4CTest.zip) を PC 上で解凍し、**M4_4CTest をコピーします。 .gcode** を SD カードにコピーするには、SD カードをマシンの SD ソケットに接続します。
- **SD カードから印刷**。 LCD 画面上の **印刷** 項目にカーソルを移動し、ノブをクリックして **M4_4CTest** ファイルを選択し、ノブをクリックして印刷を開始します。
- **ノズルの高さを微調整します**。 ノズルとホットベッドの加熱を待ち、最初の層の印刷を開始するときに、LCD 画面のノブをダブルクリックしてノズルからベッドまでの距離を微調整し (ノズルはステッカーより約 0.4 mm 高くなります)、印刷が完了するまで待ちます。 終了した。

### <a id ="a5">ステップ 5. 独自の 3D モデルをスライスして印刷する</a>
独自の 3D モデルを印刷する前に、3D モデル ファイル ([インターネットからダウンロード](#a6) または自分で描画した stl/obj/AMF 形式のファイル) を gcode ファイルに変換する必要があります。このプロセスは < u>「**スライス**」</u>。
- まず、スライス ソフトウェアをダウンロードしてコンピュータにインストールし、スライス ソフトウェアでマシンのパラメータを設定するか、3D プリンタ メーカーによって設定されたマシンのプリセット ファイルをロードする必要があります。
- 次に、スライス ソフトウェアを実行する必要があります。また、3D モデル ファイルの特性に応じていくつかのパラメーターを設定して、スライスを実行する必要がある場合もあります。
- スライスが完了したら、生成された gcode ファイルを SD カードにコピーし、[:point_right:Stpe 4](#a4) に従って 3D プリンターで印刷します。
#### *PrusaSlicer* は当社が推奨するスライス ソフトウェアです。[:point_right:here][PRUSA_SLICER] を参照して PrusaSlicer ソフトウェアをダウンロードしてインストールし、ユーザー ガイドをお読みください。
:warning: **注意してください** :warning:
デフォルトの Z9V5Pro-MK6 には M4V6 (4-IN-1-OUT ミックスカラー) ホットエンドが装備されています。スライスする際は、プリンター プリセット (Z9 + M4 ホットエンド) の選択に注意してください。

----
### <a id ="a6">有名な無料 3D モデル ダウンロード Web サイト</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

----