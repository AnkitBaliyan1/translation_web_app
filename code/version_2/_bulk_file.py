import streamlit as st
import pandas as pd

def main():
    st.title("Bulk file translation")

    dummy_df = pd.DataFrame()


import streamlit as st
import pandas as pd
import io
import base64

# Function to download data
def get_table_download_link(df, filename, text):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href


def main():
    st.title("Bulk file translation")

    # Display a sample dataframe
    st.write("Sample DataFrame:")
    sample_df = pd.DataFrame(columns=['input', 'output'])
    st.write("Enter your data in Input column.")
    st.write(sample_df)

    # File uploader
    uploaded_file = st.file_uploader("Upload a file (CSV or Excel)", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Perform operation on 'input' column
        df['output'] = df['input'].apply(lambda x: x + " processed")  # Replace with your operation

        # Show processed DataFrame
        st.write("Processed DataFrame:")
        st.write(df)

        # Download link
        st.markdown(get_table_download_link(df, 'processed_data.csv', 'Download Processed Data as CSV'), unsafe_allow_html=True)

    