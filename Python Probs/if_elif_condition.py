x = int(input("enter the mark to calculate grade"))
while True:
    if (x <00 or x>100):
        print(" Plzz....Enter your mark in range 0-100")
        break
    elif x >= 90:
        print("Perfomance :Excellent\n Grade: A")
        break
    elif x >= 80 and x <= 90:
        print("Perfomance :Average\nGrade: B")
        break
    else:
        print("Perfomance :Too Poor\nGrade : C")
        break
