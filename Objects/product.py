class Product:
    def __init__(self, name, desc, price, quanlity):
        self.name = name
        self.price = price
        #self.image = image
        self.quanlity = quanlity
        self.desc = desc
    def __str__(self):
        return "name is '%s' , desc is '%s', price is '%s'" % (self.name, self.desc, self.price)

