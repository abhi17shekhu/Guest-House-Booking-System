from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Pend
from .forms import PostForm,UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html', {})

    # Redirect to a success page.


def post_list(request):
    posts = Pend.objects.filter(booking_date__lte=timezone.now()).order_by('booking_date').filter(status = 'Pending')
    return render(request, 'blog/index.html', {'posts': posts})

def status_check(request):
    posts = Pend.objects.all()
    return render(request, 'blog/status.html', {'posts': posts})

def granted(request):
    confirmed = Pend.objects.filter(status='Granted')
    return render(request, 'blog/confirmed.html', {'confirmed': confirmed})

def arrived(request):
    posts = Pend.objects.filter(status='Arrived')
    return render(request, 'blog/conf_arrival.html', {'posts': posts})

def print_booking(request):
    posts = Pend.objects.filter(booking_date__lte=timezone.now()).latest('booking_date')
    return render(request, 'blog/print_booking.html', {'posts': posts})




def detail(request):
    details = Pend.objects.filter(booking_date__lte=timezone.now()).order_by('booking_date')
    return render(request, 'blog/details.html', {'details': details})

def post_edit(request):
    post = Pend()
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.print_booking')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/booking.html', {'form': form})