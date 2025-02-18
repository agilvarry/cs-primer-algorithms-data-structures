multiples = 0

for i in range(0,1000, 3):
    multiples += i
for i in range(0,1000, 5):
    if i%15!=0:
        multiples += i  
print(multiples)