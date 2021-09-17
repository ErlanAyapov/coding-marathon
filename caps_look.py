def normalize(text):
	if text == text.upper():
		return text.capitalize() + '!' 
	else:
		return text