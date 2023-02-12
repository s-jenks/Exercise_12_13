import random
# This is calling the module that we need and the functions that come under this module

# lotto = []
# count= 6
# for i in range (count):
#     lotto.append(random.randint(1,50))
#     print(lotto)

lotto = random.sample(range(1,50),6) # range allows us to specify the numbers and the 6 is the amount of itens in the list
print(lotto)
print(type(lotto)) # The list is the best way to store it as a list is mutabe which means it can be changed

