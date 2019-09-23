from Productcheck import *

def buy(product, num, price):
    if check(product,num)==False:
        print("Sorry! We are out of this product.")  
    else:
        print("You bought " + product + " and spent" + str(num*price))

def main():
    buy("pen", 10, 100)

if __name__ == "__main__":
    main()


