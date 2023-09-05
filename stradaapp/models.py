from django.db import models
import uuid

# Create your models here.


class Product(models.Model):
    pname = models.CharField(max_length=50, verbose_name="Product Name")

    pid = models.CharField(max_length=40, verbose_name="Product ID", primary_key=True, null=False, default=uuid.uuid4)

    inrdisplay = models.CharField(max_length=10, verbose_name="Display Price (INR)", default="0", blank=False)
    usddisplay = models.CharField(max_length=10, verbose_name="Display Price (USD)", default="0", blank=False)

    inrprice = models.IntegerField(verbose_name="Price (INR)", default=0, blank=False)
    usdprice = models.FloatField(verbose_name="Price (USD)", default=0, blank=False)

    discount = models.IntegerField(verbose_name="Discount (%)", default=0)

    img0 = models.CharField(max_length=30, verbose_name="Image 1", blank=False, default="", null=False)
    img1 = models.CharField(max_length=30, verbose_name="Image 2", blank=False, default="", null=False)
    img2 = models.CharField(max_length=30, verbose_name="Image 3", blank=False, default="", null=False)
    img3 = models.CharField(max_length=30, verbose_name="Image 4", blank=True, null=True)
    img4 = models.CharField(max_length=30, verbose_name="Image 5", blank=True, null=True)
    img5 = models.CharField(max_length=30, verbose_name="Image 6", blank=True, null=True)
    img6 = models.CharField(max_length=30, verbose_name="Image 7", blank=True, null=True)
    img7 = models.CharField(max_length=30, verbose_name="Image 8", blank=True, null=True)
    img8 = models.CharField(max_length=30, verbose_name="Image 9", blank=True, null=True)
    img9 = models.CharField(max_length=30, verbose_name="Image 10", blank=True, null=True)

    desc = models.TextField(max_length=500, verbose_name="Product Description", null=True, blank=True)

    def __str__(self):
        return self.pname


class Order(models.Model):
    completed = models.BooleanField(verbose_name="Completed", default=False)

    fname = models.CharField(max_length=50, verbose_name="First Name", null=False, blank=False)
    lname = models.CharField(max_length=50, verbose_name="Last Name", null=False, blank=False)
    phone = models.CharField(max_length=15, verbose_name="Phone Number", null=False, blank=False)
    email = models.CharField(max_length=100, verbose_name="Email", null=False, blank=False)
    address1 = models.CharField(max_length=100, verbose_name="Address Line 1", null=False, blank=False)
    address2 = models.CharField(max_length=100, verbose_name="Address Line 2", blank=True)
    landmark = models.CharField(max_length=100, verbose_name="Landmark", blank=True)
    city = models.CharField(max_length=100, verbose_name="City", null=False, blank=False)
    state = models.CharField(max_length=100, verbose_name="State", null=False, blank=False)
    country = models.CharField(max_length=100, verbose_name="Country", null=False, blank=False)
    zipcode = models.CharField(max_length=15, verbose_name="ZIP", null=False, blank=False)

    ordervalue = models.TextField(max_length=1000, verbose_name="Order", null=False, blank=False)

    total = models.IntegerField(verbose_name="Total Amount", blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created", null=False, blank=False)

    def __str__(self):
        return self.fname + " " + self.lname

class Message(models.Model):
    fname = models.CharField(max_length=50, verbose_name="First Name", null=False, blank=False)
    lname = models.CharField(max_length=50, verbose_name="Last Name", null=False, blank=False)
    email = models.CharField(max_length=100, verbose_name="Email", null=False, blank=False)
    message = models.TextField(max_length=250, verbose_name="Message", null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created", null=False, blank=False)

    def __str__(self):
        return self.email