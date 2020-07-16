from django.apps import AppConfig

from common.exceptions import WHSException


class ChukuConfig(AppConfig):
    name = 'chuku'


def statusChangedChuku(chuku_instance, warenhouse_instance, chuku_num, is_finished=False):
    if is_finished:
        if warenhouse_instance.normal_num < chuku_num:
            raise WHSException('库存良品数量小于出库数量，请核对库存数量后再出库！')
        else:
            warenhouse_instance.normal_num -= chuku_num
            warenhouse_instance.save()
    else:
        if chuku_instance.status == 'finished':
            warenhouse_instance.normal_num += chuku_num
            warenhouse_instance.save()


