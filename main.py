import time


secret_word="Enter your name"
guses=""
limit=5
count=0
out_of_guses=False
while guses!=secret_word and not out_of_guses:
  if count<limit:
    count+=1
    print("Enter password")
    guses=input()
  else:
    out_of_guses=True
    
if out_of_guses:
  print("you lose")
  guses=time.sleep(30)
else:
  print("you win")
  