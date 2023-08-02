#import datetime module fo now()
import datetime

print("------school grading system--------\n")
#prompt user
name = str(input(("\nEnter student name: ")))
cat1 = float(input("Enter cat1 marks: "))
cat2 = float(input("Enter cat2 marks: "))
cat3 = float(input("Enter cat3 marks: "))
final_examination = float(input("Enter final examination marks: "))

#compute the sum and average
#cats adds upto 60% while final examination adds upto 40%
#both contributing to 100%
results = (((cat1+cat2+cat3)/90)*60) + (((final_examination)/100) * 40)

#round results to 2 d.p
sum = round(results, 2)

#print the student marks
print("\n")
print(f"Student Name: {name.upper()}\n")
print(f"Average: {sum}")

#conditional statements to grade sum
if(sum > 0 and sum <= 30):
    print("grade D")
elif(sum > 30 and sum <= 60 ):
    print("grade C")
elif(sum > 50 and sum <= 70):
    print("grade B")
elif(sum > 70 and sum <= 100):
    print("grade A")
else:
    print("Invalid Entry")

#Invalid Entry- marks cannot be greater than 100%

#getting current datetime
current_time = datetime.datetime.now()
print(f"{current_time} \n")