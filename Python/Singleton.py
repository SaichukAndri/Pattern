class KindergartenRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.children = []
            cls._instance.employees = []
        return cls._instance

    def register_child(self, child: Child):
        self.children.append(child)

    def register_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_total_children(self):
        return len(self.children)

    def get_total_employees(self):
        return len(self.employees)