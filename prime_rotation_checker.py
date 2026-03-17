def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("enter a number: "))
num = str(n)
result = []

for i in range(len(num)):
    rotation = num[i:] + num[:i]
    result.append(int(rotation))
prime = True

for i in result:
    if not is_prime(i):
        prime = False
        

if prime:
    print("Circular prime rotation")
else:
    print("Not a circular prime rotation")