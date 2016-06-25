from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> This is skills App </h1>")
def detail(request,person_id):
    return HttpResponse("<h2>details of the skill "+ str (person_id) + "</h2>")
