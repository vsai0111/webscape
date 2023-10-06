from django.shortcuts import render
from .models import Bookmark

def index(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmarks/index.html', {'bookmarks': bookmarks})

def add_bookmark(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        category = request.POST.get('category')
        Bookmark.objects.create(title=title, url=url, category=category)
        return redirect('index')
    return render(request, 'bookmarks/add_bookmark.html')

def view_bookmarks(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmarks/view_bookmarks.html', {'bookmarks': bookmarks})
