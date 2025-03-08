from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject
from .forms import SubjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.

GRADE_POINTS = {
    "A+": 4.00,
    "A": 3.75,
    "B+": 3.50,
    "B": 3.25,
    "C+": 3.00,
    "C": 2.75,
    "D+": 2.50,
    "D": 2.25,
    "F": 0.00,
}

@login_required(login_url="recipe:login")
def delet(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect("cgpa:index")

@login_required(login_url="recipe:login")
def edit_sub(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(instance=subject)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect("cgpa:index")
    else:
        form = SubjectForm(instance=subject)
    
    context = {
        "form": form,
        "subject": subject,
    }
    return render(request, "cgpa/edit.html", context)  

@login_required(login_url="recipe:login")
def index(request):
    subjects = Subject.objects.filter(user=request.user)
    form = SubjectForm()
    
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            
            return redirect("cgpa:index")
    
    #calculate cgpa
    total_credit = 0
    total_grade_point = 0
    cgpa = 0
    
    for subject in subjects:
        total_credit += subject.credit
        total_grade_point += GRADE_POINTS[subject.grade] * subject.credit
        
        if total_credit != 0:
            cgpa = total_grade_point / total_credit
            cgpa = '{0:.2f}'.format(cgpa)
        else:
            cgpa = 0.0
            
    context = {
        "subjects": subjects,
        "form": form,
        "cgpa": cgpa,
    }
    return render(request, "cgpa/index.html", context)



@login_required(login_url="recipe:login")
def result(request):
    subjects = Subject.objects.filter(user=request.user)
    form = SubjectForm()
    
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            
            return redirect("cgpa:index")
    
    #calculate cgpa
    total_credit = 0
    total_grade_point = 0
    
    for subject in subjects:
        total_credit += subject.credit
        total_grade_point += GRADE_POINTS[subject.grade] * subject.credit
        
        if total_credit != 0:
            cgpa = total_grade_point / total_credit
        else:
            cgpa = 0.0
            
    context = {
        "subjects": subjects,
        "form": form,
        "cgpa": cgpa,
    }
    return render(request, "cgpa/result.html")

