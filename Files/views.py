from accounts.models import User
from django.shortcuts import redirect, render
from helpers.utils import _delete_file_

from Files.models import File, Folder, MainFolder

# Create your views here.

def mainFolder(request):
    return render(request, 'files/main.folder.html')

def subFolder(request, folder_id, user_id):
    context = {}
    if MainFolder.objects.filter(id = folder_id).exists():
        folder = MainFolder.objects.get(id = folder_id)  
    else:
        folder = Folder.objects.get(id = folder_id)
    context['user_id'] = str(request.user.id)
    context['owner_id'] = user_id
    context['folder'] = folder
    return render(request, 'files/subfolder.html', context)

def createFolderMain(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        folder = MainFolder.objects.create(name = name, user = request.user)
    return redirect('files:main')

def createSubFolder(request, id):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        folder = Folder.objects.create(name = name)
        if MainFolder.objects.filter(id = id).exists():
            user.main_folder.subfolders.add(folder)
        else:
            Folder.objects.get(id = id).subfolders.add(folder)
    return redirect('files:sub', folder.id,request.user.id)

def addFile(request, id):
    if MainFolder.objects.filter(id = id):
        folder = MainFolder.objects.get(id = id)
    else:
        folder = Folder.objects.get(id = id)
    if request.method == 'POST':
        print(request.FILES)
        file = request.FILES.get('file')
        f = File.objects.create(file = file, name='file')
        folder.items.add(f)
        # folder.save()
    return redirect('files:sub', id, request.user.id)

def deleteItemsSubs(folder):
    for item in folder.items.all():
        _delete_file_(item.file.path)
        item.delete()
    if folder.subfolders.count() > 0:
        for f in folder.subfolders.all():
            deleteItemsSubs(f)
    folder.delete()
    
def deleteFolderItem(request, id):
    if Folder.objects.filter(id = id).exists():
        folder = Folder.objects.get(id = id)
        deleteItemsSubs(folder)
    if File.objects.filter(id = id).exists():
        file = File.objects.get(id = id)
        file.delete()
