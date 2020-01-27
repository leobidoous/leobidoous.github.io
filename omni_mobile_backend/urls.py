from django.contrib import admin
from django.urls import path, include

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
