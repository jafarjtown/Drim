from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Post, SavePost,SavedPost, Comment as C
# Create your views here.


def Comment(request, id):
    if request.method == 'POST':
        import json
        try:

            text = request.POST['text']
            if text == '':
                return JsonResponse({'Error': 'comment is required'})
            c = C.objects.create(status=text, author=request.user)
            p = Post.objects.get(id=id)
            p.comments.add(c)
            c.save()
            p.save()

            # print(text)

            return JsonResponse({'response': 'success'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': e})
    return render(request, 'posts/comment.html', {'id': id})
def Edit(request, id):
    context = {}
    post = Post.objects.defer('author__followers', 'author__followings').get(id = id)  
    if request.method == 'POST':
        status = request.POST.get('status')
        delete = request.POST.get('delete')
        if delete:
            post.delete()
            return redirect('home:home')
        fileIds = request.POST.getlist('fileIds')
        for i in fileIds:
            post.files.get(id = i).delete()
        post.status = status
        post.save()
    context['post'] = post
    return render(request, 'post/edit.html', context)
def savePost(request, id):
    post = SavePost.objects.create(post = Post.objects.get(id = id))
    save = SavedPost.objects.get_or_create(user = request.user)[0]
    save.posts.add(post)
    return redirect('home:home')
def Like(request, id):
    user = request.user
    post = Post.objects.get(id = id)
    if user in post.likes.all():
        t = 'like'
        post.likes.remove(user)
    else:
        t = 'dislike'
        post.likes.add(user)
    post.save()
    return JsonResponse(
        {
            'status': 200,
            'type': t
        }
    )
    pass