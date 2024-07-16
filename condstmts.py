classesheld=int(input("enter a number of classes held"))
classesattended=int(input("enter classes attended"))
percentage=(classesattended/classesheld)*100
if percentage>=75:
    print("he is eligible  to next class")
else:
    print ("he is not eligible to attend the exam")