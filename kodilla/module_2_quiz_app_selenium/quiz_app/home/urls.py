from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="Home-home"),
    path("about/", views.about, name="Home-about"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("instructor/", views.instructor, name="instructor"),
    path("create_quiz/", views.create_quiz, name="create_quiz"),
    path("display_questions/", views.display_questions, name="display_questions"),
    path("view_scores/", views.view_scores, name="view_scores"),
    path("student/", views.student, name="student"),
    path("start_quiz/", views.start_quiz, name="start_quiz"),
    path("user_scores/", views.user_scores, name="user_scores"),
]
