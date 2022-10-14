height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
int_height = float(height)
int_weight = float(weight)
bmi = int_weight / (int_height * int_height)
a = "underweight"
b = "normal weight"
c = "overweight"
d = "obese"
float(bmi)
print(bmi)
if(bmi<18.5):
  print("you aren " + a )
if(bmi>18.5 and bmi < 24.9):
    print("you are " + b)
if(bmi > 25 and bmi<29.9):
      print("you are " + c)
if(bmi > 30):
        print("you are " + d)
        
  
  