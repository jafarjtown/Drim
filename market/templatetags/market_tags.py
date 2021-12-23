from django import template

register = template.Library()

@register.simple_tag
def get_amount_in_cart(itemId, cart):

    if cart:
        return cart.price(itemId)

# register.filter('get_amount_in_cart', get_amount_in_cart)