import json

from django import http
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from comments.models import Comment


def graffiti_index(request):
    return TemplateResponse(
        request,
        'graffiti_index.html'
    )

@csrf_exempt
def api(request):
    url = request.GET.get('url')

    if request.POST:
        data = request.POST

        name = data['username']
        user, _created = User.objects.get_or_create(username=name)
        Comment.objects.create(
            user=user,
            text=data['text'],
            url=data['url']
        )
        url = data['url']

    if url:
        comments = [
            {
                'text': c.text,
                'user': c.user.username,
            } for c in Comment.objects.filter(url=url)
        ]
        print comments
    else:
        comments = []

    return http.HttpResponse(
        json.dumps(comments)
    )