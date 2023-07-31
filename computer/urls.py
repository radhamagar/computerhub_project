from django.contrib import admin
from django.urls import include,path
from . import views



urlpatterns = [
    # path('computer/', views.computer, name='computer'),
    # path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('computer/', views.CreateComputerView.as_view(), name='computer'),
    path('update/<int:pk>', views.UpdateComputerView.as_view(), name='update_computer'),
    path('delete/<int:pk>', views.DeleteComputerView.as_view(), name='delete_computer'),
    path('brand', views.CreateBrandView.as_view(), name='brand'),
    path('generation', views.CreateGenerationView.as_view(), name='generation'),
    path('specification', views.CreateSpecificationView.as_view(), name='specification'),   
    

    
    path('home', views.HomeView.as_view()),
    # path('course/<int:courseid>', views.courseDetails),
]





