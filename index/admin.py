from django.contrib import admin

# Register your models here.
from django.contrib import admin
from index.models import News, Service

admin.AdminSite.site_header = 'MiraclePhone系统'
admin.AdminSite.site_title = 'MiraclePhone系统'


class NewsAdmin(admin.ModelAdmin):
    fields = ('Catagory', 'Title', 'Content')
    search_fields = ('Catagory', 'Title', 'Content')
    list_display = ('Catagory', 'Title', 'Content', 'createdtime', 'updatedtime')
    list_per_page = 10


admin.site.register(News, NewsAdmin)


class ServiceAdmin(admin.ModelAdmin):
    fields = ('idx','Type', 'Name', 'Must', 'Price', 'Unit', 'Memo')
    search_fields = ('idx','Type', 'Name', 'Must', 'Price', 'Unit', 'Memo')
    list_display = ('idx','Type', 'Name', 'Must', 'Price', 'Unit', 'createdtime', 'updatedtime', 'Memo')
    list_per_page = 10


admin.site.register(Service, ServiceAdmin)
