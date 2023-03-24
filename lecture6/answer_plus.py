import configparser

import pandas as pd
import matplotlib.pyplot as plt


def read_csv(filepath, enc):
    """CSVを読み込んで空行を削除する関数

    Args:
        filepath (str): CSVファイルのパス
        enc (csv): CSVファイルのエンコーディング

    Returns:
        df (DataFrame): CSVファイルを読み込んで空行を削除したデータフレーム
    """
    df = pd.read_csv(filepath, encoding=enc)
    df_dna = df.dropna(how="all")
    return df_dna


def draw_graph(config, spect):
    """グラフを描画してファイルに保存する関数

    Args:
        info (dict): インフォメーションファイルを読み込んで作成した辞書
        spect (DataFrame): CSVファイルを読み込んで作成したデータフレーム

    Returns:
        なし
    """
    # Figure/Axesオブジェクトの作成
    figure = plt.figure()
    ax = figure.subplots()

    # 折れ線グラフのプロット
    ax.plot(spect["Wavelength"], spect["Intensity1"], label=config["Legend labels"]["LINE1"])
    ax.plot(spect["Wavelength"], spect["Intensity2"], label=config["Legend labels"]["LINE2"])

    # グラフの装飾
    ax.set_title(config["Title"]["TITLE"])
    ax.set_xlabel(config["Labels"]["XLABEL"])
    ax.set_ylabel(config["Labels"]["YLABEL"])
    ax.legend()

    # グラフを画像ファイルに保存
    figure.savefig("graph.png", dpi=100, format="png")

    # グラフを画面に表示
    plt.show()

    # グラフをクローズ
    plt.close(figure)

# メイン処理

# グラフ情報ファイル(INI形式)の読み込み
config = configparser.ConfigParser()
config.read("graph_info.txt")

spect_df = read_csv("spectrum.csv", "cp932")
draw_graph(config, spect_df)
