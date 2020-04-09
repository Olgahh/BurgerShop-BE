# from rest_framework.permissions import BasePermission

# class IsStaffOrUser(BasePermission):
# 	message = "You must be staff or user who added this item"

# 	def has_object_permission(self, request, view, obj):
# 		return request.user.is_staff or (obj.added_by == request.user)
	