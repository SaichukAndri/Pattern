from abc import ABC, abstractmethod

class GroupFactory(ABC):
    @abstractmethod
    def create_group(self):
        pass

class YoungGroupFactory(GroupFactory):
    def create_group(self):
        return YoungGroup()

class MiddleGroupFactory(GroupFactory):
    def create_group(self):
        return MiddleGroup()

class PreschoolGroupFactory(GroupFactory):
    def create_group(self):
        return PreschoolGroup()

class Group:
    def __init__(self):
        self.children = []

    def add_child(self, child: Child):
        self.children.append(child)

class YoungGroup(Group):
    def __init__(self):
        super().__init__()
        self.age_range = (2, 3)

class MiddleGroup(Group):
    def __init__(self):
        super().__init__()
        self.age_range = (4, 5)

class PreschoolGroup(Group):
    def __init__(self):
        super().__init__()
        self.age_range = (5, 6)