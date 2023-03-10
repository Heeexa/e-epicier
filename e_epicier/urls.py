"""e_epicier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_views
from clients import views as client_views
from produits import views as produit_views
from credit import views as credit_views
urlpatterns = [
    path('', user_views.home,name ='home'),
    path('clients/', client_views.clientView,name ='client-view'),
    path('clients/add/', client_views.clientAdd,name ='client-add'),
    path('clients/edit/<int:id>/', client_views.clientEdit,name ='client-edit'),
    path('clients/remove/<int:id>/', client_views.clientDelete,name ='client-remove'),
    path('clients/<int:id>/', client_views.clientDetail,name ='client-detail'),

    path('produits/', produit_views.produitView,name ='produit-view'),
    path('produits/add/', produit_views.produitAdd,name ='produit-add'),
    path('produits/edit/<int:id>/', produit_views.produitEdit,name ='produit-edit'),
    path('produits/remove/<int:id>/', produit_views.produitDelete,name ='produit-remove'),
    path('produits/<int:id>/', produit_views.produitDetail,name ='produit-detail'),

    path('credits/add/', credit_views.creditAdd,name ='credit-add'),
    path('credits/edit/<int:id>/', credit_views.creditEdit,name ='credit-edit'),
    path('credits/remove/<int:id>/', credit_views.creditDelete,name ='credit-remove'),
    path('credits/<int:id>/', credit_views.creditDetail,name ='credit-detail'),
    path('credits/check/', credit_views.creditCheck,name ='credit-check'),

    path('credits/produits/<int:id>/', credit_views.creditProduits,name ='credit-produit'),

    path('credits/pay/<int:id>/', credit_views.creditPay,name ='credit-pay'),
    path('credits/', credit_views.creditView,name ='credit-view'),





    path('/#about', user_views.aboutUs,name ='about-us'),
    path('/#contact', user_views.contact_us,name ='contact-us'),
    path('/#service', user_views.services,name ='services'),
    path('/manage', user_views.manage,name ='manage'),



    path('admin/', admin.site.urls),
    # path('register/', user_views.register, name ='register'),
    path('login/', user_views.authenticatePage, name ='login'),
    path('logout/', user_views.logoutpage, name ='logout'),
]
