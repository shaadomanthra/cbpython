# # Creating an audio file and play

# import google text to speech library
from gtts import gTTS

# import os package
import os

# process text to audio
text = gTTS("welcome to Xplore")

# write the file
text.save('welcome_to_xplore.mp3')

#play the file
os.system("mpg321 welcome_to_xplore.mp3") # mac command to play mpg321
# os.system("start Warning.mp3") #windows command
