#("exercise10")

def check_even_odd(number):
    if number % 2==0:#if number is divisible by 2 has 0 remainder, its even
        return f"{number} is even"
    else:
        return f"{number} is odd"
    
def main():
     number=int(input("Enter a number:\n"))#asks user for input
     result=check_even_odd(number)#passes the number to the function to get the output
     print(result)#prints the output
     
main()#calls the main function