from django.urls import path
from cars import views
# from cars.views import moter
#from cars.views import register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('/m', moter),
    path('', views.reg, name='reg'),
    path('table', views.datashow, name='datashow'),
    path('del_data/<int:id>/', views.deletedata, name='del_data'),
    path('edititem/<int:id>/', views.editdata, name='edititem'),
    path('showalldata', views.showalldata, name='showalldata'),
    path('datatble', views.datatble, name='datatble'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('adddata', views.add_data, name='adddata'),
    path('update_data', views.update_data, name='update_data'),
    path('delete_user', views.delete_user, name='delete_user'),
    path('tinymce_prac', views.tinymce_prac, name='tinymce_prac'),
    path('export-csv', views.export_csv, name='export-csv'),
    path('export-excel', views.export_excel, name='export-excel'),
    path('export-pdf', views.export_pdf, name='export-pdf'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)