from urllib import request
from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd

def chart_select_view(request):
    error_message = None

    # qs1 = Product.objects.all().values() # --> Dictionary
    # qs2 = Product.objects.all().values_list() # --> List
   
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['product_id'] = product_df['id']
    print(purchase_df.shape) # --> (5, 7) 5:items; 7:fields

    if purchase_df.shape[0] > 0: # if there are items
        df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1).rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
   
        if request.method == 'POST':
            chart_type = request.POST.get('sales')
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']
            print(chart_type)
            print("Date from:", date_from, " Date to:", date_to)
    else:
        error_message = "No records in the database"
        df = None

    context = {
        "error_message": error_message,
        
    }
    return render(request, "products/main.html", context)
