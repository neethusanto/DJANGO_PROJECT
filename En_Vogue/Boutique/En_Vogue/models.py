from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator



class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('En_Vogue:products_by_category',args=[self.slug])

    def __str__(self):
            return '{}'.format(self.name)

class Product(models.Model):
        name = models.CharField(max_length=250, unique=True)
        slug = models.SlugField(max_length=250, unique=True)
        description = models.TextField(blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='product', blank=True)
        stock = models.IntegerField()
        available = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        def get_url(self):
            return reverse('En_Vogue:prodCatdetail',args=[self.category.slug,self.slug])

        class Meta:
            ordering = ('name',)
            verbose_name = 'product'
            verbose_name_plural = 'products'

        def __str__(self):
            return '{}'.format(self.name)
        

class Gallery(models.Model):
     img_name=models.CharField(max_length=250, unique=True)
     gallery_image = models.ImageField(upload_to='gallery', blank=True)


     def __str__(self):
         return '{}'.format(self.img_name)
     

class NewGallery(models.Model):
     new_img_name=models.CharField(max_length=250, unique=True)
     new_gallery_image = models.ImageField(upload_to='gallery', blank=True)


     def __str__(self):
         return '{}'.format(self.new_img_name)
     
# class NewContact(models.Model):     
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254)
#     phone_number = models.CharField(max_length=15)
#     message =models.TextField(blank=True)

#     def __str__(self):
#         return '{}'.format(self.name) 


# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone_regex = RegexValidator(
#         regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(
#         validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
#     message = models.TextField()

#     def __str__(self):
#         return self.name
      

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message =models.TextField(blank=True)
   
    
    def __str__(self):
        return self.email      
     



    
        
       