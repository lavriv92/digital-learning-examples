cache = {}

while True:
    n = int(input('Enter number to calculate factorial: '))

    fact = cache.get(n)

    if fact is None:
        fact = 1
        if n == 0:
            fact = 1
        else:
            for i in range(1, n + 1):
                fact *= i
            
            cache[n] = fact
    else:
        print('Value is extracted from cache')
        
    print(f'Factorial of {n} is ', fact)