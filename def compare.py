import functools
arr=[(2,8,9,7),(3,9,2),(2,9,1,3),(4,5),(3,7,9)]
def compare(x,y):
    if len(x)!=len(y):
        if len(x)>len(y):
            return -1
        else:
            return 1    

    else:
        return -1
y=sorted(arr,key=functools.cmp_to_key(compare))
print(y)


