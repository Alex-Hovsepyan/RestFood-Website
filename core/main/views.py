from django.shortcuts import render, redirect
from .models import Header, Home, Title, About, AboutContent, Offer, Chef, Gallery, ReservationContent, OpenDays, Reservation
from .models import ContactContent, ContactInfo, Menu, Product
from .forms import ReservationModelForm

# Create your views here.

def index(request):
    header = Header.objects.first()
    home = Home.objects.first()
    titles = Title.objects.first()
    about = About.objects.first()
    about_content = AboutContent.objects.all()
    offer = Offer.objects.first()
    chefs = Chef.objects.all()
    gallery = Gallery.objects.all()
    reservation_content = ReservationContent.objects.first()
    open_days = OpenDays.objects.all()
    contact_content = ContactContent.objects.all()
    contact_info = ContactInfo.objects.first()
    menu = Menu.objects.all()
    products = Product.objects.all()

    if request.method == 'POST':
        form = ReservationModelForm(request.POST)
        if form.is_valid():
            Reservation.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = ReservationModelForm()

    return render(request, 'index.html', context={
        'header':header,
        'home':home,
        'titles':titles,
        'about':about,
        'about_content':about_content,
        'offer':offer,
        'chefs':chefs,
        'gallery':gallery,
        'reservation_content':reservation_content,
        'open_days':open_days,
        'contact_content':contact_content,
        'contact_info':contact_info,
        'menu':menu,
        'products':products,
    })