from rest_framework import permissions
from rest_framework.views import Request, View 
from movies.models import Movie

class IsMovieUser(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, movie: Movie) -> bool:

        return movie.user == request.user

