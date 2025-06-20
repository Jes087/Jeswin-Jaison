input_numbers=[10,3,5,72,50,34,35,70]
numberlist={}
for number in input_numbers:
    if number%1==0:
        numberlist[1]=numberlist.get(1,0)+1
    if number%2==0:
        numberlist[2]=numberlist.get(2,0)+1
    if number%3==0:
        numberlist[3]=numberlist.get(3,0)+1
    if number%4==0:
        numberlist[4]=numberlist.get(4,0)+1
    if number%5==0:
        numberlist[5]=numberlist.get(5,0)+1
    if number%6==0:
        numberlist[6]=numberlist.get(6,0)+1
    if number%7==0:
        numberlist[7]=numberlist.get(7,0)+1
    if number%8==0:
        numberlist[8]=numberlist.get(8,0)+1
    if number%9==0:
        numberlist[9]=numberlist.get(9,0)+1
print(numberlist)

#we could also do this by using nested for loop but time complexity increases 
