from django.urls import path    
from .views import task_one, create_task,delete,update, finalupdate
  
urlpatterns = [
    path('', task_one),
    path('new/',create_task, name = 'create_task'),
    path('delete/<int:iddb>/',delete, name="delete"),
    path('update/<int:iddb>', update,name = 'update'),
    path('finalupdate/<int:iddb>',finalupdate , name="finalupdate")
    
    
]