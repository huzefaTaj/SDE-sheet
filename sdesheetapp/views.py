from django.shortcuts import render, redirect
from .models import Sdeproblems, Category
from django.urls import reverse


# Create your views here.


def index(request):
    sde_problems = Sdeproblems.objects.all()
    return render(request, "index.html", {'sde_problems': sde_problems})


def postdata(request):
    if request.method == 'POST':
        name = request.POST['name']
        link = request.POST['link']
        difficulty = request.POST['difficulty']
        category_id = request.POST['category']
        notes = request.POST['notes']

        category = Category.objects.get(id=category_id)

        sde_problem = Sdeproblems.objects.create(
            name=name,
            link=link,
            difficulty=difficulty,
            category=category,
            notes=notes
        )
        sde_problem.save()
        return redirect(postdata)
    category = Category.objects.all()
    return render(request, "post.html", {'category': category})


def view_notes(request, sde_problem_id):
    if request.method == 'POST':
        notes = request.POST['nt']
        sde_problem = Sdeproblems.objects.get(id=sde_problem_id)
        sde_problem.notes = notes
        sde_problem.save()
        return redirect(reverse(view_notes, args=[sde_problem_id]))
    sde_problem = Sdeproblems.objects.get(id=sde_problem_id)
    print(sde_problem.name)
    return render(request, 'notes.html', {'sde_problem': sde_problem})
