class bikerent():
    def __init__(self,stock):
        self.stock = stock
    def display(self):
        print("Total bikes",self.stock)
    def rent(self,q):
        if q <=0 :
            print("Enter value greater than zero.")
        elif q > self.stock:
            print("Enter the value less than stock.")
        else:
            self.stock = self.stock - q
            print("Total Price:",q*100)
            print("Total Bikes rented:",q)
        
while True:
    obj = bikerent(100)
    uc = int(input('''
    1. Display Stock
    2. Rent bike (cost per bike = 100/-)
    3. Exit
    '''))
    if uc==1:
        obj.display()
    elif uc==2:
        n = int(input("Enter the number of bikes:"))
        obj.rent(n)
    elif uc==3:
        
        exit()
    else:
        print("Enter Valid choice")