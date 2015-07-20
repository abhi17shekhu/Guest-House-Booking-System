from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Pend(models.Model): #each class is a DB
    
    status_choices = (                    #dict datastructure for status field drop down
        ('Pending', 'Pending'),
        ('Granted', 'Granted'),
        ('Arrived', 'Arrived'),
        ('Departed', 'Departed'),
    )

    category_type = (                    #dict datastructure for category field drop down
        ('Personal Guest', 'Personal Guest'),
        ('Departmental Guest', 'Department Guest'),
    )

    count = 0
    totalrooms = 30
    #variables of a DB with their type
    author = models.ForeignKey('auth.User')
    #sec_clearance = models.ForeignKey('UserProfile',null = True)
    booking_date = models.DateTimeField(
            default=timezone.now)
    gname = models.CharField(max_length=30)
    bookin = models.CharField(max_length=100)
    dept = models.CharField(max_length=40)
    roomsno = models.CharField(max_length=5,default='1/0')
    address = models.CharField(max_length=200,default='e.g House Number,Street,City,State,PINCODE')
    status = models.CharField(max_length=40,default='Pending',choices = status_choices)
    tele_no = models.CharField(max_length=20,default='CountryCode-Number')
    email = models.EmailField(max_length=200,default='user@example.com')
    purpose = models.CharField(max_length=100,default='')
    categ = models.CharField(max_length=30,choices = category_type,default='Personal Guest')
    expad = models.DateTimeField(
            default=timezone.now)
    expdd = models.DateTimeField(
            default=timezone.now)



    #preset functions for running into the html template
    def publish(self):
    	self.booking_date = timezone.now()
    	self.save()

    def increment(self):
        self.count = self.count + 1

    def gen_id(self):
        self.bookingID = self.bookingID + 1
    
    def confirm_arrival(self):
        self.status = 'Arrived'

    def __str__(self):
        return self.gname

