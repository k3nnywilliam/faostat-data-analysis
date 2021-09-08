FROM python:3.8
EXPOSE 8501
WORKDIR /apps
COPY app/. /apps/
RUN pip3 install -r requirements.txt
ENTRYPOINT ["streamlit","run"]
CMD ["apps/app.py"]