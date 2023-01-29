class University:
    def __init__(self, student, teacher) -> None:
        self.student = student
        self.teacher = teacher


u = University("grad student", "PHD professor")
print(u.teacher)
print(u.student)