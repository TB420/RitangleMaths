left = [1,2,3,4,5,6,7,8]

middle = [10,11,12,13,14,15,16,17,18,19,20]

right = [1,2,3,4,5,6,7,8,9]

t = 0 


for i in left: 
    for k in middle: 
        for r in right: 
            t += i * k * r


print(t)
  
