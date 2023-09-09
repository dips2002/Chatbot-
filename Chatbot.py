def DGMiniature_chatbot(user_input):
    user_input = user_input.lower()

    # Convert user input to lowercase for case-insensitivity

    if user_input in ['hello', 'hi', 'hey']:

        return "Hello there! I am DGMiniatureAI."

    elif user_input == "who are you?":

        return "I'm a rule-based chatbot developed by DGMiniature."

    elif user_input == "how are you?":

        return "I'm fine. What about you? I'm here to assist you!"

    elif user_input == "what does artificial intelligence refer to?":

        return "Artificial intelligence (AI) refers to the simulation of human intelligence processes by machines."

    elif user_input == "what's the relationship between ai and ml?":

        return "Machine learning is an application of AI. It's the process of using mathematical models of data to help a computer learn without direct instruction. This enables a computer system to continue learning and improving on its own, based on experience."

    elif user_input == "name some of my friends":

        return "Yeah sure! Bibek, Kuntal, Madhuri... whom I can suggest"

    elif user_input == "name some fruits":

        return "Yeah sure! Mango, Apple, Guava, Grapes are some fruits which I can suggest"

    elif user_input == "name some cities":

        return "Yeah sure! Kolkata, Bengalore, Chennai, Mumbai, Pune ,Hydrabad are some Cities which I can suggest."

    elif user_input in ['bye', 'goodbye']:

        return "Goodbye! Have a great day!"

    else:

        return "I'm sorry, I didn't quite get that. I am a pre-defined chatbot of DGMiniature. Please ask me pre-defined questions"


# Test the chatbot

while True:

    user_query = input("You: ")

    if user_query.lower() == 'exit':
        break

    response = DGMiniature_chatbot(user_query)

    print("Chatbot:",response)