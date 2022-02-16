from django.db import models

# Create your models here.
class tblcategory(models.Model):
    category_id = models.CharField(max_length=50)
    category_name = models.CharField(max_length=90)
    discription = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

class Meta:
    db_table = "tblcategory"


class tblfeed(models.Model):
    feed_id = models.CharField(max_length=50)
    category_id = models.CharField(max_length=50)
    feed = models.CharField(max_length=90)
    discription = models.CharField(max_length=100)

class Meta:
    db_table = "tblfeed"

class tblvaccin(models.Model):
    vaccination_id = models.CharField(max_length=30)
    category_id = models.CharField(max_length=30)
    vaccination = models.CharField(max_length=90)
    details = models.CharField(max_length=90)

class Meta:
    db_table= "tblvaccin"

class tbldoctor(models.Model):
    doctor_id = models.CharField(max_length=30)
    name = models.CharField(max_length=90)
    qualification = models.CharField(max_length=90)
    speciality = models.CharField(max_length=90)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

class Meta:
    db_table = "tbldoctor"

class tblnotification(models.Model):
    notification_id = models.CharField(max_length=50)
    notification = models.CharField(max_length=150)
    date = models.CharField(max_length=90)

class Meta:
    db_table = "tblnotification"


class tblpets(models.Model):
    pet_id = models.CharField(max_length=70)
    pet_name = models.CharField(max_length=90)
    user_id = models.CharField(max_length=90)
    category_id = models.CharField(max_length=90)
    photo = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    price = models.CharField(max_length=90)
    status = models.CharField(max_length=80)

class Meta:
    db_table = "tblpets"

class tblquery(models.Model):
    query_id = models.CharField(max_length=60)
    user_id = models.CharField(max_length=60)
    query = models.CharField(max_length=100)
    replay = models.CharField(max_length=100)
    status = models.CharField(max_length=80)
class Meta:
    db_table = "tblquery"

class tblreview(models.Model):
    review_id = models.CharField(max_length=80)
    pet_id = models.CharField(max_length=80)
    user_id = models.CharField(max_length=80)
    review = models.CharField(max_length=100)
    review_date = models.CharField(max_length=80)

class Meta:
    db_table = "tblreview"

class tblcomplaint(models.Model):
    complaint_id = models.CharField(max_length=80)
    pet_id = models.CharField(max_length=80)
    user_id = models.CharField(max_length=80)
    complaint = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=80)

class Meta:
    db_table = "tblcomplaint"

class tblregistration(models.Model):
    user_id = models.CharField(max_length=80)
    category = models.CharField(max_length=90)
    name = models.CharField(max_length=90)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=100)

class Meta:
    db_table = "tblregistartion"

class tbllogin(models.Model):
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=90)
    category = models.CharField(max_length=90)

class Meta:
    db_table = "tbllogin"

class tblorder(models.Model):
    order_id = models.CharField(max_length=80)
    pet_id = models.CharField(max_length=80)
    user_id = models.CharField(max_length=80)
    order_date = models.CharField(max_length=80)
    remark = models.CharField(max_length=100)
    status = models.CharField(max_length=80)

class Meta:
    db_table = "tblorder"
