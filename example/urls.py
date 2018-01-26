# -*- coding: utf-8 -*-

import django
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from app.views import OrderPage

admin.autodiscover()

urlpatterns = [
    url(r'payment-form/$', OrderPage.as_view(), name='payment_form'),
    url(r'fail-payment/$', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
    url(r'success-payment/$', TemplateView.as_view(template_name='success.html'), name='payment_success'),
    url(r'^yandex-money/', include('yandex_money.urls')),
]

if django.VERSION < (1, 9):
    urlpatterns.append(
        url(r'^admin/', include(admin.site.urls))
    )
else:
    urlpatterns.append(
        url(r'^admin/', admin.site.urls)
    )

urlpatterns += staticfiles_urlpatterns()
