from survery import AnonymousSurvery
#定义一个问题，并创建一个表示调查的AnonymousSurvery对象
question="What language did you first learn to speak?"
my_survery=AnonymousSurvery(question)

#显示问题并存存储答案
my_survery.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response=input("Language: ")
	if response=='q':
		break
	my_survery.store_response(response)
	
#显示调查结果
print("\nThank you to evevryone who parcticipated in the survery!")
my_survery.show_results()
