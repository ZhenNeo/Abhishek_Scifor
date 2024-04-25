def bmi(w,h):
    return w/(h*h)

def record(filepath,w,h,date):
    BMI = bmi(w,h)

    with open(filepath,'a') as file:
        file.write(f"Date: {date}, Height: {h} m, Weight: {w} kg, BMI: {BMI:.2f}\n")


filepath = 'Scifor/BMI.txt'
w = float(input("Weight in kg: "))
h = float(input("Height in meters: "))
date = input("Enter the date: ")

record(filepath,w,h,date)
