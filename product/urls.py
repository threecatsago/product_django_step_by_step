"""
URL configuration for product project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    使用元组('index.urls', 'index')并指定namespace='index'的方式为你的URL配置提供了一个额外层次的组织结构。
    这使得在模板和视图中反向解析URL时，即使在不同的应用中有相同的URL名，也能通过命名空间和应用名准确地定位到具体的URL。
    例如，如果你在index应用和另一个应用dashboard中都有一个名为home的URL，你可以在模板中这样区分它们：
    index应用的home URL：{% url 'index:home' %}
    dashboard应用的home URL：{% url 'dashboard:home' %}
    这样，即使两个应用中的URL名称相同，使用命名空间也能确保链接到正确的URL。
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings

# from emotion_wheel.views import emotion_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('index/', include(('index.urls', 'index'), namespace='index')),
    path('commodity/', include(('commodity.urls', 'commodity'), namespace='commodity')),
    path('shopper/', include(('shopper.urls', 'shopper'), namespace='shopper'))
    # path('emotions/', emotion_view, name='core_emotions'),
    # path('emotions/<int:parent_id>/', emotion_view, name='sub_emotions'),

]
