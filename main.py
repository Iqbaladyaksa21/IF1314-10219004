class hero :
  def __init__(self, inputName, inputHealth, inputPower, inputArmor, ):
      self.name = inputName
      self.health = inputHealth
      self.power = inputPower
      self.armor = inputArmor  

  def __del__ (self):
    class_name =self.__class__.___name__
    print("Sebuah Objek", class_name,", yaitu", self.name, "dihapus")

# instansiasi
hero1 = hero("sniper",150,170,30)
hero2 = hero("lancelot", 250, 200, 10)
hero3 = hero("tiny", 500, 50, 145)

print (hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

del hero1