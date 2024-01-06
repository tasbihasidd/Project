import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('rate')
    # to set voice or to choose voice
    engine.setProperty('rate', 'rate-70')
    engine.say(text)
    engine.runAndWait()
# text_to_speech('hello world')