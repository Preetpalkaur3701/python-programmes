#!/user/bin/python

import speech_recognition as SR

r = SR.Recognizer()

mic = SR.Microphone()
mic.list_microphone_names()

with mic as source:
	print ("Say Something")
	audio = r.listen(source)
	
try:
	print ("Text: " +r.recognize_google(audio))

except:
	pass
