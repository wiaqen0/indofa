from django.urls import path
from .views import successfulorder,query_from_product_name,saveorder,checkout,dynamic_lookup_view, delete_order,customize, cart, returnhome #decor, get_user_order, pot_order, gompot_order,  cuqua_order, plant_order, plapot_order,flower_order, veg_order,soil_order,other_order,hangpot_order 
urlpatterns = [
    path('<int:id>', dynamic_lookup_view, name='lookup'),
    # path('pot', pot_order, name='pot_order'),
    # path('gompot', gompot_order, name='gompot_order'),
    # path('plapot', plapot_order, name='pot_order'),
    # path('hangpot', hangpot_order, name='pot_order'),
    # path('other', other_order, name='other_order'),
    # path('plant', plant_order, name='plant_order'),
    # path('flower', flower_order, name='flower_order'),
    # path('veg', veg_order, name='veg_order'),
    # path('soil', soil_order, name='soil_order'),
    # path('cuqua', cuqua_order, name='soil_order'),
    # path('decor', decor, name='soil_order'),
    path('delete/<int:id>', delete_order, name='delete_order'),
    path('customize', customize, name='customize'),
    path('cart', cart, name='cart'),
    path('ordersuccess', successfulorder, name='ordersuccess'),
    path('checkorder', saveorder, name='checkorder'),
    path('checkout', checkout, name='checkout'),
    path('register/account', returnhome, name='returnhome'),
    # path('filter', returnhome, name='filter'),
    path('<str:product>', query_from_product_name, name='query'),
]