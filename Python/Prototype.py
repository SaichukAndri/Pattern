import copy

class PrototypeChild:
    def clone(self):
        return copy.deepcopy(self)

class MedicalRecordPrototype:
    def clone(self):
        return copy.deepcopy(self)

class ChildProfile(Child, PrototypeChild):
    def duplicate_with_modifications(self, **kwargs):
        new_child = self.clone()
        for key, value in kwargs.items():
            setattr(new_child, key, value)
        return new_child