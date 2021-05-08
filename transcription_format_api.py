def format_list(transcription, debug=False):
	# first check if we received a valid transcription object
	if transcription is None:
		if debug:
			print("Warning: received null transcription text!")
		return None

	# then check if there is a list to format
	text_parts = transcription.split("Number ")
	if len(text_parts) == 1: 
		if debug:
			print("No list found; please check transcription if this is unexpected!")
		return transcription

	# keep everything before the list_item
	transcription_formatted = text_parts[0].strip()

	# check what our starting num is and if it is valid
	start_num_s = text_parts[1].split(" ")[0].strip().lower()
	word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
	if start_num_s not in word_to_num:
		if debug:
			print("Error: could not understand list format!")
		return transcription

	# add all of the list with proper formatting
	num = word_to_num[start_num_s]
	for i in range(1, len(text_parts)):
		transcription_formatted += '\n' # start new line
		list_item = " ".join(text_parts[i].split(" ")[1:]).strip() # reform list item text
		transcription_formatted += str(num) + ". " + list_item[0].upper() + list_item[1:] # add it to formatted transcription with extras and capitalization
		num += 1

	return transcription_formatted






