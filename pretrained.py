from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample data
data = [
    ("How can I check my order?", "order_status"),
    ("Where is my package?", "order_status"),
    ("I want to book a flight", "booking"),
    ("Can I cancel my reservation?", "booking")
]

# Vectorizing the text data
X_train = [item[0] for item in data]
y_train = [item[1] for item in data]
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Training a classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

def classify_intent(user_input):
    user_input_vectorized = vectorizer.transform([user_input])
    intent = classifier.predict(user_input_vectorized)[0]
    return intent

# Example usage
user_input = "How do I check the status of my order?"
intent = classify_intent(user_input)
print(f"Predicted intent: {intent}")
