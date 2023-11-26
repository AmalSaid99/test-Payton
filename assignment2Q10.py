def cal(word_list, n):
    result = []
    for word in word_list:
        if len(word) > n:
            result.append(word)
    return result
word_list= input("enter a list of words: ").split()
n = int(input("enter the min len (n) "))

f= cal(word_list, n)

print("word longer than", n, ":")
print(f)