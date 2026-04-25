from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import random
import markdown2

def index(request):
    #print(util.list_entries())
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_entries(request,entry_name):
    print("entry_name is:", entry_name)
    entry_info = util.get_entry(entry_name)
    print(entry_info)
    if entry_info:
        return render(request, "encyclopedia/entrypage.html",{
            "name": entry_name,
            "content": markdown2.markdown(entry_info)
        })
    else:
        return HttpResponse(f"Hello, the page \"{entry_name}\" is not available!")
    
def search(request):
    if request.method == "POST":
        entry_list = util.list_entries()
        entry_list_upper = list(map(lambda x: x.upper(),entry_list))
        #print(entry_list_upper)
        form = request.POST['q'].upper()
        #print("form is:",type(form))
        if form != "" and form in entry_list_upper:
            # return HttpResponseRedirect(f"/wiki/{form}")
            return HttpResponseRedirect(reverse("encyclopedia:show_entries", kwargs={"entry_name":form}))
        # https://stackoverflow.com/questions/58387545/django-reverse-dynamic-urls-with-multiple-arguments-using-django-views
        elif form == "":
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            new_form = []
            for i in range(len(entry_list_upper)):
                if form in entry_list_upper[i]:
                    new_form.append(entry_list[i])
            if new_form == []:
                return HttpResponse(f"Hey, cant find it")
            else:
                return render(request, "encyclopedia/search_result.html",{
                    "query":request.POST['q'],
                    "result":new_form
                })

    else:
        return HttpResponse(f"This is the search engine! However you should not type the url manually")
    
def new(request):
    if request.method == "POST":
        #print("I got this!")
        form = request.POST
        title = form.get("title")
        content = form.get("content")
        if title not in util.list_entries():
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:show_entries", kwargs={"entry_name":title}))
        else:
            return HttpResponse(f"No overwrite entry!")
    else:
        print("this is form")
        return render(request, "encyclopedia/new.html", {
            "entries": util.list_entries()
        })
    
def edit(request):
    if request.method == "POST":
        form = request.POST
        print("title is:",form.get("title"))
        print("content is:",form.get("content"))
        title = form.get("title")
        content = form.get("content")
        page = form.get("page")
        if page=="entry":
            return render(request, "encyclopedia/edit.html", {
                "title":title,
                "content":content
            })
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:show_entries", kwargs={"entry_name":title}))
    else:
        print("this is edit")
        return HttpResponse("edit in progress")
    
def rand(request):
    entry_list = util.list_entries()
    random_select = random.choice(entry_list)
    return HttpResponseRedirect(reverse("encyclopedia:show_entries", kwargs={"entry_name":random_select}))
    #return HttpResponse("random page in progress")