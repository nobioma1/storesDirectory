from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    path('store/post/<int:pk>', views.StoreDetailView.as_view(), name='storedetail'),
    path('store/new/', views.StoreCreateView.as_view(), name='newstore'),
    path('store/post/<int:pk>/edit/',views.StoreUpdateView.as_view(), name='editstore'),
    path('post/<int:pk>/delete/', views.StoreDeleteView.as_view(), name='deletestore'),

]
