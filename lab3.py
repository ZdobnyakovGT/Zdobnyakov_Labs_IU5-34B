class Unit:
    def __init__(self, name, damage=150):
        self.name = name
        self.damage = damage


class Rassa:
    def __init__(self, rassa='человек'):
        self.rassa = rassa


class Archer(Unit, Rassa):
    def __init__(self, damage=10, name="безымянный", weapon="arch", rassa="elf"):

        Unit.__init__(self, name, damage)
        Rassa.__init__(self, rassa)
        self.damage_bonus = 5
        self.damage = damage + self.damage_bonus

        def attack(self):
            print("атака с уроном ", self.damage)

        def rass(self):
            print("Обладает рассой", rassa)


class Swordman(Unit):
    def __init__(self, damage=10, name="безымянный", weapon="sword"):
        Unit.__init__(self, name, damage)
        self.weapon = weapon
        self.damage_bonus = 10
        self.damage = damage + self.damage_bonus

    def attack(self):
        print("атака с уроном ", self.damage)


class Healer(Unit):
    def __init__(self, *args, **kwargs):
        super(Healer,self).__init__(*args)
        self.weapon = "staff"
        self.damage_bonus = -5
        # self.damage = damage + (-self.damage_bonus)


class OldHealer(Healer):
    def __init__(self, damage=10, name="безымянный", weapon="staff"):
        Healer.__init__(self, damage, name)
        self.damage = -damage
        self.damage_bonus = -5
        self.name = name
        self.damage = damage + (-self.damage_bonus)

    def MagicSuper(self):
        print("восстановление здоровья ", self.damage * 3)




ob1 = Swordman()
print(ob1.damage)
ob1.attack()
print(ob1.weapon, '\n')

ob2 = Healer("aaa")
print("====")
print(ob2.damage, '\n')


ob3 = OldHealer()
ob3.MagicSuper()
