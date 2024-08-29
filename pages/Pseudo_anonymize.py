import pandas as pd
from anonymizedf.anonymizedf import anonymize
import streamlit as st

st.subheader("Specify the source folder of the tabular data")

get_filepath = st.text_input('Enter your file path name')

pseudo = ''


if get_filepath:
    read_file = pd.read_csv(get_filepath)
    number_of_columns = len(read_file.axes[1])
    list_all_columns = list(read_file.columns.values)

    options = st.multiselect("Which column do you want to pseudo anonymize?", list_all_columns)

    an = anonymize(read_file)

    for x in options:
        pseudo = an.fake_categories(x)
    st.write(pseudo)

