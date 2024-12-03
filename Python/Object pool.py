class ResourcePool:
    def __init__(self, initial_size=5):
        self._resources = []
        self._in_use = set()
        
        for _ in range(initial_size):
            self._resources.append(self.create_resource())

    def create_resource(self):
        # Наприклад, ігрові майданчики або навчальні матеріали
        return {
            "id": len(self._resources),
            "is_available": True
        }

    def acquire_resource(self):
        if self._resources:
            resource = self._resources.pop()
            self._in_use.add(resource)
            return resource
        
        # Якщо немає вільних ресурсів, створюємо новий
        new_resource = self.create_resource()
        self._in_use.add(new_resource)
        return new_resource

    def release_resource(self, resource):
        if resource in self._in_use:
            self._in_use.remove(resource)
            self._resources.append(resource)