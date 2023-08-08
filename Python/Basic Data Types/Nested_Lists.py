if __name__ == '__main__':
    # Create an empty list to store the names and grades of the students as sub-lists
    students = []
    # Read the names and grades of each student and store them as sub-lists in the 'students' list
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])
    
    # Sort the list of students based on their grades in ascending order
    students.sort(key=lambda x: x[1])

    # Find the second lowest grade in the list of students
    second_lowest_grade = None
    for student in students:
        if second_lowest_grade is None and student[1] != students[0][1]:
            second_lowest_grade = student[1]
            break

    # Find the names of the students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

    # Sort the names alphabetically and print each name on a new line
    for name in sorted(second_lowest_students):
        print(name)
