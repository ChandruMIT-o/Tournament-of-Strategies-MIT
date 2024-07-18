import streamlit as st
import pandas as pd

st.title("Tournament Ranklist Hosting Web App")

st.sidebar.title("Upload Tournament Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Display the raw data
    st.write("### Raw Data")
    st.dataframe(df)

    # Assuming the CSV has 'Name', 'Wins', 'Losses', 'Draws', 'Points' columns
    # If the column names are different, adjust accordingly
    if all(col in df.columns for col in ['Name', 'Wins', 'Losses', 'Draws', 'Points']):
        
        # Sort by points
        df = df.sort_values(by='Points', ascending=False).reset_index(drop=True)

        # Display the rank list
        st.write("### Rank List")
        st.dataframe(df)

        # Display summary statistics
        st.write("### Summary Statistics")
        st.write(df.describe())
    else:
        st.write("Uploaded CSV does not have the required columns: 'Name', 'Wins', 'Losses', 'Draws', 'Points'.")

else:
    st.write("Please upload a CSV file to display the rank list.")
