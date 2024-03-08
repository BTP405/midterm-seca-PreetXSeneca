"""This module defines a Course class for managing educational courses."""

class Course:
    """Represents a course offered by an educational institution.

    Attributes:
        course_name (str): The name of the course.
        instructor (str): The name of the instructor teaching the course.
        sections (int): The number of sections available for the course (default is 1).
        prerequisites (list): List of prerequisite courses for the course (default is None).
        enrolled_students (list): List of students enrolled in the course.
        waitlisted_students (list): List of students waitlisted for the course.
        assessments (list): List of assessments (e.g., exams, quizzes) for the course.
    """

    def __init__(self, course_name, instructor, sections=1, prerequisites=None):
        """Initialize a Course object.

        Args:
            course_name (str): The name of the course.
            instructor (str): The name of the instructor teaching the course.
            sections (int, optional): The number of sections available for the course (default is 1).
            prerequisites (list, optional): List of prerequisite courses for the course (default is None).
        """
        self.course_name = course_name
        self.instructor = instructor
        self.sections = 1
        self.prerequisite = prerequisite
        self.enrolled_students = []
        self.waitlisted_students = []
        self.assessments = []
        pass


    def add_student(self, student):
        """Enroll a student in the course or add them to the waitlist if all sections are full.

        Args:
            student (Student): The student object to be enrolled or added to the waitlist.
        """
        if len(enrolled_students) >= sections:
            self.waitlisted_students.append(student)
            return

        self.enrolled_students.append(student)
        pass


    def remove_student(self, student):
        """Remove a student from the course or the waitlist.

        Args:
            student (Student): The student object to be removed from the course or waitlist.
        """
        if stu in enrolled_students:
            remaining_students = [std for std in self.enrolled_students if std.student_id != student.student_id]
            self.enrolled_students = remaining_students
            return

        if stu in waitlisted_students:
            remaining_students = [std for std in self.waitlisted_students if std.student_id != student.student_id]
            self.waitlisted_students = remaining_students
            return
        pass


    def add_instructor(self, instructor):
        """Assign an instructor to the course.

        Args:
            instructor (str): The name of the instructor to be assigned to the course.
        """
        self.instructor = instructor
        pass

    def add_assessment(self, assessment):
        """Add an assessment to the course.

        Args:
            assessment (str): The description of the assessment to be added.
        """
        self.assessments.append(assessment)
        pass

