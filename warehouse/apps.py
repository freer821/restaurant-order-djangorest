from django.apps import AppConfig

from warehouse.models import Warehouse


class WarehouseConfig(AppConfig):
    name = 'warehouse'


def addWareIntoWarehous(user, product_name, num):
    warehouse = Warehouse.objects.filter(owner_id=user, product_name=product_name).first()
    if warehouse is None:
        Warehouse.objects.create(owner_id=user,
                                 product_name=product_name,
                                 unknown_num=num)
    else:
        warehouse.unknown_num += num
        warehouse.save()


