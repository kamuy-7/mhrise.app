import streamlit as st
from PIL import Image

st.title('Kamuy-MHRise：SB')
st.caption('モンスターハンターサンブレイク')
st.text('装備紹介：汎用型貫通Lｖ２速射剛心付きクーゲル用ライトボウガン装備')

image = Image.open("ブッシュ.png")
st.image(image, width=200)
image2 = Image.open("skill.png")
st.image(image2,width=800)
image3 = Image.open("skill2.png")
st.image(image3, width=800)

st.text('よかったら参考にしてね～、アプデは2023.2.7(火)\n'
        '復活古龍はワールドよりイヴェルカーナでしたｗ')