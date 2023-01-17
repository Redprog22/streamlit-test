import streamlit as st
view = [100,150,30]
# view
st.write("#youtub view")
st.write("## row")
st.bar_chart(view)

import pandas as pd

sview = pd.Series(view)
sview