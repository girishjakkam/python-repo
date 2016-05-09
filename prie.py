def is_prime(x):
    a=1
    b=0
    while a>=1 and a<=9:
        if x%a==0 and x>0:
            a=a+1
            b=b+1
            print a
            if b<=2:
                print b
                print "prime number"
                return True
            else:
                print "not a prime number"
                return False

x=raw_input("enter a number:")  
is_prime(x) 

