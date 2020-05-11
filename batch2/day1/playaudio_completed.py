# # Creating an audio file and play

# import google text to speech library
from gtts import gTTS

# import os package
import os

# process text to audio
text = gTTS("welcome to Xplore)

# write the file
text.save('welcome_to_xplore.mp3')

#play the file
os.system("start welcome_to_xplore.mp3") #windows command
