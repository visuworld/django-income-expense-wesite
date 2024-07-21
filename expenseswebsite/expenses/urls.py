from django.urls import path
from . import views  # Import your own views


urlpatterns = [
    path('', views.index, name="expenses"),
    path('add_expenses', views.add_expense, name="add_expenses"),
    #added by me
    path('_sidebar', views._sidebar, name="_sidebar")
]