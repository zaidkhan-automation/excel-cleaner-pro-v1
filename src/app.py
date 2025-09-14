"""
app.py
Streamlit front-end for Excel Cleaner Pro v1.
Run with: streamlit run src/app.py
"""

import streamlit as st
import pandas as pd
from io import BytesIO
from cleaner import clean_pipeline
import base64

st.set_page_config(page_title='Excel Cleaner Pro v1', layout='centered')

st.title('Excel Cleaner — Pro v1')
st.write('Upload an Excel or CSV file. Choose cleaning actions and download a cleaned file.')

uploaded = st.file_uploader('Upload Excel/CSV', type=['xlsx', 'xls', 'csv'])

if uploaded is not None:
    try:
        if uploaded.name.lower().endswith('.csv'):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
    except Exception as e:
        st.error(f'Could not read the uploaded file: {e}')
        st.stop()

    st.subheader('Preview — first 10 rows (raw)')
    st.dataframe(df.head(10))

    # Sidebar options
    st.sidebar.header('Cleaning options')
    remove_dup = st.sidebar.checkbox('Remove duplicates', value=True)
    missing_strategy = st.sidebar.selectbox('Missing data', ['fill', 'drop', 'fill_column_mode'])
    fill_value = st.sidebar.text_input('Fill value (for "fill")', value='')
    text_standardize = st.sidebar.checkbox('Standardize text (trim/lowercase)', value=True)
    parse_dates_input = st.sidebar.text_input('Columns to parse as dates (comma-separated)', value='')
    format_numbers_input = st.sidebar.text_input('Columns to format as numbers (comma-separated)', value='')

    parse_date_columns = [c.strip() for c in parse_dates_input.split(',') if c.strip()] if parse_dates_input else None
    format_number_columns = [c.strip() for c in format_numbers_input.split(',') if c.strip()] if format_numbers_input else None

    if st.button('Run cleaning'):
        cleaned = clean_pipeline(df,
                                 remove_dup=remove_dup,
                                 missing_strategy=missing_strategy,
                                 fill_value=fill_value,
                                 text_standardize=text_standardize,
                                 parse_date_columns=parse_date_columns,
                                 format_number_columns=format_number_columns)
        st.subheader('Preview — first 10 rows (cleaned)')
        st.dataframe(cleaned.head(10))

        # Provide download link
        towrite = BytesIO()
        cleaned.to_excel(towrite, index=False, engine='openpyxl')
        towrite.seek(0)
        b64 = base64.b64encode(towrite.read()).decode()
        href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="cleaned.xlsx">Download cleaned Excel</a>'
        st.markdown(href, unsafe_allow_html=True)