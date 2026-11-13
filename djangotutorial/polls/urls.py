from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("all/", views.AllQuestionsView.as_view(), name="all"),
    path("<int:pk>/frequency/", views.FrequencyView.as_view(), name="frequency"),
    path('statistics/', views.statistics, name='statistics'),
    path('add/', views.add, name='add'),
    path('confirm_add/', views.confirm_add, name='confirm_add'),
    path(
        "connexion/",
        auth_views.LoginView.as_view(
            template_name="polls/login.html",
            next_page="polls:index"
        ),
        name="login"
    ),
    path(
        "deconnexion/",
        auth_views.LogoutView.as_view(
            next_page="polls:index"
        ),
        name="logout"
    ),
]
