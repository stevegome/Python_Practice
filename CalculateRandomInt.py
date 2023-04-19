import random


class randDomno:
    def __init__(self, randomnoupto):
        self.randomnoupto = randomnoupto

    def generate_random_no(self):
        randomNumber = random.randint(1, self.randomnoupto)
        return randomNumber


number = int(input("Enter a no upto : "))
r1 = randDomno(number)
newNo = r1.generate_random_no()
print(f"Random no is {newNo}")
