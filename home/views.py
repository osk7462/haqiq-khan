from django.shortcuts import redirect, render
from django.http import HttpResponse
from.models import OurWork, OurWorkPhoto, PriceList, SlideImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    slide_images = SlideImage.objects.all()
    return render(request, 'home/indexPage.html', {'slide_images': slide_images})

def price(request):
    price_list = PriceList.objects.all()
    print(price_list)
    context = {
        'title': 'price list',
        'price_list': price_list
    }
    return render(request, 'home/pricePage.html', context)

def our_work(request):
    our_works = OurWork.objects.all()
    context = {
        'title': 'our work',
        'our_works': our_works
    }
    return render(request, 'home/ourWorkPage.html', context)

def our_work_photo(request, pk):
    our_work = OurWork.objects.get(pk=pk)
    try:
        our_work_photos = OurWorkPhoto.objects.filter(our_work=our_work)
    except:
        our_work_photos = []
    context = {
        'title': 'our work',
        'our_works': our_work_photos
    }
    return render(request, 'home/ourWorkPhotoPage.html', context)

def login_user(request):
    message = ""
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['passWord'])
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            message = "username and password does not match" 
    return render(request, 'login.html', {'message': message})

@login_required
def addSlideImage(request):
    if request.method == 'POST':
        slide_image = SlideImage.objects.all()
        # for image in slide_image:
        #    if image.image:
        #        image.delete()
        slide_image.delete(True)
        for afile in request.FILES.getlist('slideImage'):
            slide_image = SlideImage(image=afile)
            slide_image.save()
        return redirect('homePage')
    return render(request, 'home/addSlideImage.html', {})
