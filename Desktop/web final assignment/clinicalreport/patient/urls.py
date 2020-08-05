from django.urls import path
from patient import views
urlpatterns = [
    path('patient', views.index),
    path('save', views.save),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]