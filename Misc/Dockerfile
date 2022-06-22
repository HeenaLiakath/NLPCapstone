FROM python:3.8

WORKDIR /deployment

COPY requirements.txt .

RUN pip install -r requirements.txt

#ADD app.py .
#ADD model.py .
COPY git/dataset/sample30.csv ./dataset/
COPY git/templates/index.html ./templates/
COPY git/pickle/cleaned-data.pkl ./pickle/
COPY git/pickle/tfidf-vectorizer.pkl ./pickle/
COPY git/pickle/xg-boost-final-model.pkl ./pickle/
COPY git/pickle/user_final_rating.pkl ./pickle/


COPY ./git ./git


ENTRYPOINT ["python"]

CMD ["./git/app.py", "--host", "0.0.0.0"]
#CMD ["./git/app.py"]
