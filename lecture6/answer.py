import pandas as pd
import matplotlib.pyplot as plt


def read_spectrum(filepath, enc):
    """CSVを読み込んで空行を削除する関数

    Args:
        filepath (str): CSVファイルのパス
        enc (csv): CSVファイルのエンコーディング

    Returns:
        df (DataFrame): CSVファイルを読み込んで空行を削除したデータフレーム
    """
    # CSVファイルを読み込むには、「pd.read_csv(ファイルパス, encoding=エンコーディング」を使用しましょう。
    # 空行の削除には、「変数 = データフレーム.dropna(how="all")」を使用しましょう。


def read_info(filepath, enc):
    """インフォメーションファイルを読み込む関数

    Args:
        filepath (str): インフォメーションファイルのパス
        enc (csv): インフォメーションファイルのエンコーディング

    Returns:
        result_dict (dict): インフォメーションファイルを読み込んで作成した辞書
    """
    # open関数でファイルを開いて、次のようにfor文を実行すると、1行ずつデータを取り出すことができます。
    # with open(ファイルパス, encoding=エンコーディング) as ファイルオブジェクト:
    #     for 変数 in ファイルオブジェクト
    #         変数を使った処理

    # 最終的に次のような辞書を作成して、リターンしましょう
    # {"TITLE":"Spectrum Graph", "XLABEL":"Wavelength", ・・・}


def draw_graph(info, spect):
    """グラフを描画してファイルに保存する関数

    Args:
        info (dict): インフォメーションファイルを読み込んで作成した辞書
        spect (DataFrame): CSVファイルを読み込んで作成したデータフレーム

    Returns:
        なし
    """
    # 次のような流れで、グラフの作成と描画を行いましょう
    # 1. Figureオブジェクトの作成
    # 2. Axesオブジェクトの作成
    # 3. 折れ線グラフのプロット
    # 4. グラフの装飾
    # 5. グラフを画面に表示
    # 6. グラフを画像に保存
    # 7. グラフをクローズ(忘れずに！)

# メイン処理
info_dict = read_info("graph_info.txt", "cp932")
spect_df = read_spectrum("spectrum.csv", "cp932")
draw_graph(info_dict, spect_df)
