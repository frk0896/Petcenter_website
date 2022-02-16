from django.shortcuts import render,redirect
from pet_app.models import tblcategory,tblfeed,tblvaccin,tbldoctor,tblnotification,tblpets,tblquery,tblreview,tblcomplaint,tblregistration,tbllogin,tblorder
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def adminhed(request):
    return render(request,"admin-header.html")

def sellerhed(request):
    return render(request,"petseller-header.html")

def buyerhed(request):
    return render(request,"buyer-header.html")

def publiched(request):
    return render(request,"public-header.html")

def doctorhed(request):
    return render(request,"doctor-header.html")

def addcategory(request):
    return render(request,"add-category.html")

def addcategory1(request):
    if request.method == 'POST' :
        data = tblcategory()
        data.category_id="cd"
        data.category_name=request.POST.get('ctgryname')
        data.discription=request.POST.get('discription')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.status="active"
        data.save()
        
        data.category_id="ctgy00" + str(data.id)
        data.save()
        return render(request,"add-category.html")

def removecategory(request):
    items= tblcategory.objects.all()
    return render(request,"removecategory.html",{'rm':items})

def removecategory1(request,id):
    items = tblcategory.objects.get(id=id)
    items.delete()
    return redirect('/removecategory')

def feed(request):
    data = tblcategory.objects.all()
    return render(request,"feed.html",{'data':data})

def addfeed(request):
    if request.method == 'POST' :
        data = tblfeed()
        data.feed_id="fd"
        data.category_id=request.POST.get('ctgryid')
        data.feed = request.POST.get('feed')
        data.discription = request.POST.get('discription')
        data.status="active"
        data.save()

        data.feed_id="fed00" + str(data.id)
        data.save()
        return render(request,"feed.html")

def vaccination(request):
    data = tblcategory.objects.all()
    return render(request,"vaccination.html",{'data':data})

def addvaccin(request):
    if request.method =='POST' :
        data = tblvaccin()
        data.vaccination_id="va"
        data.category_id = request.POST.get('ctgryid')
        data.vaccination = request.POST.get('vaccination')
        data.details = request.POST.get('details')
        data.status="active"
        data.save()

        data.vaccination_id = "vcn00" + str(data.id)
        data.save()
        return render(request,"vaccination.html")

def adddoctor(request):
    return render(request,"add-doctor.html")

def adddoctor1(request):
    if request.method == 'POST' :
        data = tbldoctor()
        data.doctor_id="da"
        data.name=request.POST.get('name')
        data.qualification=request.POST.get('qualification')
        data.speciality = request.POST.get('speciality')
        data.address = request.POST.get('address')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.status="active"
        data.save()

        data.doctor_id= "doct00" + str(data.id)
        data.save()

        data1 = tbllogin()
        data1.username = data.doctor_id
        data1.password = request.POST.get('phone')
        data1.category = "Doctor"
        data1.save()
        return render(request,"add-doctor.html")

def removedoctor(request):
    items = tbldoctor.objects.all()
    return render(request,"remove-doctor.html",{'dt':items})

def removedoctor1(request,id):
    items = tbldoctor.objects.get(id=id)
    items.delete()
    return redirect('/removedoctor')

def addnotification(request):
    return render(request,"add-notification.html")

def addnotification1(request):
    if request.method == 'POST' :
        data = tblnotification()
        data.notification_id="ni"
        data.notification= request.POST.get('notification')
        now = datetime.datetime.now()
        time = now.strftime("%y-%m-%d")
        data.date = time
        data.status="active"
        data.save()

        data.notification_id = "notify00" + str(data.id)
        data.save()
        return render(request,"add-notification.html")

def removenotification(request):
    items = tblnotification.objects.all()
    return render(request,"remove-notification.html",{'rm':items})

def removenotification1(request,id):
    items = tblnotification.objects.get(id=id)
    items.delete()
    return redirect('/removenotification')

def addpets(request):
    data = tblcategory.objects.all()
    uid = request.session['userid']
    return render(request,"addpets.html",{'ct' : data, 'uid':uid})

