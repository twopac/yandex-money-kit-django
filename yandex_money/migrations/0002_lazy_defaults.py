# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from yandex_money.models import (
    get_default_shop_id,
    get_default_scid,
    get_default_success_url,
    get_default_fail_url,
)


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='success_url',
            field=models.URLField(default=get_default_success_url, verbose_name=u'URL успешной оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='fail_url',
            field=models.URLField(default=get_default_fail_url, verbose_name=u'URL неуспешной оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='scid',
            field=models.PositiveIntegerField(default=get_default_scid, verbose_name=u'Номер витрины'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='shop_id',
            field=models.PositiveIntegerField(default=get_default_shop_id, verbose_name=u'ID магазина'),
        ),
    ]
