from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Product, Order, SimpleOrder

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Hole die Daten aus der übermittelten Form
        customer_id = request.POST.get('customer_id')
        product_ids = request.POST.getlist('product_ids')
        
        # Mache Kundenobjekt aus ausgewähltem Kunden in der Form
        customer = Customer.objects.get(id=customer_id)
        
        # Bestellung erstellen
        order = Order.objects.create(customer=customer)
        
        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            order.product.add(product)

        return HttpResponse(f'custumor: {customer.name}; products: {product_ids}')
    
    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'ecommerce/order.html', {'customers': customers, 'products': products})

def simple(request):
    if request.method == 'POST':
        post_data = request.POST.dict()
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email'),
        product= request.POST.get('product')
        
        order = SimpleOrder(
            name=name,
            city=city,
            email=email,
            product=product
        )
        order.save()
        
        # Anzeigenamen des Produkts abrufen
        product_name = order.get_product_display()  
              
        return HttpResponse((f"<h1>Thank you, {name}!</h1><p>Your order for {product_name} has been placed.</p><p>{post_data}</p>"))
        
        
    return render(request, 'ecommerce/simple.html')