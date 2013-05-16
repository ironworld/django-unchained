from models import Photo
from django.shortcuts import render_to_response


def photo_list(request):
    return render_to_response("photos_list.html", {'photo_list': Photo.objects.all()})
