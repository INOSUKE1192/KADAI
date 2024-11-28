# KADAI
　このプログラムは、入力された機関車の番号から、その機関車がどの形式に属し、製造順序がどの位置にあるのかを計算し、保存機か解体済みかを判定するツールになります。日本の8620型および9600型の機関車に対応。
## 概要
-ややこしい型式番号を持つ車両の製造番号の判別
# 主な機能
1.形式の判定
入力された車両が8620型か9600型か判別。
2．製造順序の計算
形式ごとに計算し該当車両の製造順序を算出。
3．保存機か解体済みかの判定
該当の車両が現存しているか判定
4．エラー
適合しない値にはエラーメッセージを表示。

## インストール方法
#リポジトリをクローン
git clone https://github.com/INOSUKE1192/KADAI.git
#ディレクトリに移動
cd SL.py
##必要なソフトウェア
python
##使い方
実行方法の例
python main.py
以下の文が表示されるので車両番号を入力
機関車の番号を入力してください：
#サンプル
実行例
機関車の番号を入力してください: 8622
機関車番号 8622 は 8620型 の製造順 3 両目 (保存機) です。

機関車の番号を入力してください: 49648
機関車番号 49649 は 9600型 の製造順 649 両目 (解体済み) です。
##テスト環境
ubuntu
##ライセンス
このソフトウェアパッケージは、3条項BSDライセンスの下、再分布および使用が許可されます。

©2024　Shuusuke Inomata
