def main():
    try:
        number = float(input("Enter a number: "))
        if number == 0:
            print("The number is zero.")
        else:
            print("the number is not zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if __name__=="__main__":
    main()
