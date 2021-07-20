def parr(arr1):
  print("printed matrix is:")
  for x in arr1:
    for y in x:
        print(y,end = " ")
    print()
print("enter the number of nodes")
n = input()
print("enter the input matrix for "+n+" elements")
rows, cols = (int(n), int(n))
arr =[]
recieved=[]
rec_line=[]
sent_line=[]
for i in range(0,int(n)):
  recieved.append(0)
for x in range(0,int(n)):
    rec_line.append(0)
    sent_line.append(0)
for x in range(int(n)):
    arr.append([int(y) for y in input().split()])
for i in range(0,int(n)):
  for j in range(0,int(n)):
    if(arr[i][j]>0):
      arr[i][j]=1
recieved[0]=1
sent_line[0]=1
count1=0
count2=1
l=list()
while(True):
  print("---------------------------------------------")
  for xi in range(0,int(n)):
    if xi in l:
      rec_line[xi]=1
    else:
      rec_line[xi]=0
  rec_count=0
  for i in range(0,int(n)):
    if(recieved[i]==1):
      rec_count+=1
  if(rec_count==int(n) or count1==rec_count):
    print("done")
    break
  else:
    count1=rec_count
    rec_line=sent_line
    l=[]
    for j in range(0,int(n)):
      if(rec_line[j]==1):
        for y in range(0,int(n)):
          if(arr[j][y]==1):
            if(recieved[y]==0):
              print("packet sent from ",j," ---> ",y)
              l.append(y)
              recieved[y]=1
            else:
              print("packet sent from ",j," ---> ",y,"AND has ",y," has discarded the packet")
















