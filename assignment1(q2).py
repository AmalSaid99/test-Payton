int_tuituon= 1000
rate= 0.05
years=10
i=0
curr_year= 1
while(curr_year <=  years):
    print("Tuition in year: "+str(curr_year)+": "+ "$"+str(int_tuituon))
    
    if(curr_year <= 4):
       i+= int_tuituon
       
       curr_year +=1
       
       
print("total cost for 4 years after 10 year: $"+str(i))
