from django.urls import path
from .views import PersonsPageView, PersonChangeView, create_person, PersonsDetailView

urlpatterns = [
	path('', PersonsPageView.as_view(), name='home'),
    path('detail/<int:pk>/', PersonsDetailView.as_view(), name='persondetail'),
    path('change/<int:pk>/', PersonChangeView.as_view(), name='personchange'),
    path('new/', create_person, name='personnew')
]
#path('new/', PersonNewView.as_view(), name='personnew')