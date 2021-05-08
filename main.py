import sys
import transcription_format_api

if __name__ == "__main__":
	args = sys.argv[1:]
	assert(len(args) >= 1), "Please specify filepath!"

	with open(args[0]) as f:
		lines = f.readlines()

	result = transcription_format_api.format_list("".join(lines))
	print("Formatted result: \n")
	print(result)
