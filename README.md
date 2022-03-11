# 1. 概要
[IoTBank まもセンサーAir](https://mamoair.jp/)の測定値のグラフを作成するスクリプトです。

# 2. 使用方法
外部パッケージとして、pandasとMatplotlibが必要です。

まもセンサーAirのダッシュボードから[「履歴のエクスポートボタン」](https://mamoair.jp/faq/dashboard-personal/)でCSVファイルをダウンロードし、mamosensor_air.pyと同じディレクトリに置き、実行します。

`python mamosensor_air.py`

ディレクトリ内の全てのCSVファイルを読み込み、複数のエクスポートデータからそれぞれグラフを作成します。実行時に二酸化炭素濃度が1000 ppmを超えた時刻を標準出力に出力します。
