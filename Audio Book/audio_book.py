import pyttsx3

book = open(r"book.txt")
book_text = book.readlines()

engine = pyttsx3.init()

for text in book_text:
    engine.say(text)
    engine.runAndWait()
