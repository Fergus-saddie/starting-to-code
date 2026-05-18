def square_digits(num):
    # answer
    return int(''.join(str(int(x)**2) 
                       for x in str(num)))