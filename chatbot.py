# Basic Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot.\n--------------- Type 'bye' to exit ---------------")

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input:
            print("Chatbot: Goodbye! It was nice chatting with you!")
            break

        elif any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good evening"]):
            print("Chatbot: Hi there! How are you today?")

        elif "how are" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking. How about you?")

        elif any(phrase in user_input for phrase in ["i am fine", "i am good", "fine", "good", "doing well"]):
            print("Chatbot: That’s great to hear!")

        elif any(phrase in user_input for phrase in ["not good", "sad", "tired", "bad", "upset"]):
            print("Chatbot: I'm sorry to hear that. Remember, tough times don’t last, but tough people do!")

        elif "your name" in user_input:
            print("Chatbot: I’m ChatBuddy, your friendly Python chatbot! What’s your name?")

        elif "my name is" in user_input:
            name = user_input.split("my name is")[-1].strip().capitalize()
            print(f"Chatbot: Nice to meet you, {name}!")
\
        elif "what do you do" in user_input or "your hobby" in user_input:
            print("Chatbot: I love chatting and learning new things! What about you?")

        elif "my hobby" in user_input or "i like" in user_input:
            print("Chatbot: That sounds fun! It’s great to have hobbies you enjoy.")

        elif "weather" in user_input:
            print("Chatbot: I can’t see outside, but I hope the weather is nice where you are!")

        elif "can you do" in user_input:
            print("Chatbot: I can chat with you, answer simple questions, and keep you company!")

        elif "python" in user_input:
            print("Chatbot: Python is my favorite language! It’s simple and powerful.")

        elif "programming" in user_input or "coding" in user_input:
            print("Chatbot: Coding is amazing! It helps you build anything from games to AI.")

        else:
            print("Chatbot: Hmm, I’m not sure I understand. Could you say that another way?")

# Run the chatbot
chatbot()
