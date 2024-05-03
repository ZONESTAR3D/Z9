[M4V6_PRECAUTION]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4/M4_V6/M4V6_Precaution.md
[Z9V5MK6_STEPBYSTEP]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/step_by_step.md
[Z9V5MK6_LOADFILAMENT]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/2.Operation/Operation.md#load-filaments
[Z9V5MK6_OPTION]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/OptionalFeatures.md
[LINK_M4V6]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4/M4_V6
[LINK_MIX_FEATURE]: https://github.com/ZONESTAR3D/Document-and-User-Guide/blob/master/Mixing_Color
[LINK_FIRMWARE]: https://github.com/ZONESTAR3D/Firmware/blob/master/Z9/Z9V5/bin/Z9V5Pro-MK6
[LINK_SOURCECODE]: https://github.com/ZONESTAR3D/source-code-for-3d-printer
[LINK_TROUBLESHOOTING]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5_FAQ
[M4_TEST_GCODE]: https://github.com/ZONESTAR3D/Slicing-Guide/blob/master/PrusaSlicer/test_gcode/M4/readme.md
[GCODE_REF1]: https://beginner3dprinting.com/what-is-g-code-in-3d-printing/
[GCODE_REF2]: https://www.reprap.org/wiki/G-code

----
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](./readme.md)
[![](../lanpic/ES.png)](./readme_es.md)
[![](../lanpic/PT.png)](./readme_pt.md)
[![](../lanpic/FR.png)](./readme_fr.md)
[![](../lanpic/DE.png)](./readme_de.md)
[![](../lanpic/IT.png)](./readme_it.md)
[![](../lanpic/RU.png)](./readme_ru.md)
[![](../lanpic/JP.png)](./readme_jp.md)
[![](../lanpic/KR.png)](./readme_kr.md)

----
# ZONESTAR Z9V5Pro-MK6 3D プリンター ユーザーガイド

----
## :warning: 注意してください
#### :loudspeaker: 本機をご使用になる前に、[:book:「M4V6 ご使用上の注意」][M4V6_PRECAUTION]をよくお読みください。
#### :loudspeaker: M4V6 ホットエンドに 4 つのフィラメントを同時にロードする必要があります。誤った操作を行うと、ミックス カラー ホットエンドがブロックされる可能性があります。 誤操作によるホットエンドの詰まりは保証の対象外となります。 フィラメントのロード方法については、[:book:本書][Z9V5MK6_LOADFILAMENT]を参照してください。
#### :loudspeaker: 3D プリンターの初心者の方は、[:book: ステップバイステップ ガイド][Z9V5MK6_STEPBYSTEP] をよく読み、手順に従ってください。
- [:book: **M4V6 使用上の注意事項**][M4V6_PRECAUTION]
- [:book: **フィラメントを正しくロードする方法**][Z9V5MK6_LOADFILAMENT]
- [:book: **ステップバイステップガイド**][Z9V5MK6_STEPBYSTEP]


