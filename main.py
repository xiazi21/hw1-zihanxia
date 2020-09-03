temp =input('Enter your course 1 letter grade: ')
c1=float(input('Enter your course 1 credit: '))
if temp== "A":
 g =4.0
elif temp =="A-":
 g=3.67
elif temp=="B+":
 g=3.33
elif temp =="B":
 g=3.0
elif temp =="B-":
 g=2.67
elif temp =="C+":
 g=2.33
elif temp =="C":
 g=2.0
elif temp =="D":
 g=1.0
else :
 g=0
print (f' Grade point for course 1 is: {g}')
temp1 =input('Enter your course 2 letter grade: ')
c2=float(input('Enter your course 2 credit: '))
if temp1== "A":
 g1 =4.0
elif temp1 =="A-":
 g1=3.67
elif temp1=="B+":
 g1=3.33
elif temp1 =="B":
 g1=3.0
elif temp1 =="B-":
 g1=2.67
elif temp1 =="C+":
 g1=2.33
elif temp1 =="C":
 g1=2.0
elif temp1 =="D":
 g1=1.0
else :
 g1=0
print(f' Grade point for course 2 is: {g1}')
temp2 =input('Enter your course 3 letter grade: ')
c3=float(input('Enter your course 3 credit: '))
if temp2== "A":
 g2 =4.0
elif temp2 =="A-":
 g2=3.67
elif temp2=="B+":
 g2=3.33
elif temp2 =="B":
 g2=3.0
elif temp2 =="B-":
 g2=2.67
elif temp2 =="C+":
 g2=2.33
elif temp2 =="C":
 g2=2.0
elif temp2 =="D":
 g2=1.0
else :
 g2=0
print(f" Grade point for course 3 is: {g2}")
GPA=((g*c1)+(g1*c2)+(g2*c3))/(c1+c2+c3)
print(f" Your GPA is:{GPA}")#1