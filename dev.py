class HR:
    def __init__(self, name, age, department, experience):
        self.name = name
        self.age = age
        self.department = department
        self.experience = experience

    def view(self):
        print("---- HR DETAILS ----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Experience:", self.experience)
        print()


class Manager:
    def __init__(self, name, team_size, project, experience):
        self.name = name
        self.team_size = team_size
        self.project = project
        self.experience = experience

    def view(self):
        print("---- MANAGER DETAILS ----")
        print("Name:", self.name)
        print("Team Size:", self.team_size)
        print("Project:", self.project)
        print("Experience:", self.experience)
        print()


class Employee:
    def __init__(self, name, emp_id, position, salary):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary

    def view(self):
        print("---- EMPLOYEE DETAILS ----")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Position:", self.position)
        print("Salary:", self.salary)
        print()


class Developer:
    def __init__(self, name, language, project, experience):
        self.name = name
        self.language = language
        self.project = project
        self.experience = experience

    def view(self):
        print("---- DEVELOPER DETAILS ----")
        print("Name:", self.name)
        print("Language:", self.language)
        print("Project:", self.project)
        print("Experience:", self.experience)
        print()


# Creating 4 details for each category
hr1 = HR("Kavita", 35, "Finance HR", "10 Years")
manager1 = Manager("Rohit", 12, "AI System", "8 Years")
employee1 = Employee("Aman", 101, "Sales Executive", "40,000")
developer1 = Developer("Neha", "Python", "Web App", "4 Years")

# Viewing details
hr1.view()
manager1.view()
employee1.view()
developer1.view()
