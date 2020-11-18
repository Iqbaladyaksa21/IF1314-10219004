class hero :
   jumlah = 0
   def __init__(self, inputName, inputHealth, inputPower, inputArmor, ):
      self.name = inputName
      self.health = inputHealth
      self.power = inputPower
      self.armor = inputArmor  
      hero.jumlah += 1
      print("membuat hero dengan nama " + inputName)

   def __del__ (self):
      class_name = self.__class__.__name__
      print("Sebuah Objek", class_name,", yaitu", self.name, "dihapus")

# instansiasi
hero1 = hero("sniper",150,170,30)
print("jumlah hero: ", hero.jumlah)
hero2 = hero("lancelot", 250, 200, 10)
print("jumlah hero: ", hero.jumlah)
hero3 = hero("tiny", 500, 50, 145)
print("jumlah hero: ", hero.jumlah)

print (hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

del hero2
