
# Django Project Documentation

## Install
First lets see how to install Django 

```
pip install django
django-admin startproject projectname
```

Run python server and start an app
```
python manage.py runserver
python manage.py startapp products
```

## View

Now we will go to view and will add a function to show something to our users
**view.py** will define the functions here what the users will view

```
def index(request):
    return HttpResponse("You are on product page")
```
Here the index function will show the user what is saved here

## Urls
Now to redirect the user to the view, we have to map url.
**urls.py** will map url here to redirect to another page.
First we have to create urls.py for our new app
in the urls.py of the main project, we will redirect any specific url to its app
```
path('products/', include('products.urls')),
```
Here if 127.0.0.1/products is searched, it will be redirected to products.urls
now in products.urls we will redirect it to the view:

```
path('', views.index),
```
that means it will show the user what is instructed in views.index


## Models
 We create our classes here like Product Class

```
 class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
```
## Settings

After that we have to go to the settings.py and add out new installed app path there
```
products.apps.ProductsConfig
```

## Migrate

We will execute the models in database using these commands
```
python manage.py makemigrations
python manage.py migrate
```

## Admin
First make a superuser from terminal giving username, email and password
```
python manage.py createsuperuser
```
Now the admin can access the database logging in *127.0.0.1/admin*

No we can manage our created Product class using the following commands in admin.py:

we are going to register the models the admin is going to handle:
```
admin.site.register(Product)
```
Lets Modify the admin.py, we can configure what the admin will see in the database, 
so lets go to **admin.py**, and the code:
```
class ProductAdmin(admin.ModelsAdmin):
    list_display = ('name','price','stock')

admin.site.register(Product,ProductAdmin)
```

Here we are adding a product admin class where the list of display will be name , price and stock.
we are passing the ProductAdmin class with admin.site.register

Now we will show the database products in the index page,
got to the view page and import prduct there
```
from .models import Productcts
```
```
Product.objects.all() ---> will return all products,
Product.objects.filter() ---> can filter products
Product.objects.get() ---> will return any specific mentioned product
Product.objects.save() ---> insert a new product or update existing one
```

## Templates

We can use different templates, for that we need to open a directory inside our app directorny
name **templates** and add create our desired file there. For exaple I created a index.html file
where I added 
```
<h1>Products</h1>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>

</ul>
```
Now lets go to the view and redirect index page to this html page

```
def index(request):
    Product.objects.all()
    return render(request,'index.html')

```