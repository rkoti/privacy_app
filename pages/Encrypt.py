import streamlit as st
import pandas as pd
import hashlib

global_var = []

st.set_page_config(
    page_title='Data Anonymization app',
    page_icon='🧰'
)

st.subheader("Specify the source folder of the tabular data")


get_filepath = st.text_input('Enter your file path name')


if get_filepath:
    read_file = pd.read_csv(get_filepath)
    st.write("The original file")
    st.write(read_file.head(10))

    number_of_columns = list(read_file.columns.values)
    df = pd.DataFrame(number_of_columns, columns=['columns'])
    st.write(df)
    cols = len(read_file.axes[1])
    st.write("Number of columns present")
    st.write(cols)
    options = st.multiselect("Which column do you want to encrypt with hashlib?",
                             number_of_columns, )

    for cols in options:
        read_file[cols] = read_file[cols].astype(str)
        read_file[cols] = read_file[cols].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())

    if cols is not None:
        st.write(read_file)

