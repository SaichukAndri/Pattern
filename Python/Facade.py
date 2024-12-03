class ChildRegistrationSystem:
    def __init__(self):
        self.registry = KindergartenRegistry()
        self.medical_records = {}
        self.group_assignment = GroupAssignmentSystem()

    def register_new_child(self, child: Child):
        # Комплексна реєстрація дитини
        self.registry.register_child(child)
        self.medical_records[child.name] = child.medical_records
        assigned_group = self.group_assignment.assign_group(child)
        child.group = assigned_group.name
        return child

class GroupAssignmentSystem:
    def assign_group(self, child: Child):
        if 2 <= child.age < 4:
            return YoungGroup()
        elif 4 <= child.age < 5:
            return MiddleGroup()
        else:
            return PreschoolGroup()