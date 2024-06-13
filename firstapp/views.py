from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm

#--------------------function to add products---------------------------#
#-----------------------------------------------------------------------#
def add(request, id):                                              
    if request.method == 'POST':                                        
        name = request.POST.get('name', None)                                  
        price = request.POST.get('price', None)                         
        quantity = request.POST.get('quantity', None)
        article = product.objects.all(id=id)                   
    
        product = {
            'name' : name,
            'price' : price,
            'quantity' : quantity
        }                                      

        return redirect('index')             
    return render(request, 'index.html', )
                           #
    if request.method == 'GET':                                         
        return render(request)                                          
#-----------------------------------------------------------------------#


#--------------------function to delete products------------------------#
#-----------------------------------------------------------------------#
def delete(request, prod_id):
    if request.method == 'DELETE':
        return render(request)
        
#-----------------------------------------------------------------------#



#--------------------function to validate products----------------------#
#-----------------------------------------------------------------------#
def modify(request, id=1):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            product = Product(name=name, price=price, quantity=quantity)
            product.save()
            return redirect('add_product')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'modify.html', {'form': form, 'products': products})
    
#-----------------------------------------------------------------------#
def test(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            product = Product(name=name, price=price, quantity=quantity)
            product.save()
            return redirect('add_product')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'index.html', {'form': form, 'products': products})
#reuquest,id
#form =Production(request.post,instance=)
