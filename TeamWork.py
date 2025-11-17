def get_score(prompt):
    score = float(input(prompt))
    while score < 0 or score > 100:
        print("Please enter a valid score between 0 and 100.")
        score = float(input(prompt))
    return score
test1 = get_score("Enter first test score: ")
test2 = get_score("Enter second test score: ")
test3 = get_score("Enter third test score: ")
homework1 = get_score("Enter first homework score: ")
homework2 = get_score("Enter second homework score: ")
homework3 = get_score("Enter third homework score: ")
participation = get_score("Enter participation score: ")
average_tests = (test1 + test2 + test3) / 3
average_homework = (homework1 + homework2 + homework3) / 3
average_participation = participation
final_score = (average_tests * 0.5) + (average_homework * 0.3) + (average_participation * 0.2)
print("Average test score:", average_tests)
print("Average homework score:", average_homework)
print("Participation score:", average_participation)
print("Final grade:", final_score)
if final_score >= 97:
    print("you have a A+")
elif final_score >= 93:
    print("you have a A")
elif final_score >= 90:
    print("you have a A-")
elif final_score >= 87:
    print("you have a B+")
elif final_score >= 83:
    print("you have a B")
elif final_score >= 80:
    print("you have a B-")
elif final_score >= 77:
    print(" you have a C+")
elif final_score >= 73:
    print("you have a C")
elif final_score >= 70:
    print("you have a C-")
elif final_score >= 67:
    print("you have D+")
elif final_score >= 63:
    print("you have a D")
elif final_score >= 60:
    print("you have a D-")
else:
    print("you have a F")