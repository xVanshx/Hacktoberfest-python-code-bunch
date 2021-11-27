
print("Welcome Sir/Mam to our cafe")
# all variables
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
name = input("\nYour Name Please?\n>")
items = ["Cappuccino", "Americano", "Espresso", "Latte", "cappuccino", "americano", "espresso", "latte"]
cap = 10
amer = 15
esp = 11
lat = 9
print("Okay! " + name + " here is our Menu")
print("1.Cappuccino - 10$")
print("2.Americano - 15$")
print("3.Espresso - 11$")
print("4.Latte - 9$")
# main
while(True):
  order = input("What you want to order " + name + "?\n>")
  if order in items[0]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*cap)
    break
  elif order in items[4]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*cap)
    break
  elif order in items[1]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*amer)
    break
  elif order in items[5]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*amer)
    break
  elif order in items[2]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*esp)
    break
  elif order in items[6]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*esp)
    break
  elif order in items[3]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*lat)
    break
  elif order in items[7]:
    quantity = input("How much you want to order?\nEnter no.\n>")
    print("Your Order " +  order + " will cost you $", int(quantity)*lat)
    break
  else:
    print("Wrong Input Enter Again\n")
