
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="英単語ガチャ")

# タイトルと説明
st.title('英単語ガチャ')

st.write('英語の単語をランダムに表示して、勉強をサポートします！')
st.write('がんばってください！')

# Load the data
@st.cache
def load_data():
    return 

words_df = pd.read_excel("500600.xlsx")



# ガチャ機能
if st.button('ガチャを引く！'):
    rarity_probs = {
        'N': 1.0,
    }
    chosen_rarity = np.random.choice(list(rarity_probs.keys()), p=list(rarity_probs.values()))
    subset_df = words_df[words_df['レア度'] == chosen_rarity]
    selected_word = subset_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"単語: {st.session_state.selected_word['単語']}")
    st.subheader(f"レア度: {st.session_state.selected_word['レア度']}")

    # 意味を確認するボタンを追加
    if st.button('意味を確認する'):
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.subheader(f"意味: {st.session_state.selected_word['意味']}")
        st.subheader(f"用例（英語）: {st.session_state.selected_word['用例（英語）']}")
        st.subheader(f"用例（日本語）: {st.session_state.selected_word['用例（日本語']}")
     