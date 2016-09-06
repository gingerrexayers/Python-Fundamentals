for i in range(1, 2001):
    temp = "odd"
    if i % 2 == 0:
        temp = "even"
    print "Number is " + str(i) + ". This is an " + temp + " number."
