FROM python:3.9
EXPOSE 8501
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD streamlit run app/main.py