from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.price * self.quantity
class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return promo_func
@promotion
def fidelity(order):
    '''为积分1000或以上的顾客提供5%折扣'''
    return order.total()*0.05 if order.customer.fidelity >= 1000 else 0
@promotion
def bulk_item(order):
    '''单个商品为20个或以上时提供10%折扣'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total()*.1
    return discount
@promotion
def large_order(order):
    '''订单中的不同商品达到10个或以上时提供7%折扣'''
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total()*.07
    else:
        return 0
def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)
if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    print(Order(joe, cart, fidelity))
    print(Order(joe, cart, bulk_item))
    print(Order(joe, cart, large_order))
    print(Order(joe, cart, best_promo))
    print("*"*10, "joe done", "*"*10)

    print(Order(ann, cart, fidelity))
    print(Order(ann, cart, bulk_item))
    print(Order(ann, cart, large_order))
    print(Order(ann, cart, best_promo))
    print("*"*10, "ann done", "*"*10)

    banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, best_promo))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, best_promo))