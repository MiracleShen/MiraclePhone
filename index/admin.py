from django.contrib import admin
import requests,json
# Register your models here.
from django.contrib import admin
from index.models import News, Service,Park

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

class ParkAdmin(admin.ModelAdmin):
    fields = ('Name','Address','Level', 'Manager', 'Memo')
    search_fields = ('Province', 'City', 'District', 'Town','Name','Address','Level', 'Manager','Memo')
    list_display = ('Province', 'City', 'District', 'Town','Name','Address','Level', 'Manager','createdtime', 'updatedtime', 'Memo')
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        ADDRESS = ''
        ADDRESS = obj.Address
        # 根据园区名称获得坐标
        URL2 = 'https://api.map.baidu.com/geocoding/v3/'
        params2 = {
            "ak": 'Xmjf4HD2kly5zqZybYhmZV9RW7fx7ass',
            "output": 'json',
            "address": ADDRESS,
            "ret_coordtype": 'bd09II',
        }
        res2 = requests.get(url=URL2, params=params2)
        # print (res2)
        res22 = json.loads(res2.text)
        # print (res22)
        res23 = str(res22['result']['location']['lat']) + ',' + str(res22['result']['location']['lng'])
        # 根据坐标获得所在的国家、省份、城市、区县、乡镇、街道
        URL3 = 'https://api.map.baidu.com/reverse_geocoding/v3/'
        ####测试行级按钮获得六级地址
        params3 = {
            "ak": 'Xmjf4HD2kly5zqZybYhmZV9RW7fx7ass',
            "output": 'json',
            "coordtype": 'bd09II',
            "ret_coordtype": 'bd09II',
            "extensions_town": "true",
            "extensions_road": "true",
            "location": res23,
            "sub_admin": 3
        }
        res3 = requests.get(url=URL3, params=params3)
        print(res3.text)
        res33 = json.loads(res3.text)['result']
        #####测试行级按钮获取六级地址
        add = json.loads(res3.text)['result']
        add1 = add['addressComponent']['province'] + add['addressComponent']['city'] + add['addressComponent'][
            'district'] + add['addressComponent']['town']
        res33 = res23

        obj.Province = add['addressComponent']['province']
        obj.City = add['addressComponent']['city']
        obj.District = add['addressComponent']['district']
        obj.Town = add['addressComponent']['town']
        super().save_model(request,obj,form,change)


admin.site.register(Park, ParkAdmin)