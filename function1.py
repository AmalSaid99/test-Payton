def grade_avg(x):
    sum2= 0
    for i in range(1, x+1):
        grade= float(input("enter student grade: "))
        sum2= grade
    avg= sum2/x
    return avg
print(grade_avg(2))