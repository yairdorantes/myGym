def cart_total_amount(request):
    total = 0.0
    try:
        if request.user.is_authenticated:
            for key,value in request.session['cart'].items():
                total = total + (float(value['price'])* value['quantity'])
    except KeyError:
        pass    
    return {'cart_total_amount': total}

def num_products(request):
    totals=0
    try:
        for i,j in request.session['cart'].items():
            totals+=j['quantity']
    except KeyError:
        pass
    return {'totales':totals}


