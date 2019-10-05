from django.shortcuts import render
from index.models import *
from index import forms as formlocal
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):
    shedule_form = formlocal.Shedule_Ride_Form()

    if request.method == 'POST':
        shedule_form = formlocal.Shedule_Ride_Form(request.POST)

        if shedule_form.is_valid():
            shedule_form.save(commit=True)
            subject, from_email, to = 'We Received Your Message - Techy Sight', 'shedule@techysight.com', request.POST.get('email')
            html_content = render_to_string("mail_template/shedule_client.html", {'name':request.POST.get('full_name').capitalize()})
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            for i in settings.ADMIN_EMAIL:
                # send message to ADMIN
                subject, from_email, to = 'sheduling Techy Sight', 'shedule@techysight.com', i
                html_content = render_to_string("mail_template/shedule_admin.html", {'name':request.POST.get('full_name').capitalize()})
                text_content = strip_tags(html_content)
                msg1 = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg1.attach_alternative(html_content, "text/html")
                msg1.send()
            return redirect('/')


    context = {
        'images': Upload_Image.objects.all(),
        'places': Amazing_Places.objects.all().order_by('-id'),
        'photos': Amazing_Photos.objects.all().order_by('-id'),
        'form': shedule_form,
    }
    return render(request,'index/index.html',context)



def search(request):

    query = request.GET.get('q')

    if query:
        photos_search = Amazing_Photos.objects.filter(
                            Q(title__icontains=query)
                            ).distinct()
        places_search = Amazing_Places.objects.filter(
                            Q(title__icontains=query)
                            ).distinct()
    else:
        return redirect('/')


    all_details = {
        'photos': photos_search,
        'places': places_search,
    }

    return render(request,'index/search.html',context=all_details)
