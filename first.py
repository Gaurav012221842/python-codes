with open("computer.png",'rb')as file1:
    data=file1.read()
    print(data)
file3=open("file3.bin",'wb')
file3.write(data)    
with open("computer1.png",'wb')as file2:
    file2.write(data)    
    