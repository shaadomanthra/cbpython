# # Play hindi and telugu audio

from gtts import gTTS
import os

hindi = gTTS("में  जानता हु की आप इस क्लास केलिए इंतजार कररहेहो ",lang="hi")
hindi.save("hindi.mp3")

telugu = gTTS("మరింక ఆలస్యం ఎందుకు",lang="te")
telugu.save("telugu.mp3")

os.system("mpg321 hindi.mp3")
os.system("mpg321 telugu.mp3")

# os.system("start hindi.mp3") # command for windows
# os.system("start telugu.mp3")
