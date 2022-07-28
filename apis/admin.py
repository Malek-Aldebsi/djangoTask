from django.contrib import admin
from .models import Channel, kitchefy_user, Fp, Fp_branch, Brand, Brand_branch, Status, Days, Opening_hours, Offers, Announcement_center, Knowleddge_center_section, Knowledge_center, Type_rating, Liability, Incident_report, Order, Item, Order_Item, Add_ons, Order_item_add_ons

admin.site.register(Channel)
admin.site.register(kitchefy_user)
admin.site.register(Fp)

admin.site.register(Fp_branch)
admin.site.register(Brand)
admin.site.register(Brand_branch)

admin.site.register(Status)
admin.site.register(Days)
admin.site.register(Opening_hours)

admin.site.register(Offers)
admin.site.register(Announcement_center)
admin.site.register(Knowleddge_center_section)

admin.site.register(Knowledge_center)
admin.site.register(Type_rating)
admin.site.register(Liability)

admin.site.register(Incident_report)
admin.site.register(Order)
admin.site.register(Item)

admin.site.register(Order_Item)
admin.site.register(Add_ons)
admin.site.register(Order_item_add_ons)