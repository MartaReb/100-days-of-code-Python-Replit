class Job:
  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def pretty_print(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hours}\n")

class Doctor(Job):
  def __init__(self, salary, hours, speciality, experience): 
    self.name = "Doctor"
    self.salary = salary
    self.hours = hours
    self.speciality = speciality
    self.experience = experience

  def pretty_print(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hours}\nSpeciality: {self.speciality}\nYears of Experience: {self.experience}\n")

class Teacher(Job):
  def __init__(self, salary, hours, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position

  def pretty_print(self):
    print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.hours}\nSubject: {self.subject}\nPosition: {self.position}\n")

lawyer = Job("Lawyer", "$ 80,000", "60")
lawyer.pretty_print()

teacher_1 = Teacher("$ 50,000", "40", "Math", "Professor")
teacher_1.pretty_print()

doctor_1 = Doctor("$ 100,000", "50","Cardiologist", "10")
doctor_1.pretty_print()