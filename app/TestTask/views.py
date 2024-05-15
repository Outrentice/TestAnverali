from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from TestTask.forms import ProfileEditForm
from TestTask.forms.CreateTaskForm import CreateTaskForm
from TestTask.forms.LoginForm import LoginForm
from TestTask.forms.RegisterForm import RegisterForm
from TestTask.models.Order import Order
from TestTask.models.User import User
from django.utils.translation import activate


class HomePage(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'TestTask/index.html'
    context_object_name = 'query'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Freelance'

        return context

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.role == 'Фрилансер':
            return Order.objects.filter(executor=None).select_related()
        elif self.request.user.is_authenticated and self.request.user.role == "Заказчик":
            return User.objects.filter(role='Фрилансер')
        else:
            return []


class ProfilePage(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'TestTask/profile.html'
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'

        context['orders'] = (Order.objects.filter(customer=self.get_object()).order_by('executor').select_related() or
                             Order.objects.filter(executor=self.get_object()).select_related())

        if self.request.user.role == 'Заказчик' and self.get_object().role == 'Фрилансер':
            context['give_orders'] = Order.objects.filter(customer=self.request.user, executor=None)

        return context

    def get_object(self, *args, **kwargs):
        if self.kwargs.get('slug'):
            return self.model.objects.get(username=self.kwargs.get('slug'))
        return self.request.user


class LoginPage(LoginView):
    template_name = 'TestTask/login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        activate('ru')

        return context

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('index')


class RegisterPage(CreateView):
    template_name = 'TestTask/register.html'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        activate('ru')

        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class ProfileEditPage(UpdateView):
    template_name = 'TestTask/profile_edit.html'
    form_class = ProfileEditForm.ProfileEditForm
    extra_context = {'title': 'Edit Profile'}

    def get_object(self, *args, **kwargs):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('profile')


class CreateTaskPage(CreateView):
    template_name = 'TestTask/create_task.html'
    form_class = CreateTaskForm

    def form_valid(self, form):
        if self.request.user.role == 'Заказчик':
            order = form.save(commit=False)
            order.customer = self.request.user
            order.save()
        return redirect('profile')


class TaskDetailPage(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'TestTask/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Task Detail'

        return context

    def get_object(self, *args, **kwargs):
        return Order.objects.get(id=self.kwargs.get('pk'))


def logout_user(request):
    logout(request)
    return redirect('index')


def take_task(request, pk, id_user=None):
    task = Order.objects.get(pk=pk)

    if (task.customer == request.user or not id_user) and task.executor is None:
        if id_user:
            task.executor = User.objects.get(pk=id_user)
        else:
            task.executor = request.user
        task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_task(request, pk):
    task = Order.objects.get(pk=pk)

    if request.user == task.customer:
        task.delete()
    elif request.user == task.executor:
        task.executor = None
        task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

