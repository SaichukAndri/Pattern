class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ChildActivityCommand(Command):
    def __init__(self, activity, child):
        self._activity = activity
        self._child = child

    def execute(self):
        return f"Дитина {self._child.name} виконує {self._activity}"

class ActivityInvoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_all(self):
        results = []
        for command in self._commands:
            results.append(command.execute())
        return results