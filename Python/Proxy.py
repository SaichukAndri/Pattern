class ChildRecordsSystem:
    def __init__(self):
        self._records = {}

    def add_record(self, child: Child):
        self._records[child.name] = child

    def get_record(self, child_name: str):
        return self._records.get(child_name)

class ChildRecordsProxy:
    def __init__(self, system: ChildRecordsSystem, access_level: str):
        self._system = system
        self._access_level = access_level

    def get_record(self, child_name: str, requesting_user: str):
        if self._access_level == "admin":
            return self._system.get_record(child_name)
        elif self._access_level == "teacher" and requesting_user in ["Teacher", "Director"]:
            return self._system.get_record(child_name)
        elif self._access_level == "parent" and requesting_user == "Parent":
            return self._system.get_record(child_name)
        else:
            raise PermissionError("Немає дозволу на перегляд даних")