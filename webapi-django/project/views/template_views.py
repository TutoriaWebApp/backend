from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from project.models import Usuario
from project.forms import UsuarioCreateForm, UsuarioUpdateForm

class AdminDashboardMixin(LoginRequiredMixin, UserPassesTestMixin):
    """ Mixin para garantir que apenas admins (staff) acessem a view """
    def test_func(self):
        return self.request.user.is_staff

class UsuarioListView(AdminDashboardMixin, ListView):
    model = Usuario
    template_name = 'project/usuario_list.html' # Crie este template
    context_object_name = 'usuarios'

class UsuarioCreateView(AdminDashboardMixin, CreateView):
	model = Usuario
	form_class = UsuarioCreateForm
	template_name = 'project/usuario_form.html'
	success_url = reverse_lazy('dashboard:usuario_list')
