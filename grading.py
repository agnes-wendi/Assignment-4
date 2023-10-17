maths = int(input("Enter marks awarded in Maths : "))
phyc = int(input("Enter marks awarded in Physics : "))
geog = int(input("Enter marks awarded in Geography : "))
chem = int(input("Enter marks awarded in Chemistry : "))


def avg_grade(maths, phyc, geog, chem):
    avg = (maths + phyc + geog + chem) / 4
    print(avg)

    if avg >= 0 and avg <= 30:
        print("D")
    elif avg > 30 and avg <= 50:
        print("C")
    elif avg > 50 and avg <= 70:
        print("B")
    elif avg > 70 and avg <= 100:
        print("A")
    else:
        print("Unrecognized marks/avg")
final_grade=avg_grade(maths, phyc, geog, chem)
print(f"Your average grade is {final_grade}")
