import pyttsx3

print("-------------------TEXT TO SPEECH-------------------\n")
while True:
        engine = pyttsx3.init()
        text = input("Enter your text : ").lower()
        if(text == 'quit'):
            engine.say("Byee Byee Aditya")
            engine.say(text)
            engine.runAndWait()
            break
        else:
            engine.say(text)
            engine.runAndWait()
    