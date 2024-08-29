import random

import pandas as pd
from pycanon import anonymity, report
import streamlit as st

st.subheader("Specify the source folder of the tabular data")

get_filepath = st.text_input('Enter your file path name')

if get_filepath:
    read_file = pd.read_csv(get_filepath)
    number_of_columns = len(read_file.axes[1])
    list_all_columns = list(read_file.columns.values)

    quasi_identifier = st.multiselect("Which column do you want to select as Quasi identifier?", list_all_columns)
    sensitive_attribute = ["salary-class"]
    # sensitive_attribute = st.multiselect("Which column do you want to select as sensitive attribute?", list_all_columns, key=random.randint(0,1000))
    # print("sensitive:", type(sensitive_attribute))

    if quasi_identifier:

        print(type(quasi_identifier))
        k = anonymity.k_anonymity(read_file, quasi_identifier)
        st.write("k-anonymity is:", k)
        # st.write(report.print_report(read_file, quasi_identifier, sensitive_attribute))
        json_report = report.get_json_report(read_file, quasi_identifier, sensitive_attribute)
        report.get_pdf_report(read_file, quasi_identifier, sensitive_attribute)
        st.json(json_report)


