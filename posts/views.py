from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Post, Comment as C
# Create your views here.


def Comment(request, id):
    if request.method == 'POST':
        import json
        # print(request.POST)
        # print(request.FILES)
        # json_loads = json.loads(request.body)
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