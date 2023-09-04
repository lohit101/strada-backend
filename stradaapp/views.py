from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
import base64
from .models import Product, Order, Message

# Create your views here.
def home(request):
    return HttpResponse("200 OK/")

def products(request):
    products = Product.objects.all().values()

    data = json.dumps(list(products), indent=2)

    return HttpResponse(data, content_type='application/json')

def display(request, pid):
    product = Product.objects.filter(pid=pid)

    data = serialize('json', product)
    data = json.loads(data)
    data = json.dumps(data, indent=2)

    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def message(request):
    message = Message()

    data = request.body.decode()
    data = json.loads(data)

    message.fname = data["fname"]
    message.lname = data["lname"]
    message.email = data["email"]
    message.message = data["message"]

    message.save()

    response = {}
    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def payment(request):
    order = Order()

    data = request.body.decode()
    data = json.loads(data)

    print(json.dumps(data, indent=2))

    total = data["total"]
    ordervalue = ""

    for i in data["passVal"]:
        ordervalue += data["passVal"][str(i)]["pname"] + " --- " + data["passVal"][str(i)]["pid"] + " --- " + data["passVal"][str(i)]["inrdisplay"] + " | "

    order.fname = data["passData"]["fname"]
    order.lname = data["passData"]["lname"]
    order.phone = data["passData"]["pcode"] + " " + data["passData"]["phone"]
    order.email = data["passData"]["email"]
    order.address1 = data["passData"]["address1"]
    order.address2 = data["passData"]["address2"]
    order.landmark = data["passData"]["landmark"]
    order.city = data["passData"]["city"]
    order.state = data["passData"]["state"]
    order.country = data["passData"]["country"]
    order.zipcode = data["passData"]["zip"]

    order.ordervalue = ordervalue
    order.total = total

    order.save()
    
    response = {}
    return HttpResponse(response, content_type='application/json')