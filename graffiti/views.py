import json

from django import http
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from graffiti.comments.models import Comment


def graffiti_index(request):
    return TemplateResponse(
        request,
        'graffiti_index.html'
    )


@csrf_exempt
def api(request):
    if not request.user and request.user.is_superuser:
        return http.HttpResponse(
            'YOU DONE FUCKED UP'
        )
    user, _created = User.objects.get_or_create(username=request.user.username)
    url = request.GET.get('url')

    if request.POST:
        data = request.POST
        url = data['url']
        Comment.objects.create(
            user=user,
            text=data['text'],
            url=url
        )

    if url:
        comments = [
            {
                'text': comment.text,
                'username': comment.user.username
            }
            for comment in Comment.objects.filter(url=url)
        ]
    else:
        comments = []

    return http.HttpResponse(
        json.dumps(comments)
    )