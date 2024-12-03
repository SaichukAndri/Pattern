from enum import Enum, auto

class EmployeeType(Enum):
    TEACHER = auto()
    ASSISTANT = auto()
    COOK = auto()
    MEDICAL_STAFF = auto()

class EmployeeFactory:
    @staticmethod
    def create_employee(employee_type: EmployeeType, name: str, age: int):
        if employee_type == EmployeeType.TEACHER:
            return Teacher(name, age)
        elif employee_type == EmployeeType.ASSISTANT:
            return Assistant(name, age)
        elif employee_type == EmployeeType.COOK:
            return Cook(name, age)
        elif employee_type == EmployeeType.MEDICAL_STAFF:
            return MedicalStaff(name, age)

class Teacher(Employee):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, position="Вихователь", salary=25000, contact_info="")

class Assistant(Employee):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, position="Помічник вихователя", salary=18000, contact_info="")

class Cook(Employee):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, position="Кухар", salary=20000, contact_info="")

class MedicalStaff(Employee):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, position="Медсестра", salary=22000, contact_info="")