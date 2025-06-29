import pyttsx3

print("-------------------TEXT TO SPEECH-------------------\n")
while True:
        engine = pyttsx3.init()
        text = input("Enter your text : ").lower()
        if(text == 'quit'):
            break
        else:
            engine.say(text)
            engine.runAndWait()
    