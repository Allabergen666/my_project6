from django.shortcuts import redirect, render
from .models import Contact

# Create your views here.

# views.py отвечает  на отправление и получение запроса с сайта

def index(request):
    all_data = Contact.objects.all()

    # render обновление сайта
    return render(request,  'home/index.html', {"context": all_data})

def add_index(request):
    if request.method == "POST":
        if "post_img" in request.FILES:
        # photo, video and other обяьзательно забирать вот так
            post_img = request.FILES["post_img"]
            post_firstname = request.POST.get('post_firstname')
            post_lastname = request.POST.get('post_lastname')
            post_phone = request.POST.get('post_phone')
            post_email = request.POST.get('post_email')

            add = Contact(image=post_img,
                          firstname=post_firstname,
                          lastname=post_lastname,
                          phone=post_phone,
                          email=post_email)
            add.save()
            return redirect("/")

        
    return render(request, "blog/index.html")




