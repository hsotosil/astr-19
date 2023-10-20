#define a class with a data of characteristics
#for my favorite animal
import sys #import sys to access system-specific parameters

class FavoriteAnimal:
    #a class for physical parameters of the animal

    def print_info(self):
        print("Here is my favorite animal!")
        print(f"Length of arms = {self.arm_length}", (float))
        print(f"Length of legs = {self.leg_length}", (float))
        print(f"It has {self.eye_count} eyes", type(self.eye_count))
        print(f"Does it have a tail? : {'Yes!' if self.has_tail else 'No'}", type(self.has_tail)) #instead of printing "True"
        print(f"Does it have fur? : {'Yes!' if self.has_fur else 'No'}", type(self.has_fur))     # I made it to print "Yes!"
        print("\nI am describing a Dachshund! Also known as a wiener dog!")

    def __init__(self, alength=6.5, llength=8.5, ecount=2, tproof=True, fproof=True):
        self.arm_length = f' {alength}" '
        self.leg_length = f' {llength}" '
        self.eye_count = ecount
        self.has_tail = tproof
        self.has_fur = fproof
    
def main():

    my_favorite_animal = FavoriteAnimal()
    my_favorite_animal.print_info()

if __name__=="__main__":
    main() 