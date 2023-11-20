def main ():
    result= sum_no (1,4,3)
    print(result)
    
def sum_no (*args):
    sum1=0
    for n in args:
        sum1+=n
        return sum1
result= sum_no
main()

    
