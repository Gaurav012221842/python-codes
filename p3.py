from functools import reduce
n=[2,4,5,4,]

# num=0
# for i in n:
#     num=num+i
# print(num)
s=reduce(lambda x,y:x+y,n)
print(s)
    