from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name="index"),  # 首页
    path('Bookings/', views.bookings, name="Bookings"),  # 选择预约自习室
    path('seat/<int:id>', views.seat, name="seat"),  # 预约座位
    path('recording/', views.recording, name="recording"),  # 预约座位
    path('warn/', views.warn, name="warn"),  # 警告记录

]
