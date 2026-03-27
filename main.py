from src.model import train_models
from src.predict import predict_sentiment

def main():
    print("Training models...")
    vectorizer, model = train_models()

    print("\nEnter text (type 'exit' to quit):")

    while True:
        user_input = input(">> ")

        if user_input.lower() == 'exit':
            break

        result = predict_sentiment(user_input, vectorizer, model)
        print("Sentiment:", result)

if __name__ == "__main__":
    main()