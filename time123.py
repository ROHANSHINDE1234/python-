import time
intial = time.time()
print(intial)
k = 0
while(k<5):
    print("This is me")
    time.sleep(2)
    k+=1
print("While loop ran in",time.time()- intial,"Seconds")
intial2 = time.time()
for i in range(5):
     print("This is me")
print("For loop ran in",time.time()- intial2,"Seconds")

local_time = time.asctime(time.localtime(time.time()))
print(local_time)

