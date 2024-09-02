
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product,Gallery,NewGallery,Contact
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# from.forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")



def services(request):
    return render(request, "services.html")

def gallery(request):
    obj=Gallery.objects.all()
    return render(request, "gallery.html",{'gallery_list':obj})

def galleryseemore(request):
    new=NewGallery.objects.all()
    return render(request, "gallery1.html",{'newgallery_list':new})

def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "categories.html", {'category': c_page, 'products': products})



def proDetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Product.DoesNotExist:
        raise  # Handle this exception appropriately in your code
    return render(request, 'product.html', {'product': product})

# def bouquet(request):
#     return render(request, "bouquet.html")
# def proDetail(request,c_slug,product_slug):
#     try:
#         product=Product.objects.get(category__slug=c_slug,slug=product_slug)
#     except Exception as e:
#         raise e
#     return render(request,'product.html',{'product':product})





# def contact_view(request):

#     if request.method == 'POST':
#         contact = NewContact()

#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         message = request.POST.get('message')

#         contact.name = name
#         contact.email = email
#         contact.phone_number = phone_number
#         contact.message = message

#         contact.save()
#         print('saveeeed')

#         return HttpResponseRedirect(reverse('thanks_contact'))
#     else:
#         print('method not post')

#     return render(request, "contact.html")


# def thanks_contact(request):

#     return render(request, "thanks_contact.html")

def contact_view(request):
  if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone_number=phone_number,message=message)
        contact.save()
        return redirect('En_Vogue:success')  # Ensure you have a success URL pattern
  return render(request, 'contact.html')


def success_view(request):
    return render(request, 'success.html')

