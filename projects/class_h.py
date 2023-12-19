class PhoneBran:
    def __init__(self, model, colors, price):
        self.model = model
        self.colors = colors
        self.price = price

    def new_model(self, new_model):
        self.model = new_model

    def add_color(self, add_color):
        self.colors = add_color

    def change_price(self, c_price):
        self.price = c_price


    