# Question 4: University Examination Grading System
# Concepts: Inheritance, function overriding, super()
# Scenario: A university calculates grades differently for theory and practical
# examinations. A theory examination uses the marks directly, while a practical
# examination awards 5 bonus marks for successful lab completion, subject to a
# maximum of 100.
# Task: Create a parent class Examination with a calculate_marks() method.
# Override it in PracticalExam and use super().
# Sample input:
# Theory Marks: 80
# Practical Marks: 92
# Expected output:
# Theory Final Marks: 80
# Practical Final Marks: 97

class Examination:
    def __init__(self, marks):
        self.marks = marks

    def calculate_marks(self):
        return self.marks

class PracticalExam(Examination):
    def __init__(self, marks):
        super().__init__(marks)

    def calculate_marks(self):
        base_marks = super().calculate_marks()
        bonus_marks = 5
        total_marks = base_marks + bonus_marks
        return min(total_marks, 100)

theory_marks = int(input("Theory Marks: "))
practical_marks = int(input("Practical Marks: "))

theory_exam = Examination(theory_marks)
practical_exam = PracticalExam(practical_marks)

print("Theory Final Marks:", theory_exam.calculate_marks())
print("Practical Final Marks:", practical_exam.calculate_marks())
