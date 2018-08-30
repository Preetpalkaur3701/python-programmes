import vlc
import time
from gtts import gTTS

words = raw_input ("Enter the sentence: ")
Audio = gTTS((words) , lang='en')
Audio.save('hello.mp3')

player = vlc.MediaPlayer("/home/preetpal/Desktop/hello.mp3")
player.play()
time.sleep(1)

for i in range(1,10000000):

	print("Would you like try again?")
	answer = raw_input("Yes/No: ")

	if answer == "Yes":	
		words = raw_input ("Enter the sentence")
		Audio = gTTS((words) , lang='en')
		Audio.save('hello.mp3')
			
		player = vlc.MediaPlayer("/home/preetpal/Desktop/hello.mp3")
		player.play()
		time.sleep(1)
		
	if answer == "No":
		print"Thankyou"	
		break
	

