
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm, CreateProjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View


# Create your views here.
from .models import Project


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
            return redirect('/home/')
  
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
class CreateProjectView(View):
    form = CreateProjectForm()
    template_name = 'new_project.html'

    def get_project(self, request, *args, **kwargs):
        project = Project.objects.all()
        context = {
            'project':project
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')

        return render(request, 'new_project.html', {'form': form})
