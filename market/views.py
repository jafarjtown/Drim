from django.shortcuts import redirect, render
from .models import Cart, Market,Shop,Item
# Create your views here.

def Index(request, mid):
    usercart = request.user.cart
    
    context = {}
    market = Market.objects.prefetch_related('shops').defer('page').get(id = mid)
    shops = market.shops.all()
    
    if request.method == 'POST':
        shop = request.POST.get('shop')
        price = request.POST.get('price')
        name = request.POST.get('name')
        file = request.POST.get('file')
        cartshop = market.shops.get(name = shop)
        print(cartshop)
        item = Item.objects.create(name = name, price = price)
        cartshop.items.add(item)
    items = Item.objects.filter(shop__in = shops).order_by('-id')
    if request.GET.get('shop'):
        shopName = request.GET.get('shop')
        items = market.shops.prefetch_related('items').get(name = shopName).items.all()
    context['market'] = market
    context['shops'] = shops
    context['items'] = items
    return render(request, 'market/index.html', context)

def ItemIndex(request,mid, iid):
    context = {}
    item = Item.objects.get(id = iid)
    context['item'] = item
    context['marketId'] = mid
    return render(request, 'market/item.html', context)

def AddToCart(request,mid, iid):
    it = Item.objects.get(id = iid)
    cart = Cart.objects.get_or_create(user = request.user)[0]
    # print(cart[0]/)
    if cart.items.filter(item = it).exists():
        itemcart = cart.items.get(item = it)
        itemcart.amount += 1
        itemcart.save()
        print(itemcart)
    else:
        print('hello')
        itemcart = cart.items.create(item = it, amount = 1)
        cart.save()
    return redirect('market:item',mid, iid)    

def UserCart(request):
    context = {}
    useritems = Cart.objects.get_or_create(user = request.user)[0].items.all()
    context['items'] = useritems
    return render(request, 'market/cart.html', context)