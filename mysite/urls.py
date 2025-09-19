from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('', include('blog.urls')),   # '/'로 들어오는 요청은 blog.urls로 전달
]