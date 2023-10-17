#using Python we will ask it to perform operations
def perform_operations():
    float_1 = 4.20 #float_1 is our first floating number
    float_2 = 1.9276 #float_2 is our second floating number
    sum_result = float_1 + float_2 #adds specified floating numbers

    print(f"Sum:",sum_result, f"Data Type:", type(sum_result))

    int_1 = 17 #int_1 is our first integer
    int_2 = 5 #int_2 is our second integer
    dif_result = int_1 - int_2 #subtracts specified integers

    print(f"Difference:", dif_result, f"Data Type:",type(dif_result))

    float_3 = 3.065 #float_3 is our third floating number
    int_3 = 2.0 #int_3 is our third integer
    pro_result = float_3 * int_3 #multiplys specified float number and integer together

    print(f"Product:", pro_result, f"Data Type:", type(pro_result)) 
    
def main():
     perform_operations

if __name__=="__main__":
       main()


