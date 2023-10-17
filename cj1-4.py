#define a class with a data of characteristics
#for my favorite animal
import sys #import sys to access system-specific parameters

class FavoriteAnimal:
    #a class for physical parameters of the animal

    def print(self):
        print("Here is my favorite animal!")
        print(f"Length of arms = {self.arm_length}")
        print(f"Length of legs = {self.leg_length}")
        print(f"Number of eyes = {self.eye_count}")
        print(f"Does it have a tail? : {'Yes!' if self.has_tail else 'No'}") #instead of printing "True"
        print(f"Does it have fur? : {'Yes!' if self.has_fur else 'No'}")     # I made it to print "Yes!"
        print("\n(Hint: Commonly reffered to as a wiener dog)")

    def __init__(self, alength=6.5, llength=8.5, ecount=2, tproof=True, fproof=True):
        self.arm_length = f' {alength}" '
        self.leg_length = f' {llength}" '
        self.eye_count = ecount
        self.has_tail = tproof
        self.has_fur = fproof
    
def main():

    alength = 6.5
    llength = 8.5
    ecount = 2
    tproof = True
    fproof = True

    if(len(sys.argv)>=5):
        alength = float(sys.argv[1])

    if(len(sys.argv)>=5):
        llength = float(sys.argv[2])

    if(len(sys.argv)>=5):
        ecount = int(sys.argv[3])

    if(len(sys.argv)>=5):
        tproof = bool(sys.argv[4])

    if(len(sys.argv)>=5):
        fproof = bool(sys.argv[5])

    my_favorite_animal = FavoriteAnimal(alength=alength, llength=llength, ecount=ecount, tproof=tproof, fproof=fproof)


    my_favorite_animal.print()

if __name__=="__main__":
    main() 