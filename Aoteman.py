from abc import ABCMeta,abstractmethod
from random import randint,randrange


class Fighter(object,metaclass = ABCMeta):
    """战斗者"""

    __slots__ = ('_name','_hp')

    def __init__(self, name,hp):

        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp>=0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self,other):
        """
        攻击

        : param other：被攻击的对象
        """

        pass

class Ultraman(Fighter):
    #奥特曼

    __slots__ = ('_name','_hp','_mp')

    def __init__(self,name,hp,mp):

        super().__init__(name, hp)

        self._mp = mp

    def attack(self,other):
        other.hp -= randint(15,25)

    def huge_attack(self,other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp*3//4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True

        else:
            self.attack(other)
            return False
