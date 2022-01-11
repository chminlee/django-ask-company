from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request) : 
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q : 
        qs = qs.filter(message__icontains=q)
    return render(
        # render를 통해 django의 template를 이용해 손쉽게 만듦
        request, 
        # instagram/templates/instagram/post_list.html을 지정하는 것임
        'instagram/post_list.html' ,
        {
            'post_list' : qs,
        }
    )