FROM python:3.8
EXPOSE 8501
WORKDIR /app
COPY app /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["streamlit","run"]
CMD app.py