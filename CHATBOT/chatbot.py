import datetime
import random
import webbrowser

def simple_chatbot(user_input):
    greetings = ["hello", "hi dhruba", "hey", "howdy"]
    date_keywords = ["date", "day", "today", "time"]
    search_keywords = ["search", "open"]
    joke_keywords = ["joke", "funny", "laugh"]
    compliment_keywords = ["compliment", "nice", "good"]
    music_keywords = ["music", "song"]
    calculator_keywords = ["calculate", "math", "solve"]
    last_keyword = ["bye", "goodbye", "exit", "quit"]

    user_input_lower = user_input.lower()
    open_website = None

    if any(word in user_input_lower for word in greetings):
        return "Hello! How can I help you today?"

    elif any(word in user_input_lower for word in date_keywords):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"The current date and time is: {current_time}"

    elif any(word in user_input_lower for word in search_keywords):
        open_website = user_input.replace("search", "").replace("open", "").strip()
    
    elif any(word in user_input_lower for word in compliment_keywords):
        return "You are very kind..!  Thank you"
    
    elif any(word in user_input_lower for word in music_keywords):
        return  "please enter the song name to play it.."
    
 
    
    # For opening website in browser
    if open_website:
        webbrowser.open(f"https://www.google.com/search?q={open_website}")
        return f"Opening search results for {open_website}."
    
    # pre-difine jokes 
    elif any(word in user_input_lower for word in joke_keywords):
        jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!",
                 "I told my wife she should embrace her mistakes. She gave me a hug.",
                 "Why don't scientists trust atoms? Because they make up everything!"]
        return random.choice(jokes)
    
    # Calculate mathematical problems
    elif any(word in user_input_lower for word in calculator_keywords):
        expression = user_input_lower.replace("calculate", "").replace("math", "").replace("solve", "").strip()
        try:
            result = eval(expression)
            return f"The result of {expression} is: {result}"
        except ZeroDivisionError:
            return "Cannot divide by zero."
        except Exception as e:
            return f"Error in the calculation: {str(e)}"

    # ... (rest of the conditions)

    elif any(word in user_input_lower for word in last_keyword):
        return "Goodbye! If you have more questions, feel free to ask later."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Continuous conversation loop
while True:
    user_query = input("You: ")
    if user_query.lower() == "stop":
        print("Bot: Goodbye! If you have more questions, feel free to ask later.")
        break
    else:
        response = simple_chatbot(user_query)
        print("Bot:", response)

# created by Dhruba Singha Roy (CODSOFT INTERNSHIP)