from urllib.error import URLError

import pandas as pd
import pydeck as pdk

import streamlit as st
from streamlit.hello.utils import show_code

st.metric('Amount', 14000)
d = pd.DataFrame([["Mechanize", 1422]], columns=["Provider", "GGR"])
st.dataframe(d)