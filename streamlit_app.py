import streamlit as st
import pandas as pd

# Excelファイルのパス
EXCEL_FILE_PATH = "国.xlsx"

# Excelファイルの読み込み
@st.cache
def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

# メインのStreamlitアプリケーション
def main():
    st.title('Excelから画像を表示する')

    # Excelファイルを読み込む
    try:
        data = load_data(EXCEL_FILE_PATH)
    except:
        st.write('Excelファイルを読み込めませんでした。')
        return

    # 画像のファイルパスを取得する
    image_path = data.iloc[0]['画像']

    # 画像を表示する
    if image_path:
        st.image(image_path, caption='国の画像', use_column_width=True)
    else:
        st.write('画像のファイルパスが見つかりませんでした。')

if __name__ == '__main__':
    main()
