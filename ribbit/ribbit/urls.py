"""ribbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', 'ribbit_app.views.login_view'), #login
    url('^$', 'ribbit_app.views.index'),
    url(r'^logout$', 'ribbit_app.views.logout_view'),
    url(r'^signup$', 'ribbit_app.views.signup'),
    url(r'^ribbits$', 'ribbit_app.views.public'),
    url(r'^submit$', 'ribbit_app.views.submit'), 
    url(r'^users/$', 'ribbit_app.views.users'),
    url(r'^users/(?<username>\w{0,30})/$', 'ribbit_app.views.users'),
    url(r'^follow$', 'ribbit_app.views.follow'),
]
