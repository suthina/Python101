class Restaurant:
    # Attribute
    restaurantName = 'ครัวไวท์เฮ้าส์'

    # Contructor
    def __init__(self, typefood = 'Japanesefood'):
        print ('KONNICHIWA')
        self.typefood = typefood

    # Method
    def hello(self):
        print('สวัสดีลูกค้าทุกคน ยินดีต้อนรับสู่ร้านของเรา')

    def sell(self):
        print(f'ร้านของเรา ขายอาหาร {self.typefood}')

    def order(self):
        print('ลูกค้าสามารถเลือกสั่งอาหารในเมนู')

class Customer(Restaurant):
    def __init__(self, fullname, sex, price, typefood):
        super().__init__(typefood)
        self.fullname = fullname
        self.sex = sex
        self.price = price

    def checkDiscount(self):
        if self.price >= 1500:
            print(f'ราคา {self.price} ส่วนลด 100 บาท')
        elif self.price >= 800:
            print(f'ราคา {self.price} ส่วนลด 50 บาท')
        else:
            print(f'ราคา {self.price} ไม่มีส่วนลด')

# Instance
# restaurant1 = Restaurant('Thaifood')
# print(f'ชื่อร้านอาหาร : {restaurant1.restaurantName}')
# restaurant1.hello()
# restaurant1.sell()
# restaurant1.order()
print('===============================')
customer01 = Customer('คุณฟ้าใส', 'หญิง', 500, 'ยากินิกุ')
customer01.hello()
print(f'ชื่อร้าน {customer01.restaurantName}')
print(f'ชื่อลูกค้า {customer01.fullname}')
print(f'เพศ {customer01.sex}')
print(f'ชื่ออาหาร {customer01.typefood}')
customer01.checkDiscount()
print('===============================')
customer02 = Customer('คุณต้นกล้า', 'ชาย', 1600, 'ไคเซกิ')
customer02.hello()
print(f'ชื่อร้าน {customer02.restaurantName}')
print(f'ชื่อลูกค้า {customer02.fullname}')
print(f'เพศ {customer02.sex}')
print(f'ชื่ออาหาร {customer02.typefood}')
customer02.checkDiscount()
print('===============================')
customer03 = Customer('คุณสายฟ้า', 'ชาย', 450, 'ชาบู')
customer03.hello()
print(f'ชื่อร้าน {customer03.restaurantName}')
print(f'ชื่อลูกค้า {customer03.fullname}')
print(f'เพศ {customer03.sex}')
print(f'ชื่ออาหาร {customer03.typefood}')
customer03.checkDiscount()
print('===============================')
customer04 = Customer('คุณแพรวา', 'หญิง', 650, 'ซาชิมิ')
customer04.hello()
print(f'ชื่อร้าน {customer04.restaurantName}')
print(f'ชื่อลูกค้า {customer04.fullname}')
print(f'เพศ {customer04.sex}')
print(f'ชื่ออาหาร {customer04.typefood}')
customer04.checkDiscount()


