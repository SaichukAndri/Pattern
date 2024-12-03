class BaseChildActivity:
    def perform_activity(self):
        return "Basic activity"

class ActivityDecorator(BaseChildActivity):
    def __init__(self, activity: BaseChildActivity):
        self._activity = activity

    def perform_activity(self):
        return self._activity.perform_activity()

class ArtActivityDecorator(ActivityDecorator):
    def perform_activity(self):
        base_activity = super().perform_activity()
        return f"{base_activity} + Art elements"

class MusicActivityDecorator(ActivityDecorator):
    def perform_activity(self):
        base_activity = super().perform_activity()
        return f"{base_activity} + Musical elements"