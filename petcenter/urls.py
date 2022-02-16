"""petcenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pet_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('login/',views.login),
    path('adm/',views.adminhed),
    path('seller/',views.sellerhed),
    path('buyer/',views.buyerhed),
    path('public/',views.publiched),
    path('doctor/',views.doctorhed),
    path('addcategory/',views.addcategory),
    path('addcategory1/',views.addcategory1),
    path('removecategory/',views.removecategory),
    path('remove/<int:id>',views.removecategory1),
    path('feed/',views.feed),
    path('feed1/',views.addfeed),
    path('vaccin/',views.vaccination),
    path('vaccination/',views.addvaccin),
    path('adddoctor/',views.adddoctor),
    path('adddoctor1/',views.adddoctor1),
    path('removedoctor/',views.removedoctor),
    path('remove1/<int:id>',views.removedoctor1),
    path('addnotification/',views.addnotification),
    path('addnotification1/',views.addnotification1),
    path('removenotification/',views.removenotification),
    path('removenotification1/<int:id>',views.removenotification1),
    path('addpets/',views.addpets),
    path('addpets1/',views.addpets1),
    path('removepets/',views.removepets),
    path('removepets1/<int:id>',views.removepets1),
    path('viewfeed/',views.viewfeed),
    path('viewfeed1/<str:id>',views.viewfeed1),
    path('viewvaccination/',views.viewvaccination),
    path('viewvaccination1/<str:id>',views.viewvaccination1),
    path('addquery/',views.addquery),
    path('addquery1/',views.addquery1),
    path('givereview/',views.givereview),
    path('givereview1/<str:id>',views.givereview1),
    path('givereview2/',views.givereview2),
    path('givecomplaint/',views.givecomplaint),
    path('givecomplaint1/<str:id>',views.givecomplaint1),
    path('givecomplaint2/',views.givecomplaint2),
    path('registration/',views.registration),
    path('registration1/',views.registration1),
    path('searchpet/',views.searchpet),
    path('searchpet1/<str:id>',views.searchpet1),
    path('viewreview/',views.viewreview),
    path('viewreview1/<str:id>',views.viewreview1),
    path('searchpet2/',views.searchpet2),
    path('searchpet3/<str:id>',views.searchpet3),
    path('viewreview2/<str:id>',views.searchpet4),
    path('viewcomplaint/<str:id>',views.searchpet5),
    path('order/<str:id>',views.order),
    path('order1/',views.order1),
    path('viewquery/',views.viewquery),
    path('answerquery/',views.answerquery),
    path('answerquery1/<int:id>',views.answerquery1),
    path('answerquery2/<int:id>',views.answerquery2),
    path('vieworder/',views.vieworder),
    path('orderprocess/',views.orderprocess),
    path('orderprocess1/<int:id>',views.orderprocess1),
    path('orderprocess2/<int:id>',views.orderprocess2),
    path('orderstatus/',views.orderstatus),
    path('login/',views.login),
    path('login1/',views.login1),
   
    path('searchpbc/',views.searchpbc),
    path('searchpbc2/<str:id>',views.searchpbc2),
    path('viewreviewpbc/<str:id>',views.searchpbc3),
    path('viewcomplaintpbc/<str:id>',views.searchpbc4),
    path('orderpbc/<str:id>',views.orderpbc),
    path('orderpbc1/',views.orderpbc1),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
