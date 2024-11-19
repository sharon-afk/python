user_input=input("Enter digits separated by space:")
digits=list(map(int,user_input.split()))
result=sum(digits)
print("The sum of the digits is:",result)
