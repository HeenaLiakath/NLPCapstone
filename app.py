from email import header
from operator import index
from flask import Flask, redirect, url_for, request, render_template,render_template_string
from model import SentimentRecommenderModel


app = Flask(__name__)

sentiment_model = SentimentRecommenderModel()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def prediction():
    # get user from the html form
    user = request.form['userName']
    # convert text to lowercase
    user = user.lower()
    items = sentiment_model.getSentimentRecommendations(user)

    if(not(items is None)):
        print(f"Retrieving items....{len(items)}")
        print(items)
        # data=[items.to_html(classes="table-striped table-hover", header="true",index=False)
        return render_template("index.html", column_names=items.columns.values, row_data=list(items.values.tolist()), zip=zip)
    else:
        return render_template("index.html", message="User Name doesn't exists, No product recommendations at this point of time!")


@app.route('/predictSentiment', methods=['POST'])
def predict_sentiment():
    # get the review text from the html form
    review_text = request.form["reviewText"]
    print(review_text)
    pred_sentiment = sentiment_model.classify_sentiment(review_text)
    print(pred_sentiment)
    return render_template("index.html", sentiment=pred_sentiment)

def api_response():
    from flask import jsonify
    if request.method == 'POST':
        return jsonify(**request.json)


if __name__ == '__main__':
    app.run()
    #app.run(debug=True,port=8000)
    #app.run(port=8000, host='0.0.0.0' )
