iterations = int(input())
students = [[input(), float(input())] for _ in range(iterations)]


scores = set()
for student in students:
    name = student[0]
    score = student[1]
    scores.add(score)

sorted_scores = sorted(scores)
second_lowest = sorted_scores[1]

names = []
for name, score in sorted(students):
    if score == second_lowest:
        names.append(name)

print("\n".join(names))


