def collect_user_feedback():
    feedback = input("Was this helpful? (Yes/No): ")
    if feedback.lower() == "yes":
        return "Glad I could help!"
    elif feedback.lower() == "no":
        return "Sorry for the inconvenience. I'll try to improve."
    else:
        return "Please reply with 'Yes' or 'No'."

# Example usage
print(collect_user_feedback())
