def multiples(start, end):
    total = 0
    for i in range(start, end):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
    
print(multiples(1, 1000))