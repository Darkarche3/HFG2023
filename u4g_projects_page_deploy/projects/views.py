from django.shortcuts import render, redirect

from .models import Project, Participant
from .forms import RegistrationForm, ProjectRequestForm, CollaborationForm, SignupForm
# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {
        'show_projects': True,
        'projects': projects
    })

def project_details(request, project_slug):
    try:
        selected_project = Project.objects.get(slug=project_slug)
        if request.method == "GET":
            
            registration_form = RegistrationForm()
            return render(request, 'projects/project-details.html', {
            'project_found': True,
            'project': selected_project,
            'form': registration_form,
        })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data["email"]
                user_name = registration_form.cleaned_data["name"]
                participant, _ = Participant.objects.get_or_create(email=user_email, name = user_name)
                selected_project.participants.add(participant)
                return redirect("confirm-registration", project_slug=project_slug)


    except Exception as exc:
        return render(request, "projects/project-details.html", {
            'project_found': False
        })

def confirm_registration(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    return render(request, "projects/registration-success.html", {
        'organizer_email': project.organizer_email
    })

def request_project(request):
    if request.method == "GET":
        request_form = ProjectRequestForm()
        return render(request, "projects/request-project.html",{
        'form': request_form,
        })
    else:
        request_form = ProjectRequestForm(request.POST)
        if request_form.is_valid():
            return redirect("projects/request-success.html")


def request_success(request):
    return render(request, "projects/request-success.html",{
    })

def company_profile(request):
    return render(request, "projects/ascezell.html",{
    })

def collaborations(request):
    if request.method == "GET":
        collaboration_form = CollaborationForm()
        return render(request, "projects/collaborations.html", 
                  {"participants": Participant.objects.all(),
                   "form": collaboration_form} )


def collabtable(request):
    if request.method == "POST":
        request_form = CollaborationForm(request.POST)
        if request_form.is_valid():
            members = list(request_form.data.getlist('members'))
            member_1 = Participant.objects.get(id = members[0])
            member_2 = Participant.objects.get(id = members[1])
            projects = Project.objects.all().order_by('id')


            shared = []
            for project in projects:
                participants = project.participants.all()
                if member_1 in participants and member_2 in participants:
                    shared.append(project)
            


            return render(request, "projects/collabtable.html", {
                "member_1": member_1,
                "member_2": member_2,
                "projects": shared,
            })

def contact(request):
    return render(request, 'projects/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = SignupForm()

    return render(request, 'projects/signup.html',{
        'form': form
    })
