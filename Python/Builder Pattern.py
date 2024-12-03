class ChildBuilder:
    def __init__(self):
        self._child = None

    def reset(self):
        self._child = Child(name="", age=0, group="", parents_contacts=[])

    def set_name(self, name: str):
        self._child.name = name
        return self

    def set_age(self, age: int):
        self._child.age = age
        return self

    def set_group(self, group: str):
        self._child.group = group
        return self

    def add_parent_contact(self, contact: str):
        self._child.parents_contacts.append(contact)
        return self

    def set_medical_records(self, records: dict):
        self._child.medical_records = records
        return self

    def build(self):
        return self._child

class ChildDirector:
    def __init__(self, builder: ChildBuilder):
        self._builder = builder

    def create_full_profile(self, name: str, age: int, group: str, parents: List[str]):
        return (self._builder
                .reset()
                .set_name(name)
                .set_age(age)
                .set_group(group)
                .set_medical_records({"vaccinations": [], "allergies": []}))