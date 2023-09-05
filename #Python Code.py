#Python Code
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        return [emp for emp in self.employees if emp.age == target_age]

    def search_by_name(self, target_name):
        return [emp for emp in self.employees if emp.name.lower() == target_name.lower()]

    def search_by_salary(self, operator, target_salary):
        if operator == ">":
            return [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == "<":
            return [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == ">=":
            return [emp for emp in self.employees if emp.salary >= target_salary]
        elif operator == "<=":
            return [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            return []

    def display_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary")
            for emp in results:
                print(f"{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

    def search_employee(self):
        print("Search by:")
        print("1. Age")
        print("2. Name")
        print("3. Salary (>, <, <=, >=)")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            age = int(input("Enter age to search: "))
            results = self.search_by_age(age)
        elif choice == 2:
            name = input("Enter name to search: ")
            results = self.search_by_name(name)
        elif choice == 3:
            operator = input("Enter operator (>, <, <=, >=): ")
            salary = int(input("Enter salary to search: "))
            results = self.search_by_salary(operator, salary)
        else:
            print("Invalid choice.")
            return

        self.display_results(results)


if __name__ == "__main__":
    emp_table = EmployeeTable()

    # Add employees to the table
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    emp_table.search_employee()
