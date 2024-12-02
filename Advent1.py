
#print (open('input').read())
input = open('input').read()
inputraw=input.splitlines()
lines =inputraw
#print (lines[0])
number1= lines[0].split()
#print (number1)
list1 = []
list2 = []
#print (list1)
#print (list2)

for line in lines:
    numbers = line.split()
    list1.append(numbers[0])
    list2.append(numbers[1])
#print(list1 , list2)
list1.sort()
print (list1)
list2.sort()
print(list2)

distances=[]
for i in range (len(list1)):
    distances.append(abs(int(list1[i]) - int(list2[i])))
print (distances)

result= sum(distances)
print(result)













