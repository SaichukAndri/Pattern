from typing import List

class OrganizationComponent(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_total_salary(self):
        pass

class LeafEmployee(OrganizationComponent):
    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = salary

    def get_name(self):
        return self._name

    def get_total_salary(self):
        return self._salary

class Department(OrganizationComponent):
    def __init__(self, name: str):
        self._name = name
        self._employees: List[OrganizationComponent] = []

    def get_name(self):
        return self._name

    def add_employee(self, employee: OrganizationComponent):
        self._employees.append(employee)

    def get_total_salary(self):
        return sum(employee.get_total_salary() for employee in self._employees)