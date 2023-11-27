def count_input(n):
    attempts = input("Enter your attempts: ").split(",")
    counter = []
    for i in range(1, n+1):
        counter.append(attempts.count(str(i)))
    return counter

def print_count(lst):
    for i in range(1, len(lst)+1):
        print("{}: {}".format(i,lst[i-1]))

def main():
    sides = int(input("enter number of sides: "))
    count_list= count_input(sides)
    print_count(count_list)
    
main()

    