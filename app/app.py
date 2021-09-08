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
    img_path = (curr_dir, '/app/data/bovine.jpg')
    image = Image.open("".join(img_path))
    st.image(image)
    
    dataprocessor = DataProcessor()
    dataviewer = DataView()

    data_path = (curr_dir, '/app/data/FAOSTAT_enteric_emm_9-7-2021.csv')
    dataprocessor.load_dataset("".join(data_path))
    dataprocessor.process_data()
    data = dataprocessor.get_processed_data()

    dataviewer.display_dataframe(data, st)
    dataviewer.display_chart(data, x='Area', y='Value', st=st)