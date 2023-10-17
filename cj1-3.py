#defines a function that returns a value
def f(x):
    return x**3 + 8 #return the function

#calls f(x) with x = 9 then prints a statement depending if it the following result is true
def main():
    x = 9
    result = f(x)
    print(f"f({x}) = {result}")

    if result > 27:    #if the result of f(x)= x**3 + 8 is greater than 27
        print("YAY!")  #then it will print the following statement

if __name__ == "__main__":
    main()