def func1(param):
    return param.upper()
y=func1
print(y("computer"))

def func1(param1):
    def func2(param2):
        return param1.upper()+param2.lower()
    return func2
y=func1("computer")    
print(y("science")) 


def func1(func2):
    def func3():
        print("computer")
        func2()
        print("science")
    return func3
@func1
def func2():
    print("department")
func2() 
       