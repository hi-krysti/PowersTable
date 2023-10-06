print("Learn your squares and cubes!\n")

num = int(input("Enter an integer: "))

print(f"\nNumber      Squared      Cubed")
print(f"======      =======      =====")

for n in range(1, num + 1):
    square = n ** 2
    cube = n ** 3
    print(f"{n}           {square}            {cube}")

cont = input("\nWould you like to continue? y/n: ")

while cont == "y":
    num = int(input("\nEnter an integer: "))
    print(f"\nNumber      Squared      Cubed")
    print(f"======      =======      =====")
    for n in range(1, num + 1):
        square = n ** 2
        cube = n ** 3
        print(f"{n}           {square}            {cube}")
    cont = input("\nWould you like to continue? y/n: ")
else:
    print("\nGoodbye!")
