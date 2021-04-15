from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404

# Models
from .models import *
from main.models import *
from main.views import login__required

# Create your views here.


@login__required
def view__bookmarks(request):
    return render(request, 'main/view_bookmarks.html')

# @login__required


def add__bookmarks(request, donor_id):
    id = request.session['user_id']
    user_obj = User.objects.get(pk=id)
    donor_obj = Donor.objects.get(pk=donor_id)

    if not Bookmark.objects.filter(donor=donor_obj).first():
        bookmark = Bookmark.objects.create(donor=donor_obj)
        bookmark.save()
        print('bookmark created')
    else:
        bookmark = Bookmark.objects.filter(donor=donor_obj).first()
    bookmark.client.add(user_obj)
    bookmark.save()

    return redirect('/donors')


def remove__bookmarks(request, donor_id):

    id = request.session['user_id']
    user_obj = User.objects.get(pk=id)
    donor_obj = Donor.objects.get(pk=donor_id)

    if Bookmark.objects.filter(donor=donor_obj).first():
        bookmark = Bookmark.objects.filter(donor=donor_obj).first()
        bookmark.client.remove(user_obj)

        client = bookmark.client.all()

        if not client.exists():
            bookmark.delete()
    return redirect('/donors')
