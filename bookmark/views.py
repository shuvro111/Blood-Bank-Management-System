import os
from PIL import Image
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404

# Models
from .models import *
from main.models import *
from main.views import login__required
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


@login__required
def view__bookmarks(request):
    user = request.session['user_id']
    bookmarks = Bookmark.objects.filter(client=user)

    paginator = Paginator(bookmarks, 15)  # Show 15 contacts per page.
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_number = 1
        page_obj = paginator.page(page_number)

    pagination_info = {
        'total_items': paginator.count,
        'start_result': 1 + (15 * (int(page_number) - 1)),
        'end_result': (15 * int(page_number)) if paginator.count >= 15 and paginator.count > (15 * int(page_number)) else paginator.count,
        'page_number': page_number,
    }

    return render(request, 'main/view_bookmarks.html', {'page_obj': page_obj, 'pagination_info': pagination_info})
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
