from django.urls import path
from . import views
urlpatterns = [
    # path('', views.show_tasks, name='show'),
    # path('', views.show_taksks_tv.as_view(), name='show'),
    path('', views.show_tasks_lv.as_view(), name='show'),
    # path('add/', views.add_task, name='add'),
    path('add/', views.add_task_fv.as_view(), name='add'),
    # path('add/', views.add_task_cv.as_view(), name='add'),
    path('completed/', views.completed_tasks, name='completed'),
    path('del/<int:id>', views.delete_task, name='del'),
    path('del/<int:pk>', views.delete_task_dv.as_view(), name='del'),
    # path('del/<int:id>', views.delete_task_tv.as_view(), name='del'),
    path('com/<int:id>', views.completed, name='com'),
    # path('edi/<int:id>', views.edit, name='edi'),
    path('edi/<int:pk>', views.edit_uv.as_view(), name='edi'),
]