------
## :book: 目次
- [**インストールガイド**](#A1)
- [**操作ガイド**](#A2)
- [**gcode ファイルをテスト**](#A3)
- [**スライスソフトウェア**](#A4)
- [**ファームウェア**](#A5)
- [**トラブルシューティング**](#A6)
- [**パーツ stl ファイルを印刷**](#A7)
- [**オプションのアップグレード機能**](#A8)

-----
## <a id="A1"> 1. インストール ガイド </a>
まず、以下の資料とビデオを参照して、機械の設置と配線を完了してください。
### インストール
- [:book: インストール ガイド オンライン ドキュメント](./1.installation/installation.md)
- [:blue_book: インストール ガイド PDF ファイル](./1.インストール/インストール.pdf)
- [:clapper: インストールガイドビデオチュートリアル](https://youtu.be/TGHUVzV1Pg4)
### 配線
- [:book: 配線ガイド オンライン ドキュメント](./1. Installation/Wiring.md)
- [:blue_book: 配線ガイド PDF ファイル](./1.取り付け/配線.pdf)
- [:art: 配線図](./1.installation/Z9V5Pro_Wiring_Diagram.jpg)
- [:clapper: 配線ビデオチュートリアル](https://youtu.be/tQQNLDOpdQU)

## <a id="A2"> 2. 操作ガイド </a>
### **LCD コントロール パネルの概要**
設置と配線が完了したら、以下のガイドを参照してコントロールパネル (LCD 画面) の使用方法を知り、LCD メニューの機能を全体的に理解してください。
- [:book: LCD メニュー オンライン ドキュメント](./2.Operation/LCDMENU_Description.md)
- [:blue_book: LCD メニュー PDF ファイル](./2.Operation/LCDMENU_Description.pdf)
#### **最初の作品を印刷します**
これで、「Hello word」作品を印刷してみることができます。印刷を開始する前に、まずホット ベッドの高さを簡単に修正し (「ベッド レベリング」と呼ばれます)、次にフィラメントを押出機にロードする必要があります。 (プリントの色に関係なく、4 本のフィラメントすべてを押出機とホットエンドにロードする必要があることに注意してください)。 次に、SD カードをマシンに挿入し、SD カード内のテスト用 3D モデル gcode ファイルを選択できます。 詳細は以下の資料をご参照ください。
- [:book: 操作ガイド オンラインドキュメント](./2.Operation/Operation.md)
- [:blue_book: 操作ガイド PDF ファイル](./2.Operation/Operation.pdf)
#### :page_with_curl: その他の機能
また、次のドキュメントを読んで、マシンで使用される押出機 (ホットエンドおよびプリントヘッド) やマシンの高度な機能についてより深く理解することもできます。
- [:book: ミックスカラー機能使用ガイド][LINK_MIX_FEATURE]
- [:book: M4V6 Hotend の紹介][LINK_M4V6]
- [:book: PC から印刷](./2.Operation/PrintFromPC/readme.md)
- [:book: Advanced 機能使用ガイド](./2.Operation/Advance_Feature.md)

## <a id="A3"> 3. G コード ファイルをテストします </a>
**:pencil: 3D プリントにおける G コードとは何ですか?**
G コードとは、3D プリンターが 3 次元オブジェクトを印刷するために必要な情報、または命令であり、3D プリンターが理解できる言語です。 G コードは、STL、オブジェクト、AMF ファイルなどの標準 3D モデリング ファイルを変換することにより、スライシング ソフトウェアによって生成されます。 :page_with_curl: [**参照 1**][GCODE_REF1] :page_with_curl: [**参照 2**][GCODE_REF2]   
マシンが適切に動作しているかどうかを確認したり、このマシンにどのような印刷機能があるかを実証したりするために、いくつかのテスト gcode ファイルを SD カードに保存しました。 SD カード内にテスト gcode ファイルが見つからない場合は、[:arrow_down: **ここ**](./3.TestGcode/Test_gcode.zip) からダウンロードしてください。  
- **xyz_cube.gcode**: マシンが正常に動作しているかどうかを確認するために使用される単純なテスト gcode ファイル。  
- **dog.gcode**: 古典的な印刷品質テスト ファイル。
- **Vase.gcode**: テスト用の花瓶。
   - **GradientMix_Vase.gcode**: vase.gcode と同じ花瓶ですが、「グラデーション ミックス」機能が有効になっています。
   - **RandomMix_Vase.gcode**: vase.gcode と同じ花瓶ですが、「ランダム ミックス」機能が有効になっています。
- **M4_4CTest.gcode**: M4 ホット エンドを備えた 3D プリンター用の基本 4 色のテスト ファイル。
- **M4_4C_BODY3D.gcode**: より大きな 4 色のテスト ファイル。
- **16color_tower.gcode**: 異なる色のフィラメントを混合した結果を示す基本 16 色のテスト ファイル。
- **level_test_310.gcode**: ホット ベッドの平坦度を検証するために使用されるテスト ファイル (ベッドの自動レベリングなし)。
- **level_test_310-G29.gcode**: ホット ベッドの平坦度 (ベッドの自動レベリング付き) を検証するために使用されるテスト ファイル。
**[:arrow_down: さらにテスト gcode ファイルをダウンロード][M4_TEST_GCODE].**
 
## <a id="A4"> 4. スライス </a>
**[:pencil: 3D プリントにおけるスライスとは何ですか?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**
スライサーは、3D オブジェクト モデルをプリンターの特定の命令に変換するために、ほとんどの 3D プリンティング プロセスで使用されるツールパス生成ソフトウェアです。 特に、溶融フィラメント製造やその他の同様のプロセスにおける STL 形式のモデルから G コード形式のプリンタ コマンドへの変換。   
- [:book:スライサー ユーザー ガイド オンライン ドキュメント](./4.Slicing/readme.md)
- [:blue_book: スライサー ユーザーガイド PDF ファイル](./4.Slicing/Slicing.pdf)

## <a id="A5"> 5. ファームウェア </a>
**:pencil: ファームウェアの bin ファイルとソース コードとは何ですか?**
ファームウェア bin ファイルは、内蔵フラッシュに書き込まれる正確なメモリです。   
ファームウェアのソース コードは、ファームウェアの中核部分です。 当社のファームウェアのソース コードは [**marlin**](https://www.marlinfw.org) に基づいています。   
以下のリンクからファームウェアの bin ファイルまたはソース コードをダウンロードできます。  
- [:arrow_down: ファームウェア bin ファイル][LINK_FIRMWARE]
- [:arrow_down: ファームウェアのソース コード][LINK_SOURCECODE]

## <a id="A6"> 6. トラブルシューティング </a>
プリンタのインストールと使用に問題がある場合は、まず [:book: トラブルシューティング オンライン ドキュメント][LINK_TROUBLESHOOTING] から解決策を見つけてみてください。 この問題を解決できない場合は、電子メール (:email: support@zonestar3d.com) でお問い合わせください。

## <a id="A7"> 7. パーツの印刷 </a>
マシンには印刷されるいくつかのコンポーネントがあり、いくつかのアップグレードも用意されています。 必要に応じて、ダウンロードして印刷し、マシンにインストールできます。

-----
## <a id="A8"> オプション機能 </a>
このマシンにはいくつかのオプション機能が導入されており、好みに応じていつでもこれらの機能をアップグレードできます。 これに興味がある場合は、「オプションのアップグレード機能ガイド」を読んで、より詳細な情報を入手してください。
- [:book: オプションのアップグレード機能ガイドのオンライン ドキュメント][Z9V5MK6_OPTION]
- [:blue_book: オプションのアップグレード機能ガイド PDF ファイル](./OptionalFeature.pdf)

