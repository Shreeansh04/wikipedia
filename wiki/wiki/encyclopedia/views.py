from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse

class addingp(forms.Form):
    """docstring for addingp"""
    title = forms.CharField(label = "Add title")
    content = forms.CharField(widget=forms.Textarea)
        

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_enter(request,name):
    return render(request, "encyclopedia/get_entry.html",{
        "entry":util.get_entry(name),"title":name
        })

def add_page(request):
    
    if request.method == "POST":
        form = addingp(request.POST)
        if form.is_valid():
           title = form.cleaned_data["title"]
           content = form.cleaned_data["content"]
           util.save_entry(title,content)
           return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"encyclopedia/add_page.html",{
        "form":form
        })


    return render(request,"encyclopedia/add_page.html",{
        "form":addingp()
        })