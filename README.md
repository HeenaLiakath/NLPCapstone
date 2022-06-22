# NLP Sentiment Based Product Recommendation System - Capstone Project 


**Problem Statement** :
The e-commerce business is quite popular today. Here, you do not need to take orders by going to each customer. A company launches its website to sell the items to the end consumer, and customers can order the products that they require from the same website. Famous examples of such e-commerce companies are Amazon, Flipkart, Myntra, Paytm and Snapdeal.

Suppose you are working as a Machine Learning Engineer in an e-commerce company named 'Ebuss'. Ebuss has captured a huge market share in many fields, and it sells the products in various categories such as household essentials, books, personal care products, medicines, cosmetic items, beauty products, electrical appliances, kitchen and dining products and health care products.

With the advancement in technology, it is imperative for Ebuss to grow quickly in the e-commerce market to become a major leader in the market because it has to compete with the likes of Amazon, Flipkart, etc., which are already market leaders.

As a senior ML Engineer, you are asked to build a model that will improve the recommendations given to the users given their past reviews and ratings. 

**Solution** :

In order to do this, I have built a sentiment-based product recommendation system, which includes the following tasks.

1.Data sourcing and sentiment analysis

2.Building a recommendation system

3.Improving the recommendations using the sentiment analysis model

4.Deploying the end-to-end project with a user interface


The user interface has the following workflow:

1.User enters the username (exisiting in the system database) and submits using the 'Show Recommendations' button.

2.Recommender System runs in the background to recommend products based on their past data.

3.Reviews of these products are passed to Sentiment Classifier to fine-tune the recommendations based on their review sentiments from the user.

4.User enters a review text and submits it using the 'Predict Sentiment' button in order to classify the sentiment.

5.The sentiment of given text(either positive or negative) is returned.

This will eventually improve the recommedations and help the user choose the product effectively.

**Approach** :

1.Exploratory data analysis

2.Data cleaning

3.Text preprocessing

4.Feature extraction: In order to extract features from the text data,i tried WordtoVec and TF-IDF vectorization. The model was built using the TF_IDF vectorization because it is more generalisable. 

5.Training a text classification model: The following four models were built (including handling the class imbalance and performing hyperparameter tuning. 
1. Logistic regression
2. Random forest
3. XGBoost
4. Naive Bayes

Out of these four models, XG Boost classification model had the best performance.

6.Building a recommendation system: I used the following types of recommendation systems.
1. User-based recommendation system
2. Item-based recommendation system

Out of these two, the User-based recommender system had the lowest error(RMSE)

7.Improving the recommendations using the sentiment analysis model: Recommendation of top 20 products based on the XGBoost Classifier and User-based approach and filtering out the top 5 products for recommendation

8.Deployment of this end to end project with a user interface: Using Heroku

**Assumption**: 
The recommender system is built based on the assumption that the dataset doesn't change ie, (No new users or products will be introduced or considered when building or predicting from the models built) 

******************************************************************************************************************

**Recommender System** : Collaborative Filter (User-based) i.e. Similarity b/w users is used for recommendations 

**Sentiment Classifier** : XG Boost Sentiment Classifier model is used

*******************************************************************************************************************

The website is live in Heroku app. Feel free to explore here :
https://productrecommendsys.herokuapp.com/
