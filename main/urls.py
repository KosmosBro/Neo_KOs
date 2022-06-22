from django.urls import path
import main.views as v

app_name = 'main'

urlpatterns = [
    path('', v.view_home, name='home'),
]
