from django.contrib import admin
from sign.models import Event, Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    # 显示列表
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    # 搜索栏
    search_fields = ['name']
    # 过滤器
    list_filter = ['status']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'phone', 'sign', 'create_time', 'event']
    # 搜索栏
    search_fields = ['real_name', 'phone']
    # 过滤器
    list_filter = ['sign']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
