# this context processor is needed to pass the information of the cart
# to the base-template.html to render when the user is in the login/signup page

def cartinfo(request):

    # to determine the qty of items in cart
    cart = request.session.get('shopping_cart', {})

    return {'cart': cart}
