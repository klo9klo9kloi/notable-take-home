import transcription_format_api

def test1():
	inpt = "Patient presents today with several issues. Number one BMI has increased by 10\% since their last visit. Number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks."
	expected_output = "Patient presents today with several issues.\n1. BMI has increased by 10\% since their last visit.\n2. Patient reports experiencing dizziness several times in the last two weeks.\n3. Patient has a persistent cough that hasn’t improved for last 4 weeks."
	assert(transcription_format_api.format_list(inpt) == expected_output)

def test2():
	inpt = "Patient presents today with several issues. Number nine BMI has increased by 10\% since their last visit. Number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks."
	expected_output = "Patient presents today with several issues.\n9. BMI has increased by 10\% since their last visit.\n10. Patient reports experiencing dizziness several times in the last two weeks.\n11. Patient has a persistent cough that hasn’t improved for last 4 weeks."
	assert(transcription_format_api.format_list(inpt) == expected_output)

def test3():
	inpt = ""
	expected_output = ""
	assert(transcription_format_api.format_list(inpt) == expected_output)

def test4():
	inpt = "Hello world! \n\n\n\n\n\n"
	expected_output = "Hello world! \n\n\n\n\n\n"
	assert(transcription_format_api.format_list(inpt) == expected_output)

def test5():
	inpt = "Number BMI"
	expected_output = "Number BMI"
	assert(transcription_format_api.format_list(inpt) == expected_output)

def test5():
	inpt = "Numberone"
	expected_output = "Numberone"
	assert(transcription_format_api.format_list(inpt) == expected_output)

def test6():
	inpt = "Start. Number one patient is a-okay!"
	expected_output = "Start.\n1. Patient is a-okay!"
	assert(transcription_format_api.format_list(inpt) == expected_output)


test1()
test2()
test3()
test4()
test5()
test6()
print("Passed all test cases!")