def addpets1(request):
    if request.method == 'POST':
        data = tblpets()
        data.pet_id = "pi"
        data.pet_name = request.POST.get('petname')
        data.user_id = request.POST.get('userid')
        data.category_id = request.POST.get('catgryid')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.discription = request.POST.get('discription')
        data.price = request.POST.get('price')
        data.status = "active"
        data.save()

        data.pet_id = "pet00" + str(data.id)
        data.save()
        return render(request,"addpets.html")

def removepets(request):
    items = tblpets.objects.all()
    return render(request,"removepets.html",{'rm':items})

def removepets1(request,id):
    items = tblpets.objects.get(id=id)
    items.delete()
    return redirect('/removepets')

def viewfeed(request):
    data = tblcategory.objects.all()
    return render(request,"viewcategory.html",{'vw':data})
    

def viewfeed1(request,id):
    data = tblfeed.objects.filter(category_id=id)
    return render(request,"viewfeed.html",{'vw':data})

def viewvaccination(request):
    data = tblcategory.objects.all()
    return render(request,"viewcategory1.html",{'vw':data})

def viewvaccination1(request,id):
    data = tblvaccin.objects.filter(category_id=id)
    return render(request,"viewvaccination.html",{'vv':data})

def addquery(request):
    uid = request.session['userid']
    return render(request,"add-query.html",{'uid':uid})

def addquery1(request):
    if request.method == 'POST':
        data =tblquery()
        data.query_id = "qi"
        data.user_id = request.POST.get('userid')
        data.query = request.POST.get('query')
        data.status="pending"
        data.save()

        data.query_id = "qry00" + str(data.id)
        data.save()
        return render(request,"add-query.html")

def givereview(request):
    data = tblpets.objects.all()
    return render(request,"viewpets.html",{'itm':data})

def givereview1(request,id):
    uid = request.session['userid']
    return render(request,"givereview.html",{'itm':id, 'uid' :uid})

def givereview2(request):
    if request.method == 'POST' :
        data = tblreview()
        data.review_id = "ri"
        data.pet_id = request.POST.get('petid')
        data.user_id = request.POST.get('userid')
        data.review = request.POST.get('review')
        now = datetime.datetime.now()
        time = now.strftime("%y-%m-%d")
        data.review_date = time
        data.status = "active"
        data.save()

        data.review_id = "rvw00" + str(data.id)
        data.save()
        return render(request,"givereview.html")

def givecomplaint(request):
    items = tblpets.objects.all()
    return render(request,"viewpets1.html",{'itm':items})

def givecomplaint1(request,id):
    uid = request.session['userid']
    return render(request,"givecomplaint.html",{'itm':id, 'uid':uid})

def givecomplaint2(request):
    if request.method == 'POST':
        data = tblcomplaint()
        data.complaint_id ="ci"
        data.pet_id = request.POST.get('petid')
        data.user_id = request.POST.get('userid')
        data.complaint = request.POST.get('complaint')
        now = datetime.datetime.now()
        time = now.strftime('%y-%m-%d')
        data.complaint_date = time
        data.status="active"
        data.save()

        data.complaint_id = "cmpt00" + str(data.id)
        data.save()
        return render(request,"givecomplaint.html")

def registration(request):
    return render(request,"registration.html")

def registration1(request):
    if request.method == 'POST' :
        data = tblregistration()
        data.user_id = "usr"
        data.category = request.POST.get('category')
        data.name = request.POST.get('name')
        data.address = request.POST.get('address')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.status="active"
        data.save()

        data.user_id = "usr00" + str(data.id)
        data.save()

        data1 = tbllogin()
        data1.username = data.user_id
        data1.password = request.POST.get('phone')
        data1.category = request.POST.get('category')
        data1.save()
        return render(request,"registration.html")

def searchpet(request):
    data = tblcategory.objects.all()
    return render(request,"viewcategory2.html",{'itm' : data})

def searchpet1(request,id):
    data = tblpets.objects.filter(category_id=id)
    return render(request,"searchpet.html",{'itm':data})

def viewreview(request):
    data = tblpets.objects.all()
    return render(request,"viewpets2.html",{'vw':data})

def viewreview1(request,id):
    data = tblreview.objects.filter(pet_id=id)
    return render(request,"viewreview.html",{'itm':data})

def searchpet2(request):
    items = tblcategory.objects.all()
    return render(request,"viewcategory3.html",{'items':items})

