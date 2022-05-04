from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import shorturl
import random
import string
from app_ml import GB_Classifier as gb
from app_ml.feature import generate_data_set
import numpy as np
import re
# Create your views here.


@login_required(login_url='/login/')
def dashboard(request):
    usr = request.user
    urls = shorturl.objects.filter(user=usr)
    return render(request, 'dashboard.html', {'urls': urls})

def history(request):
    usr = request.user
    urls = shorturl.objects.filter(user=usr)
    return render(request, 'history.html', {'urls': urls})


def randomgen():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


@login_required(login_url='/login/')
def generate(request):
    if request.method == "POST":
        pass
        if request.POST['original'] :
            # generate based on user input
            usr = request.user
            original = request.POST['original']
            print(original,"ss")
            x=np.array(generate_data_set(original))
            if len(x)!=30:
                for i in range(30-len(x)):
                    x_new=np.append(x,[-1])
                x_new1=x_new.reshape(1,30)
            else:
                x_new1=x.reshape(1,30)
            output,percentage=gb.input_data(x_new1)
            print(output)
            final_output = False
            if(output==1):
                final_output = True
            newurl = shorturl(
                user=usr,
                    original_url=original,
                    is_legitimate = final_output
                )
            newurl.save()
            if final_output==True:
                messages.success(request,"Hurray! The URL is {0:.2f} % safe to go.".format(percentage*100))
            else:
                messages.error(request,"Beware! This is a phishing URL.")
            return redirect(dashboard)
            # check = shorturl.objects.filter(short_query=short)
            # if not check:
                # newurl = shorturl(
                #     user=usr,
                #     original_url=original,
                #     short_query=short,
                #     is_legitimate = final_output
                # )
                # newurl.save()
                # return redirect(dashboard)
            # else:
            #     messages.error(request, "Already Exists")
            #     return redirect(dashboard)
        else:
            messages.error(request, "You cannot proceed without URL")
            return redirect(dashboard)
    else:
        return redirect('/url-checker')


def home(request, query=None):
    if not query or query is None:
        return render(request, 'home.html')
    else:
        try:
            check = shorturl.objects.get(short_query=query)
            check.visits = check.visits + 1
            check.save()
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'home.html', {'error': "error"})

# added delete URl


@login_required(login_url='/login/')
def deleteurl(request):
    if request.method == "POST":
        short = request.POST['delete']
        try:
            check = shorturl.objects.filter(original_url=short)
            check.delete()
            return redirect(history)
        except shorturl.DoesNotExist:
            return redirect(home)
    else:
        return redirect(home)
