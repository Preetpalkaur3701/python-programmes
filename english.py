punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# take input from the user
a = input("write the sentence: ")
 
# remove punctuation from the string
no_punct = ""
# char means character.
for char in a:
   if char not in punctuations:
       no_punct = no_punct + char
 
# display the unpunctuated string
print(no_punct)

