number=int(input())
count=1
seq_num=1
while count<=number:
    print(seq_num,end="," if count<number else "")
    seq_num+=2
