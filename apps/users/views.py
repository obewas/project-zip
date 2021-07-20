
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm, CreateProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
from .models import Project
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks
from .models import Photo
from .forms import PhotoForm

def dashboard(request):
	return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/')
  
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
  
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
  
    return render(request, 'users/profile.html', context)


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/profile_list.html', args)

#creating project views
class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'


    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        projects = self.get_queryset()

        context['projects'] = projects
        return context

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/create_project.html'
    fields = '__all__'
    success_url = reverse_lazy('/')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project-detail.html'
    context_object_name = 'project'

class ProjectUpdateView(UpdateView):

    model = Project
    template_name = 'project/project-update.html'
    context_object_name = 'project'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'pk': self.object.id})

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project-delete.html'
    success_url = reverse_lazy('project-list')




def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

        return redirect('/profile/')
  return render(request, 'project/upload.html', context)