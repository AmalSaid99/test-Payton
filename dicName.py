# dic inside dic
dic= {1:{"name": "ali", "age": 23},
      2:{"name": "Muna", "age": 22}}
for key in dic:
    for key1 in dic[key]:
        print(dic[key][key1])