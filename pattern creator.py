print("enter 0 to create normal * pyramid and 1 to create inverted * pyramid")
choice=int(input("enter your choice"))
if choice==0:
    n = int(input("enter the no of rows"))
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

            # ending line after each row
        print("\r")
elif choice==1:

    n = int(input("enter the no of rows"))
    for i in range(n, 0, -1):
        print((n - i) * ' ' + i * '*')
else:
    print("invalid choice")