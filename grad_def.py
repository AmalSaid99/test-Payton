def grade_exam(numQuesition, markForEach):
    sum_mark=0
   answer=input("enter answer for {} questins".format(numQuesition))
    user_answer=input("enter your answer: ")
    for i in range(len(answer)):
        if(user_answer[i] == answer[i]):
        sum_mark+= markForEach
    print(sum_mark, "out of", len(answer)*markForEach)
grade_exam(12,2)
