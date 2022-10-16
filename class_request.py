class Request:
    """доставка потребителю"""
    #'Доставить 3 печеньки из склад в магазин'
    def __init__(self, task: str):
        self.task = task
        k = self.task.split(' ')
        self.frm = k[4]
        self.to = k[-1]
        self.amount = int(k[1])
        self.product = k[2]

    def result(cls):
        s = cls.__dict__
        res = [s['product'], s['amount']]
        return res


class Capitalize:
    """доставка на склад"""
    #Курьер забирает 3 печеньки из склад
    def __init__(self, task: str):
        self.task = task
        k = self.task.split(' ')
        self.to = k[-1]
        self.product = k[3]
        self.amount = int(k[2])


    def result(cls):
        s = cls.__dict__
        res = [s['product'], s['amount']]
        return res

# re = 'Курьер забирает 3 печеньки из склад'
#
# s = Capitalize(re)
# print(s.result())

