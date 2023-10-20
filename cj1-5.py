import numpy as np

def main():
    x = np.linspace(0.0, 2*np.pi, num=1000) #creates an evenly spaced sequence
    sinx = np.sin(x)                        #in a specified interval

    print(f"      x | sin(x)")    #formats a makeshift table
    print(f"-----------------")

    for i in range(1000):
        print(f"{x[i]:.5f} | {sinx[i]:.5f}")


if __name__ =="__main__":
    main()