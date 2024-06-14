from django.contrib import admin
from django.urls import path
from myapp.views import UserLoginAPIView, GerenteAPIView, ClienteAPIView, VendedorAPIView
from myapp.views_produto import   produto_get_by_id, produto_list, produto_create, produto_update, produto_delete
from myapp.logout import LogoutView
#from myapp.views_cliente import cliente_create, cliente_list
from myapp.tests import cliente_list_create, cliente_detail, cliente_create, cliente_update
from myapp.reset_password import PasswordResetRequest, PasswordReset

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('reset-password/', PasswordResetRequest.as_view(), name='reset_password_request'),
    path('reset-password/confirm/', PasswordReset.as_view(), name='password_reset_confirm'),

    path('gerente/', GerenteAPIView.as_view(), name='gerente'),
    path('cliente/', ClienteAPIView.as_view(), name='cliente'),
    path('vendedor/', VendedorAPIView.as_view(), name='vendedor'),

    path('produtos/',produto_list, name='produtos' ),
    path('produtos/<int:pk>/', produto_get_by_id, name='produto'),
    path('produto/',produto_create, name='produto_create' ),
    path('produto_delete/<int:pk>',produto_delete, name='produto_delete' ),
    path('produto_update/<int:pk>',produto_update, name='produto_update' ),

    path('cliente/detail/<int:pk>', cliente_detail, name='cliente'),
    path('clientes/', cliente_list_create, name='clientes'),
    path('cliente/create/', cliente_create, name='create'),
    path('cliente/update/<int:pk>', cliente_update, name='update'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

