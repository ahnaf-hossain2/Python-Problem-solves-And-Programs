class Money:
    m = 300

    @classmethod
    def add_money(cls, change_money):
        cls.m = change_money # this will change the value of m

new_money = Money.add_money(500)
print(Money.m)
