from django.urls import path

from . import views

app_name: "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/",views.add_page, name="add_page"),
    path("<str:name>/",views.get_enter, name="entry")
   ]
