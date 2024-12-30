from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

def classify_intent(text):
    # Tokenize and encode the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    
    # Get predicted class (assuming you have pre-trained labels)
    predicted_class = torch.argmax(outputs.logits, dim=1)
    return predicted_class

# Example usage
user_input = "What is the status of my order?"
intent = classify_intent(user_input)
print(f"Predicted intent: {intent.item()}")
