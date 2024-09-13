number_1=float(input("Please Inter First Number = "))
operation=input("Please Enter Your Required Operation You Want To Perform (+,-,*,/) ")
number_2=float(input("Please Inter Second Number = "))
result=None
if operation=="+":
    result=number_1+number_2
elif operation=='-':
    result=number_1-number_2
elif operation=='*':
    result=number_1*number_2
elif operation=='/':
     if number_2 != 0:
         result=number_1/number_2
     else:
            print('Error: Divide By 0 Is Not Allowed')
            result=None
else:
    result = "Invalid Operation"

print(f"Your Result Is = {result}")