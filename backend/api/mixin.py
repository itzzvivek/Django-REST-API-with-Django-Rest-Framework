from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    Permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]