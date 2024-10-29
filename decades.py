age = int(input("how old are you?"))

decades = age // 10
years = age % 100

print("you are " + str(decades) +
      " decades and "+str(years)+ " years old.")