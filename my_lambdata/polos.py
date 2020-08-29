class Polo():
    def __init__(self, color, size, price, style='normal'):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def fold(self):
        print(f'folding {self.size.upper()}')



if __name__ == "__main__":

    polo = Polo('Blue','Large',99.99, style='fit')
    print(polo.color, polo.size,polo.price,polo.style)
    polo.fold()

    polo2 = Polo(color='Yellow', size='Small', price=69.99)
    print(polo2.color, polo2.size,polo2.price,polo2.style)
    polo2.fold()