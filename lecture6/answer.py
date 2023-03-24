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
    # 処理を記述


def read_info(filepath, enc):
    """インフォメーションファイルを読み込む関数

    Args:
        filepath (str): インフォメーションファイルのパス
        enc (csv): インフォメーションファイルのエンコーディング

    Returns:
        result_dict (dict): インフォメーションファイルを読み込んで作成した辞書
    """
    # 処理を記述


def draw_graph(info, spect):
    """グラフを描画してファイルに保存する関数

    Args:
        info (dict): インフォメーションファイルを読み込んで作成した辞書
        spect (DataFrame): CSVファイルを読み込んで作成したデータフレーム

    Returns:
        なし
    """
    # 処理を記述


# メイン処理
info_dict = read_info("graph_info.txt", "cp932")
spect_df = read_spectrum("spectrum.csv", "cp932")
draw_graph(info_dict, spect_df)
