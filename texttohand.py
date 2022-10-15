import pywhatkit as pw

"""Following are some features of pywhatkit module:

Send WhatsApp messages.
Play a YouTube video.
Perform a Google Search.
Get information on a particular topic.
"""
text = input("Enter the text you want to convert to handwriting :")
pw.text_to_handwriting(text,"hand.png",(0,0,0))
print("END")