def calculate_area(length, width):
    if length == width:
        print("This is a square!")
        return main()
    else:
        return length * width

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    result = calculate_area(length, width)
    
    print(result)

if __name__ == "__main__":
    main()
