def sum_no (*args):
    sum1=0
    for n in args:
        sum1+=n
        return sum1
result= sum_no(1,4)
print(result)
result= sum_no(1,9,5)
print(result)
    