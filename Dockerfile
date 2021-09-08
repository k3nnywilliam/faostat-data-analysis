FROM python:3.9
EXPOSE 8501
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD streamlit run app/main.py