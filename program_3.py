input1=int(input())
number=input1 if input1%2!=0 else input1-1
count=1
seq_num=1
while count<=number:
    print(seq_num,end="," if count<number else "")
    seq_num+=2
    count+=1
