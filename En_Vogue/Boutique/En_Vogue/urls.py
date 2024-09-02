from django.urls import path
from . import views

app_name = 'En_Vogue'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('galleryseemore/', views.galleryseemore, name='galleryseemore'),
    path('contacts/',views.contact_view, name='contact_view'),
    path('success/', views.success_view, name='success'),
    path('allProdCat/', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
    # path('bouquet/', views.bouquet, name='bouquet'),
]