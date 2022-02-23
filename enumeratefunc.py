l1 = ["Bhindi","Aloo","Choamine","Chowmein"]
i = 1
for item in l1:
    if i%2 != 0:
        print(f"Jarvis plz buy {item}")
    i +=1

for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"Jarvis plz buy {item}")

