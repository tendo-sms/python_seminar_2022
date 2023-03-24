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
    df = pd.read_csv(filepath, encoding=enc)
    df_dna = df.dropna(how="all")
    return df_dna


def read_info(filepath, enc):
    """インフォメーションファイルを読み込む関数

    Args:
        filepath (str): インフォメーションファイルのパス
        enc (csv): インフォメーションファイルのエンコーディング

    Returns:
        result_dict (dict): インフォメーションファイルを読み込んで作成した辞書
    """
    with open(filepath, encoding=enc) as info:
        result_dict = {}
        for txtdata in info:
            if "=" in txtdata:
                result_dict[txtdata.split("=")[0].strip()] = txtdata.split("=")[1].strip()

    return result_dict


def draw_graph(info, spect):
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
    ax.plot(spect["Wavelength"], spect["Intensity1"], label=info["LINE1"])
    ax.plot(spect["Wavelength"], spect["Intensity2"], label=info["LINE2"])

    # グラフの装飾
    ax.set_title(info["TITLE"])
    ax.set_xlabel(info["XLABEL"])
    ax.set_ylabel(info["YLABEL"])
    ax.legend()

    # グラフを画像ファイルに保存
    figure.savefig("graph.png", dpi=100, format="png")

    # グラフを画面に表示
    plt.show()

    # グラフをクローズ
    plt.close(figure)

# メイン処理
info_dict = read_info("graph_info.txt", "cp932")
spect_df = read_spectrum("spectrum.csv", "cp932")
draw_graph(info_dict, spect_df)
