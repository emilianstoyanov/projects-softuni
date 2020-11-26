class BulgarianPerson:  # Class definition
    country = 'Bulgaria'  # Class-level attribute

    def __init__(self, name):  # class - level attribute & method
        self.name = name  # instance - level attribute (name е на ниво инстанция)

    def say_hi(self):
        pass


emo = BulgarianPerson('Emo')
print(emo.__dict__)  # {'name': 'Emo'}
print(emo.country)  # Bulgaria


