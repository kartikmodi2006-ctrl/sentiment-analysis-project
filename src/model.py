import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from src.preprocess import clean_text

def train_models():
    df = pd.read_csv("data/dataset.csv")

    df['text'] = df['text'].apply(clean_text)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['text'])
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    nb = MultinomialNB()
    lr = LogisticRegression()

    nb.fit(X_train, y_train)
    lr.fit(X_train, y_train)

    nb_pred = nb.predict(X_test)
    lr_pred = lr.predict(X_test)

    print("Naive Bayes Accuracy:", accuracy_score(y_test, nb_pred))
    print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_pred))

    return vectorizer, lr