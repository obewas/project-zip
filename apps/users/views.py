
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm, CreateProjectForm, PhotoForm, GradeForm, Photo2Form, Photo3Form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Photo, Grading
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks

# Create your views here.


def dashboard(request):
	return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
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

# class ProjectCreateView(CreateView):
#     model = Project
#     template_name = 'project/create_project.html'
#     fields = '__all__'
#     success_url = reverse_lazy('project-list')
    

def create_project(request):
    
    context ={}
    form = CreateProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/project')
         
    context['form']= form
    return render(request, "project/create_project.html", context)


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

# class ProjectDeleteView(DeleteView):
#     model = Project
#     template_name = 'project/project-delete.html'
#     success_url = reverse_lazy('project')

def delete_project(request, pk):
    project = Project.objects.get(pk=pk).delete()
    return redirect('/project')



def upload(request):
    context = dict( backend_form = PhotoForm())
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

            return redirect('/profile/')
    return render(request, 'project/upload.html', context)

def upload_two(request):
    context = dict( backend_form = Photo2Form())

    if request.method == 'POST':
        form = Photo2Form(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
            return redirect('/create/')

    return render(request, 'project/upload2.html', context)

def upload_three(request):
    context = dict( backend_form = Photo3Form())

    if request.method == 'POST':
        form = Photo3Form(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

            return redirect('/create/')
    return render(request, 'project/upload3.html', context)



class SearchResultsView(ListView):
    model = Project
    template_name = 'project/project-search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Project.objects.filter(
            Q(title__icontains=query)
        )
        return object_list

@login_required(login_url='/accounts/login/')
def project_grading(request,id):
    user = Profile.objects.get(user= request.user)
    project = Project.objects.get(id=id)
    
    grades=Grading.objects.filter(project = project).last()
    #tech_tags = project.technologies.split(",")
 
    try:
        grades = Grading.objects.filter(user=user,project=project).first()
    except Grading.DoesNotExist:
        grades=None
        
    if grades is None:
        grades_status=False
    else:
        grades_status = True
   
    form = GradeForm()
    grading=None
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = user
            grade.project = project
            grade.save()
        try:
            grading = Grading.objects.filter(project_id=id)
        except Grading.DoesNotExist:
            grading=None
        design = form.cleaned_data['design']
        usability = form.cleaned_data['usability']
        content = form.cleaned_data['content']
        creativity = form.cleaned_data['creativity']
        grade.average = (design + usability + content + creativity)/4
        grade.save()
        
        design_gradings = [d.design for d in grading]
        design_average = sum(design_gradings) / len(design_gradings)
        usability_gradings = [us.usability for us in grading]
        usability_average = sum(usability_gradings) / len(usability_gradings)
        content_gradings = [content.content for content in grading]
        content_average = sum(content_gradings) / len(content_gradings)
        creativity_gradings = [cr.creativity for cr in grading]
        creativity_average = sum(creativity_gradings) / len(creativity_gradings)
        score = (design_average + usability_average + content_average + creativity_average) / 4
        grade.design_average = round(design_average, 2)
        grade.usability_average = round(usability_average, 2)
        grade.content_average = round(content_average, 2)
        grade.creativity_average = round(creativity_average, 2)
        grade.score = round(score, 2)
    
        grade.save()
        return redirect("project-list")
    else:
        form = GradeForm()
              
    context={
        "project":project,
        "grading":grading,
        "form":form,
        "grades_status":grades_status 
    }
    return render(request,"project/grading.html",context)




