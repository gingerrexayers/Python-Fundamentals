scores = []
i = 0
while len(scores) < 10:
    i = input("input " + str(10 - len(scores)) + " scores between 60 and 100: ")
    if 59 < i < 101:
        scores.append(i)
        i = 0

for j in range(0, len(scores)):
    grade = ""
    if scores[j] < 70:
        grade = "D"
    elif scores[j] < 80:
        grade = "C"
    elif scores[j] < 90:
        grade = "B"
    else:
        grade = "A"
    print "Score: " + str(scores[j]) + "; Your grade is " + grade
