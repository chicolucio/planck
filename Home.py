import warnings

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from numpy import ComplexWarning

from helpers import load_css, text_from_markdown, find_me_buttons
from planck import Planck

st.set_page_config(layout="centered", page_title="Planck",
                   page_icon=":rainbow:")

load_css("pages/styles.css")

PAGE_TEXT_FILE = 'pages/01_Home.md'
content = text_from_markdown(PAGE_TEXT_FILE)

st.title("Planck's Law")

st.markdown(""":warning: Move the slider to change the temperature! :warning:""")

temperature = st.slider("temperature", 200, 8_000, 300, 400)

lambda_array = np.linspace(1.0e-9, 2.0e-6, 1000)

fig, ax = plt.subplots()

Planck.plot_interactive(lambda_array, temperature, ax=ax, transparency=0.15)

st.pyplot(fig)

lambda_peak = Planck.wien_peak(temperature)

for classification in Planck.spectral_categories(lambda_peak):
    categories = [classification.category]
    subcategories = [classification.subcategory]

columns = st.columns(4)

with columns[0]:
    st.metric('Temperature / K', temperature)

with columns[1]:
    st.metric('Wavelength peak / nm', f'{lambda_peak / 1E-9:.0f}')

with columns[2]:
    for category in categories:
        st.metric('Peak category', category)

with columns[3]:
    for subcategory in subcategories:
        st.metric('Peak subcategory', subcategory)

st.markdown(''.join(content[0]))

columns = st.columns([1, 1, 1.2, 1, 1])

sites = ("linkedin", "portfolio", "github", "github_sponsors")
links = (
    "flsbustamante",
    "https://franciscobustamante.com.br",
    "chicolucio",
    "chicolucio",
)

with columns[2]:
    st.write('Developed by: Francisco Bustamante')
    for site, link in zip(sites, links):
        find_me_buttons(site, link)
