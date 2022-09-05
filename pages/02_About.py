import streamlit as st

from helpers import find_me_buttons, github_avatar_link, load_css


st.set_page_config(layout="centered", page_title="Planck - About",
                   page_icon=":rainbow:")

load_css("pages/styles.css")

sites = ("linkedin", "github", "portfolio", "github_sponsors")
links_francisco = (
    "flsbustamante",
    "chicolucio",
    "https://franciscobustamante.com.br",
    "chicolucio",
)

columns_main = st.columns(3)

with columns_main[1]:
    st.image(github_avatar_link(23560423))

st.header("Francisco Bustamante")
st.success("A chemist working with Data Science and Python Programming")

columns_extra = st.columns(4)
for column, site, link in zip(columns_extra, sites, links_francisco):
    with column:
        find_me_buttons(site, link)
