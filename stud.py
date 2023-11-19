avg= 0
sum2= 0
stud= int(input("number of students: "))
for i in range(1,stud+1):
    grade= float(input("enter a student grade: "))
    sum2= grade
avg= sum2/stud
print(avg)