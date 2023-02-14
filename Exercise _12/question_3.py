import random
# This is calling the module that we need and the functions that come under this module

# The below code creates 6 different lists with the final output being 6 items.

lotto = []
for i in range(0,6):
    lotto.append(random.randint(1,50))

print(lotto)

lotto_set = set()
while len(lotto_set) < 6:
    lotto_set.add(random.randint(1,50))

print(lotto_set)

# # The sample method seems to be more efficient
# lotto = random.sample(range(1,50),6) # range allows us to specify the numbers and the 6 is the amount of itens in the list
# print(lotto)
# print(type(lotto)) # The list is the best way to store it as a list is mutable which means it can be changed