def searchpet3(request,id):
    data = tblpets.objects.filter(category_id=id)
    return render(request,"viewpets3.html",{'dt':data})

def searchpet4(request,id):
    data = tblreview.objects.filter(pet_id=id)
    return render(request,"viewreview2.html",{'items':data})

def searchpet5(request,id):
    data = tblcomplaint.objects.filter(pet_id=id)
    return render(request,"viewcomplaint.html",{'items':data})

def order(request,id):
    uid = request.session['userid']
    return render(request,"order.html",{'pi':id,'uid':uid})

def order1(request):
    if request.method == 'POST' :
        data = tblorder()
        data.order_id = "oi"
        data.pet_id = request.POST.get('petid')
        data.user_id = request.POST.get('userid')
        now = datetime.datetime.now()
        time = now.strftime('%y-%m-%d')
        data.order_date = time
        data.remark = request.POST.get('remark')
        data.status = "pending"
        data.save()

        data.order_id = "ord00" + str(data.id)
        data.save()
        return render(request,"order.html")

def viewquery(request):
    data = tblquery.objects.all()
    return render(request,"viewquery.html",{'vw':data})

def answerquery(request):
    items = tblquery.objects.filter(status="pending")
    return render(request,"answerquery.html",{'itm':items})

def answerquery1(request,id):
    items = tblquery.objects.get(id=id)
    return render(request,"answerquery1.html",{'items':items})

def answerquery2(request,id):
    data = tblquery.objects.get(id=id)
    if request.method == 'POST' :
        data.replay = request.POST.get('replay')
        data.status = "ok"
        data.save()
    return redirect('/viewquery')

def vieworder(request):
    data = tblorder.objects.all()
    return render(request,"vieworder.html",{'itm':data})
    
def orderprocess(request):
    items = tblorder.objects.filter(status="pending")
    return render(request,"orderprocess.html",{'itm':items})


def orderprocess1(request,id):
    data = tblorder.objects.get(id=id)
    data.status = "Accepted"
    data.save()
    return redirect('/vieworder')

def orderprocess2(request,id):
    data = tblorder.objects.get(id=id)
    data.status = "Rejected"
    data.save()
    return redirect('/vieworder')

def orderstatus(request):
    data = tblorder.objects.filter(status="Accepted")
    return render(request,"vieworder1.html",{'dta':data})

def login(request):
    return render(request,"login.html")

def login1(request):
    if request.method == 'POST':
        data = tbllogin.objects.all()
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        flag = 0
        for d in data:
            if uname == d.username and pwd == d.password:
                type = d.category
                request.session['userid'] = uname
                flag = 1
                if type == "Admin":
                    return redirect('/adm/')
                elif type == "Seller" :
                    return redirect('/seller/')
                elif type == "Buyer" :
                    return redirect('/buyer/')
                elif type == "Doctor":
                    return redirect('/doctor/')
                else:
                    return HttpResponse("invalid acc type")
                    if flag == 0:
                        return HttpResponse("invalid user")





def searchpbc(request):
    items = tblcategory.objects.all()
    return render(request,"viewcategorypbc.html",{'items':items})

def searchpbc2(request,id):
    data = tblpets.objects.filter(category_id=id)
    return render(request,"viewpetspbc.html",{'dt':data})

def searchpbc3(request,id):
    data = tblreview.objects.filter(pet_id=id)
    return render(request,"viewreviewpbc.html",{'items':data})

def searchpbc4(request,id):
    data = tblcomplaint.objects.filter(pet_id=id)
    return render(request,"viewcomplaintpbc.html",{'items':data})

def orderpbc(request,id):
    uid = request.session['userid']
    return render(request,"orderpbc.html",{'pi':id,'uid':uid})

def orderpbc1(request):
    if request.method == 'POST' :
        data = tblorder()
        data.order_id = "oi"
        data.pet_id = request.POST.get('petid')
        data.user_id = request.POST.get('userid')
        now = datetime.datetime.now()
        time = now.strftime('%y-%m-%d')
        data.order_date = time
        data.remark = request.POST.get('remark')
        data.status = "pending"
        data.save()

        data.order_id = "ord00" + str(data.id)
        data.save()
        return render(request,"orderpbc.html")


