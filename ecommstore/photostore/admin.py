from django.contrib import admin
from photostore.models import Customer, Product, Order, Cart

# imports for redirecting url
from django.utils.http import urlencode
from django.urls import reverse, path
from django.utils.html import format_html



#admin site customisation
# class MyAdminSite(admin.AdminSite):
#     site_header = "PG Picsies Administration"
#     site_title = "Administration"
#     index_title = "PG Picsies"
#     app_index_template = "admin/index.html"


#     def register(self, model_or_iterable, admin_class=None, **options):
#         result = super().register(model_or_iterable, admin_class, **options)
#         return result


    # def index(self, request, extra_context=None):
    #     app_dict = {}
    #     for model, model_admin in self._registry.items():
    #         app_label = model._meta.app_label
    #         if app_label not in app_dict:
    #             app_dict[app_label] = {}
    #         app_dict[app_label][model.__name__] = model_admin

    #     extra_context = extra_context or {}
    #     extra_context['app_dict'] = app_dict
    #     return super().index(request, extra_context)


# admin_site = MyAdminSite(name='customadmin')



# Model Registration, ModelAdmin customisation
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "customer_type")
    list_filter = ("customer_type", )

#admin_site.register(Customer, CustomerAdmin)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "theme", "category", "view_image_link", )
    list_display_links = ("title", )
    list_filter = ("category", "theme", "author", )
    search_fields = ("title__icontains", )

    def view_image_link(self, obj):
        url_text = 'Display Image'
        result = Product.objects.filter(pk=obj.id).values_list('image_url', flat=True)
        url = ''.join(link for link in result)
        default_url = "https://www.pexels.com" 
        
        # retrieve images stored in media dir
        if url == default_url:
            result = Product.objects.get(pk=obj.id)
            url = result.image.url
            return format_html('<a href={} target="_blank">{}</a>'.format(url, url_text))            
        else:
            return format_html('<a href={} target="_blank">{}</a>'.format(url, url_text))

    view_image_link.short_description = 'Image Preview'

#admin_site.register(Product, ProductAdmin)



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("view_customer_link", "view_item_link", "quantity", )
    list_filter = ("item__title", )

    # redirect to Customers model
    def view_customer_link(self, obj):
        url = (
            reverse('admin:photostore_customer_changelist')
            + "?"
            + urlencode({"customer_type": f"{obj.customer_info.customer_type}"})
        )
        url_text = obj.customer_info.full_name
        return format_html('<a href={}>{}</a>', url, url_text)
    view_customer_link.short_description = "Customer"


    # display item(image) in cart in a new tab
    def view_item_link(self, obj):
        # retrieve image_url 
        result = Product.objects.filter(pk=obj.item.id).values_list('image_url', flat=True)
        # collect image_url as string
        url = ''.join(i for i in result)
        url_text = obj.item.title
        return format_html('<a href={} target="_blank">{}</a>'.format(url, url_text))
    view_item_link.short_description = "Item Preview"

#admin_site.register(Cart, CartAdmin)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("view_order_link", "view_cart_link", "order_date", "order_status", "payment")
    list_display_links = ("order_date", )

    def view_order_link(self, obj):
        order_item = Product.objects.get(pk=obj.customer_order.item.id)
        url = order_item.image_url
        url_text = f"{order_item.title} By {order_item.author}" 
        return format_html('<a href={} target="_blank">{}</a>'.format(url, url_text))
    view_order_link.short_description = "Order Preview"

    def view_cart_link(self, obj):
        url = (
            reverse('admin:photostore_cart_changelist')
            + "?"
            + urlencode({"item__title":f"{obj.customer_order.item.title}"})
        )        
        return format_html('<a href={}>Show</a>', url)
    view_cart_link.short_description = "View Cart"

#admin_site.register(Order, OrderAdmin)



