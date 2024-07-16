# f=open("file1.txt",'w')
# print(f.write("dsdfjjjj"))
# f.close()

with open("file1.txt","r") as f1:
    print(f1.read())