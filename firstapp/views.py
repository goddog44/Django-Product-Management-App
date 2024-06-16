from django.shortcuts import redirect, render, get_object_or_404
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
                                        
#-----------------------------------------------------------------------#


#--------------------function to delete products------------------------#
#-----------------------------------------------------------------------#
# def delete(request, prod_id):
#     if request.method == 'DELETE':
#         return render(request)
        
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
            return redirect('modify_product')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'modify.html', {'form': form, 'products': products})
    
#-----------------------------------------------------------------------#
def test(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price']
            # quantity = form.cleaned_data['quantity']
            # product = Product(name=name, price=price, quantity=quantity)
            # product.save()
            form.save()
            print("saved successfully")
            return redirect('add_product')
    else:
        form = ProductForm()
    products = Product.objects.all()
    return render(request, 'index.html', {'form': form, 'products': products})
#request, id
#form = Production(request.post, instance=)

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('modify_product')

#--------------------function to update products----------------------#
#-----------------------------------------------------------------------#
def update(request, id):
    product = Product.objects.get(id=id)  # Fetch the product object
    form = ProductForm(request.POST)
    form = ProductForm(initial={'name': product.name, 'price': product.price, 'quantity': product.quantity})  # Populate form with initial values
    
    products = Product.objects.all()
    return render(request, 'modify.html', {'form': form, 'products': products, 'product': product})



def finalupdate(request, id):
    products = Product.objects.get(id=id)
    product = Product.objects.get(id=id)
    # products.delete()
    form = ProductForm(request.POST or  None,instance = product)
    if request.method == 'POST':
        if form.is_valid():
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price']
            # quantity = form.cleaned_data['quantity']
            # product = Product(name=name, price=price, quantity=quantity)
            # product.save()
            form.save()
            print("saved successfully")
            return redirect('modify_product')
    else:
        # form = ProductForm(instance = product)
        pass
    products = Product.objects.all()
    return render(request, 'modify.html', {'form': form, 'products': products, 'dev':product})