import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

#Web app title
st.markdown(''' ***THE EDA APP*** 
            
            This is the EDA APP created in Streamlit using pandas''')

#Upload CSV Data
with st.sidebar.header('1. Upload your CSV data: '):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type = ["CSV"])
    st.sidebar.markdown('''[Example SCV Input File]''')

#Pandas ProfilingReport
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header("**INPUT DATA FRAME**")
    st.write(df)
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV File to be uploaded')
    if st.button('Press to use Example Dataset'):
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns = ['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)