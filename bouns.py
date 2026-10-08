weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print (f"your bmi is {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi < 25:
    print ("You are healthy.")
else:
    print ("You are overweight, you need to work out more and watch your diet")