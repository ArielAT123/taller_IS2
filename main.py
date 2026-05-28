"""
Student Grade Management System module.
This module provides the Student class for managing student records and grades.
"""

class Student:
    """A class to represent a student and manage their grades."""

    def __init__(self, student_id, name):
        """
        Initialize the student with an ID and name.
        Validates that they are not empty.
        """
        if not student_id or not str(student_id).strip():
            print("Error: Student ID cannot be empty.")
            self.student_id = "Unknown"
        else:
            self.student_id = str(student_id).strip()

        if not name or not str(name).strip():
            print("Error: Student name cannot be empty.")
            self.name = "Unknown"
        else:
            self.name = str(name).strip()

        self.grades = []

    def add_grade(self, grade):
        """Add a numeric grade between 0 and 100."""
        try:
            grade_value = float(grade)
            if 0 <= grade_value <= 100:
                self.grades.append(grade_value)
            else:
                print(f"Error: Grade {grade} must be between 0 and 100.")
        except (ValueError, TypeError):
            print(f"Error: Grade '{grade}' must be a numeric value.")

    def calculate_average(self):
        """Calculate and return the average of all grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Convert the average grade into a letter grade."""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def is_passed(self):
        """Determine if the student passed (average >= 60)."""
        return self.calculate_average() >= 60

    def is_honor_roll(self):
        """Determine if the student is on the honor roll (average >= 90)."""
        return self.calculate_average() >= 90

    def remove_grade_by_value(self, grade):
        """Remove a grade by its value."""
        try:
            self.grades.remove(grade)
            print(f"Success: Grade {grade} removed.")
        except ValueError:
            print(f"Error: Grade {grade} not found.")

    def remove_grade_by_index(self, index):
        """Remove a grade by its index."""
        try:
            removed = self.grades.pop(index)
            print(f"Success: Grade {removed} at index {index} removed.")
        except IndexError:
            print(f"Error: Index {index} is out of bounds.")
        except TypeError:
            print("Error: Index must be an integer.")

    def generate_summary_report(self):
        """Generate and print a formatted summary report for the student."""
        print("--- Student Summary Report ---")
        print(f"Student ID:     {self.student_id}")
        print(f"Student Name:   {self.name}")
        print(f"Grades Count:   {len(self.grades)}")
        print(f"Average Grade:  {self.calculate_average():.2f}")
        print(f"Letter Grade:   {self.get_letter_grade()}")

        pass_status = "Passed" if self.is_passed() else "Failed"
        print(f"Pass/Fail:      {pass_status}")

        honor_status = "Yes" if self.is_honor_roll() else "No"
        print(f"Honor Roll:     {honor_status}")
        print("------------------------------")


def main():
    """Main function to test the Student Grade Management System."""
    invalid_student = Student("", "  ")
    print(invalid_student)

    student = Student("S123", "John Doe")
    student.add_grade(100)
    student.add_grade(85.5)
    student.add_grade("Fifty")
    student.add_grade(150)
    student.add_grade(-10)

    student.remove_grade_by_value(100)
    student.remove_grade_by_value(999)

    student.add_grade(95)
    student.add_grade(92)

    student.remove_grade_by_index(5)
    student.remove_grade_by_index(0)

    print()
    student.generate_summary_report()


if __name__ == "__main__":
    main()
