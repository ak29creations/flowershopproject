from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import District, Place, Flower,Order


def index(request):
    districts = District.objects.all()
    return render(request, 'index.html', {'districts': districts})


def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})

def order(request):
    districts = District.objects.all()
    if request.method=='POST':
        customer_name = request.POST['customer_name']
        customer_phone = request.POST['customer_phone']
        customer_email = request.POST['customer_email']
        customer_address = request.POST['customer_address']
        district = District.objects.get(id=request.POST['district'])
        center = Place.objects.get(id=request.POST['center'])
        flower = Flower.objects.get(id=request.POST['flower'])
        quantity = request.POST['quantity']
        total = request.POST['total']
        order = Order.objects.create(customer_name=customer_name,customer_phone=customer_phone,customer_email=customer_email,customer_address=customer_address,district=district,place=center,flower=flower,quantity=quantity,total=total)
        order.save()
        messages.success(request, 'Order Successfully Placed')
        return redirect('order')
    return render(request, 'order.html', {'districts': districts,'button':True})

@csrf_exempt
def get_centers(request):
    if request.method == 'POST':
        district_id = request.POST['district_id']
        centers = Place.objects.filter(district_id=district_id).all()
    return render(request, 'centers.html', {'centers': centers})

@csrf_exempt
def get_flowers(request):
    if request.method == 'POST':
        center_id = request.POST['center_id']
        flowers = Flower.objects.filter(place_id=center_id).all()
    return render(request, 'flowers.html', {'flowers': flowers})
