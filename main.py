# # Python program to show
# # how to convert text to speech
# import pyttsx3

# # Initialize the converter
# converter = pyttsx3.init(
# )

# converter1 = pyttsx3.init()

# converter1.setProperty('rate', 150)
# converter1.setProperty('volume', 0.7)
# voice = converter1.getProperty('voices')
# converter1.setProperty('voice', voice[1].id)
# converter1.say("Hello Humza Khan")
# converter1.say("I'm also a Abdullah")





# # Set properties before adding
# # Things to say

# # Sets speed percent
# # Can be more than 100
# converter.setProperty('rate', 150)
# # Set volume 0-1
# converter.setProperty('volume', 0.7)




# # Queue the entered text
# # There will be a pause between
# # each one like a pause in
# # a sentence
# converter.say("Hello Humza Khan")
# converter.say("I'm also a Abdullah")



# # Empties the say() queue
# # Program will not continue
# # until all speech is done talking
# converter.runAndWait()
# converter1.runAndWait()

import pyttsx3 

def voiceChange():
    eng = pyttsx3.init()
    voice = eng.getProperty('voices') 
    eng.setProperty('voice', voice[0].id) 
    eng.say("Hello Humza Khan")
    eng.setProperty('voice', voice[1].id) 
    eng.say("Hello Humza Khan")
    eng.runAndWait() 

if __name__ == "__main__":
    voiceChange()

