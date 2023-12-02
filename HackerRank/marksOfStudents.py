def gradingStudents(grades):
    # Write your code here
    l = len(grades)

    for i in range(0, l):

        if grades[i] <= 37:
            print(grades[i])
            continue
        if grades[i]>38:
            if grades[i] % 5 == 0:
                print(grades[i])
                continue
            if grades[i] % 5 != 0:
                if (grades[i] + 1) % 5 == 0:
                    print(grades[i] + 1)
                    continue

                if (grades[i] + 2) % 5 == 0:
                    print(grades[i] + 2)
                    continue
                else:
                    print(grades[i])
                    continue









grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input())
    grades.append(grades_item)

gradingStudents(grades)




