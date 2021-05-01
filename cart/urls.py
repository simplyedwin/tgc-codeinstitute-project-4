from django.urls import path, include
import cart.views


urlpatterns = [
    path('add/<plant_id>', cart.views.add_to_cart,
         name="add_to_cart"),
    path('', cart.views.view_cart, name='view_cart'),
    # path('flash_msg/', cart.views.post_flash_msg,
    #      name="flash_msg"),

]
