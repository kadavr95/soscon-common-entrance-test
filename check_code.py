counter = 0
v = 1000
while v <= 1500:
    n = v
    r = n
    while r >= 100:
        r = 0
        while n > 0:
            r += n % 100
            n //= 100
        n = r
    if r % 11 == 0:
        counter += 1
    print(v)
    v += 1

print(counter)
