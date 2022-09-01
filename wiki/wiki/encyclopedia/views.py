from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_enter(request,name):
    return render(request, "encyclopedia/get_entry.html",{
        "entry":util.get_entry(name),"title":name
        })


