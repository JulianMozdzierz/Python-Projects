from cart import *

phone1 = Phone("Iphone 17 PRO" , 5000, "Black")
tv1 = Tv("Samsung", 7000, 70)
tv2 = Tv("Hisense" , 5000, 68)

cart = Cart()
cart.addProduct(phone1)
cart.addProduct(tv1)
cart.addProduct(tv2)
print(cart)