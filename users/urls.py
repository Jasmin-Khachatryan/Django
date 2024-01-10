from django.urls import path

from users.views import UserCreationView, UserLoginView, UserLogoutView, UserProfileView, UserUpdateView

urlpatterns = [
    path("register/", UserCreationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("edit-profile/<int:pk>/", UserUpdateView.as_view(), name="edit_profile"),
]


