start=2
end=100
print('prime numbers in range ',start,'and',end,'is:')

for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
                print(num)