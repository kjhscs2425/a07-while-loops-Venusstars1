# write a factorial function, given n, you return n!

number = 1
product = 1
while number <= 30:
        print (f"{number}! is {product}")
        number = number + 1
        product = number * product
print ("This factorial number is too large")