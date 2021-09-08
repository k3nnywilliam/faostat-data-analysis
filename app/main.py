import streamlit as st
from data_preprocessor import DataProcessor
from plotview import PlotView
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

    dp = DataProcessor()

    curDir = os.getcwd()

    dp.load_dataset(path=curDir+'/app/data/FAOSTAT_enteric_emm_9-7-2021.csv')
    dp.process_data()
    df = dp.get_processed_data()
    
    st.title('FAOSTAT data analysis on enteric fermentation')
    st.text('Created by Kenny William Nyallau')
    image = Image.open(curDir+'/app/data/bovine.jpg')
    st.image(image)
    st.write(df)
    
    pv = PlotView()
    pv.display_chart(df, x='Area', y='Value', st=st)