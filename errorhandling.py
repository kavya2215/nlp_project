def handle_ambiguous_query(user_input):
    # Example of handling ambiguous queries
    ambiguous_queries = ["What do you mean?", "Could you please clarify?", "I'm not sure I understood."]
    
    if "?" in user_input:  # Simple check for ambiguous queries
        return ambiguous_queries[0]  # Ask for clarification
    else:
        return "I don't understand your question."

# Example usage
user_input = "?"
response = handle_ambiguous_query(user_input)
print(response)
