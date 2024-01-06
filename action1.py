import datetime
import webbrowser
import wikipedia
import text_to_speech
import speech_to_text

def perform_wikipedia_query(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        text_to_speech.text_to_speech(result)
        return result
    except wikipedia.DisambiguationError as e:
        # Handle disambiguation pages
        options = e.options[:2]  # Choose the first two options for simplicity
        text_to_speech.text_to_speech(f"Disambiguation: {', '.join(options)}")
        return f"Disambiguation: {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        text_to_speech.text_to_speech("Sorry, I couldn't find information on that topic.")
        return "Sorry, I couldn't find information on that topic."

def action(data):
    user_data = data
    if 'what is your name' in user_data:
        text_to_speech.text_to_speech('I am Zeira')
        return 'I am Zeira'
    elif 'hello' in user_data:
        text_to_speech.text_to_speech("hey, how can I help you?")
        return "hey, how can I help you?"
    elif 'good morning' in user_data:
        text_to_speech.text_to_speech('good morning,sir')
        return 'good morning,sir'
    elif 'shutdown' in user_data:
        text_to_speech.text_to_speech('okay sir')
        return 'okay sir'
    elif 'what time is it now' in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + 'Hour: ', (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    elif 'play music' in user_data:
        webbrowser.open('https://gaana.com')
        text_to_speech.text_to_speech('gaana.comis now ready for you')
        return 'gaana.comis now ready for you'
    elif 'open google' in user_data:
        webbrowser.open('https://google.com')
        text_to_speech.text_to_speech('Opening Google')
        return 'Opening Google'
    elif 'open youtube' in user_data:
        webbrowser.open('https://youtube.com')
        text_to_speech.text_to_speech('Opening Youtube')
        return 'Opening Youtube'
    elif 'wikipedia' in user_data:
        # Extract the query after 'wikipedia'
        query = user_data.replace('wikipedia', '').strip()
        if query:
            perform_wikipedia_query(query)
        else:
            text_to_speech.text_to_speech('Please specify a topic for the Wikipedia search.')
    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"
