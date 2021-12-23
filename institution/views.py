from django.shortcuts import redirect, render
from .models import Institution
from django.contrib.auth.decorators import login_required
from Files.models import File
# Create your views here.

@login_required
def Institutions(request):
    institutions = Institution.objects.all()
    context = {
        'institutions': institutions
    }
    return render(request, 'institution/institutions.html', context)

@login_required
def InstitutionHome(request, id):
    institution = Institution.objects.get(id=id)
    context = {
        'institution': institution,
    }
    return render(request, 'institution/institution.html', context)

@login_required
def Programmes(request, id):
    institution = Institution.objects.get(id=id)
    context = {
        'programmes': institution.programmes.all(),
        'institution': institution
    }
    return render(request, 'institution/programmes.html', context)

@login_required
def Programme(request, iid, pid):
    institution = Institution.objects.get(id=iid)
    programme = institution.programmes.get(id=pid)
    context = {
        'programme': programme,
        'institution': institution
    }
    return render(request, 'institution/programme.html', context)

def Ebook(request, pid, fid):
    institution = Institution.objects.get(id=pid)
    file = File.objects.get(id=fid)
    context = {
        'file': file,
        'institution': institution
    }
    return render(request, 'institution/ebook.html', context)

def Subscribe(request, id):
    inst = Institution.objects.get(id=id)
    user = request.user
    user.subscribed.add(inst)
    return redirect('institution:institution', id)


def Unsubscribe(request, id):
    inst = Institution.objects.get(id=id)
    user = request.user
    user.subscribed.remove(inst)
    return redirect('institution:institutions')
