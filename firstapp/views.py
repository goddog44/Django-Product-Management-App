from django.shortcuts import redirect, render
from .models import Product


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
def validate(request, prod_id):
    if request.method == 'POST':
        name = request.POST.get('name', None)                                  
        price = request.POST.get('price', None)                         
        quantity = request.POST.get('quantity', None)                   
        return render(request)                                          
    if request.method == 'GET':
        return render(request)
    
#-----------------------------------------------------------------------#

def test(request):
    # Retrieve all values from the database
    products = Product.objects.all()

    return render(request, "index.html", {'products': products})