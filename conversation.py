class Chatbot:
    def __init__(self):
        self.history = []

    def respond(self, user_input):
        # Save user input to history
        self.history.append(f"User: {user_input}")
        
        # Generate a response based on context
        response = self.generate_response(user_input)
        
        # Save the bot response to history
        self.history.append(f"Bot: {response}")
        
        return response

    def generate_response(self, user_input):
        # Simple response generation logic (could be improved with NLP)
        if "order" in user_input:
            return "Your order is being processed."
        elif "hello" in user_input.lower():
            return "Hello! How can I assist you today?"
        else:
            return "Sorry, I didn't understand that."

    def get_conversation_history(self):
        return "\n".join(self.history)

# Example usage
chatbot = Chatbot()
print(chatbot.respond("Hello"))
print(chatbot.respond("What is the status of my order?"))
print(chatbot.get_conversation_history())
