from django.urls import path

from TestTask import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('profile', views.ProfilePage.as_view(), name='profile'),
    path('task/<int:pk>', views.TaskDetailPage.as_view(), name='task_detail'),
    path('delete-task/<int:pk>', views.delete_task, name='delete_task'),
    path('take-task/<int:pk>', views.take_task, name='take_task'),
    path('take-task/<int:pk>/<int:id_user>', views.take_task, name='give_task'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
    path('profile/edit', views.ProfileEditPage.as_view(), name='profile_edit'),
    path('profile/create-task', views.CreateTaskPage.as_view(), name='create_task'),
    path('profile/<slug:slug>', views.ProfilePage.as_view(), name='profile_sl'),


]

