pan = input("Enter your PAN number: ")
if len(pan) < 10:
    print("Invalid PAN number")
else:
    print(pan.upper())