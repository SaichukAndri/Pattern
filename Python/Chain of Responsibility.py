class BaseHandler:
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def handle_request(self, request):
        if self._next_handler:
            return self._next_handler.handle_request(request)
        return None

class ParentPermissionHandler(BaseHandler):
    def handle_request(self, request):
        if request.get('parent_permission'):
            return True
        return super().handle_request(request)

class MedicalClearanceHandler(BaseHandler):
    def handle_request(self, request):
        if request.get('medical_clearance'):
            return True
        return super().handle_request(request)

class RegistrationHandler(BaseHandler):
    def handle_request(self, request):
        if request.get('is_registered'):
            return True
        return super().handle_request(request)

class ChildAdmissionProcess:
    def __init__(self):
        self._handlers = (
            ParentPermissionHandler(
                MedicalClearanceHandler(
                    RegistrationHandler()
                )
            )
        )

    def process_admission(self, request):
        return self._handlers.handle_request(request)