# Sentiment Analysis using Machine Learning

## 📌 Overview

This project performs sentiment analysis on user-provided text using machine learning techniques. It classifies input text as either **Positive** or **Negative**.

The system uses Natural Language Processing (NLP) techniques along with machine learning models to understand and predict sentiment.

---

## ⚙️ Features

* Text preprocessing (lowercasing, punctuation removal, stopwords removal)
* TF-IDF vectorization for feature extraction
* Multiple machine learning models:

  * Naive Bayes
  * Logistic Regression
* Model accuracy comparison
* Command Line Interface (CLI) based interaction
* Real-time sentiment prediction

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK

---

## 📂 Project Structure

```
sentiment-analysis-project/
│
├── data/
│   └── dataset.csv
│
├── src/
│   ├── preprocess.py
│   ├── model.py
│   └── predict.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```
git clone https://github.com/kartikmodi2006-ctrl/sentiment-analysis-project
cd sentiment-analysis-project
```

### Step 2: Create Virtual Environment

```
python -m venv venv
.\venv\Scripts\Activate
```

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
python main.py
# or on Linux
python3 main.py
```

---

## 💡 Usage

* After running the program, enter any text in the terminal.
* The model will predict whether the sentiment is **positive** or **negative**.
* Type `exit` to stop the program.

---

## 📊 Example

```
Training models...
Naive Bayes Accuracy: 0.85
Logistic Regression Accuracy: 0.90

>> I love this product
Sentiment: positive

>> This is terrible
Sentiment: negative
```

---

## 📈 Methodology

1. Load dataset from CSV file
2. Clean and preprocess text
3. Convert text into numerical form using TF-IDF
4. Split data into training and testing sets
5. Train multiple machine learning models
6. Evaluate model performance using accuracy
7. Use the best model for predictions

---

## 📌 Output

* Displays accuracy of models
* Predicts sentiment (Positive/Negative) for user input

---

## 🔮 Future Improvements

* Use deep learning models (LSTM, BERT)
* Deploy as a web application
* Use larger real-world datasets (IMDb, Twitter)
* Add GUI or web interface

---

## 👨‍💻 Author

Kartik Modi

---

## 📎 Notes

* This project is fully executable via command line as required.
* The repository is public for evaluation purposes.
## Linux Execution
This project is fully compatible with Linux environments and has been successfully tested using WSL (Windows Subsystem for Linux).