English = int(input("obtained marks in English"))
Sindhi = int(input("obtaind marks in Sindhi"))
Chemistry = int(input("obtained marks in Chemistry"))
Pakistan_Studies = int(input("obtained marks in Pakisan_Studies"))
Computer = int(input("obtained marks in Computer"))
obtained_marks = English + Sindhi + Chemistry + Pakistan_Studies + Computer
print(obtained_marks)
total_marks = int(input("enter total marks"))
percentage = (obtained_marks/total_marks)*100
print(percentage)
if percentage >= 80 :
    print("Grade A+")
elif percentage >= 70 :
    print("Grade A") 
elif percentage >= 60 :
    print("Grade B")
elif percentage >= 50 :
    print("Grade C")
else : 
    print("Fail")                