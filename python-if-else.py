n = int(input().strip())
check = {True:"Not Weird" , False: "Weird"}

print(check[n % 2 == 0 and  n in range(6,20) or n > 20 ])