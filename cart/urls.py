from django.urls import path, include
import cart.views


urlpatterns = [
    path('add/<plant_id>', cart.views.add_to_cart,
         name="add_to_cart"),
    path('', cart.views.view_cart, name='view_cart'),

]
