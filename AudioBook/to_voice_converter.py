import pyttsx3
#pyttsx3.speak('This is a test word! Is it functioning alright 123, 1 to 10')

#select page by page
def text_to_speech(book):
    for page in book:
        #here i may add anything important that probably needs to happen before the start of a new text on page
        for line in page:
            #this code reads each line
            pyttsx3.speak(line)