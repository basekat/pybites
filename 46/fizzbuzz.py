def fizzbuzz(num):
    return ', '.join(['Fizz' if x % 3 == 0
                      else 'Buzz' if x % 5 == 0
                      else str(x) for x in range(1, num)])
