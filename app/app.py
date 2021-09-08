import streamlit as st
from data_preprocessor import DataProcessor
from data_view import DataView
from PIL import Image
import os

if __name__ == "__main__":

    hide_streamlit_style = """
            <style>
            <!--# MainMenu {visibility: hidden;}-->
            footer {visibility: hidden;}
            </style>
            """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.title('FAOSTAT data analysis on enteric fermentation')
    st.text('Created by Kenny William Nyallau')
    curr_dir = os.getcwd()
    image = Image.open(curr_dir+'/app/data/bovine.jpg')
    st.image(image)
    
    dp = DataProcessor()
    dv = DataView()

    dp.load_dataset(curr_dir+'/app/data/FAOSTAT_enteric_emm_9-7-2021.csv')
    dp.process_data()
    df = dp.get_processed_data()

    dv.display_dataframe(df, st)
    dv.display_chart(df, x='Area', y='Value', st=st)