# # Creating an audio file and play

# import google text to speech library
from gtts import gTTS
# import os package
import os

# process text to audio
text = gTTS("welcome to coding bootcamp and happy coding")
# write the file
text.save("welcome.mp3")

# play the file
#os.system("start welcome.mp3") # command for windows
os.system("mpg321 welcome.mp3")
