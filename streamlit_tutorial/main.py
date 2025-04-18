import streamlit as st
import os
import numpy as np
import pandas as pd

# RUN FILE AS: streamlit run main.py


st.write("# Hello World!") # display text in the app

st.write({"Key":"value"})
st.write(True)
st.write(1234.56)
st.write( 3+ 4)

"Hello" if (1 == 1) else "Goodbye"

# create stremlit button

pressed = st.button("Click me!")
# Default value is False, if pressed it will be True. 
# Page refresh sets button to False again.
print(f"first: {pressed}")

pressed2 = st.button("Click me again!")
print(f"second: {pressed2}")
# Pressing this sets button 1 value to False again.

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("This is a **markdown** text")
st.caption("This is a caption")

code_example = """
import streamlit as st
import numpy as np
"""
st.code(code_example, language="python")
st.divider()


st.image(os.path.join(os.getcwd(), "static", "truck.jpg"))


# Data Elements
st.subheader("DataFrame")
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4, 5],
    "Column 2": ["A", "B", "C", "D", "E"],
    "Column 3": [True, False, True, False, True]
})
st.dataframe(df)
editable_df = st.data_editor(df)

st.subheader("Static Table")
st.table(df)

st.subheader("Metrics")
st.metric(label= "Total Rows", value=len(df), delta=1)

st.subheader("JSON")
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
st.json(json_data) # writes dict as json
st.write("Dictionary View", json_data)


st.divider()

# Charts

st.header("Charts Demo")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.subheader("Line Chart")
st.line_chart(chart_data)

# Map

st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)