from django.urls import path
from . import views
app_name = 'market'
urlpatterns = [
    path('<int:mid>/', views.Index, name='market-home'),
    path('<int:mid>/item/<int:iid>/', views.ItemIndex, name='item'),
    path('<int:mid>/item/<int:iid>/add', views.AddToCart, name='add'),
    path('cart/', views.UserCart, name='cart'),
]
