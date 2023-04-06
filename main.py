import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Vladislav Kham")
    content = """Something I
    can tell about myself
    """
    st.info(content)

content2 = """
<b>Below you can find some of the apps I have built in Python. Feel free to contact me!</b>
"""
st.write(content2, unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")


for index, row in df.iterrows():
    if index % 2 == 0:
        with col3:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source code: ]({row['url']})")
    else:
        with col4:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source code: ]({row['url']})")



