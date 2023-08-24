from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from penjualan_app import views
from .views import CustomerViewSet, PetugasViewSet, BarangViewSet, TransaksiViewSet, api_root
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# router = DefaultRouter()
# router.register(r'customers', CustomerViewSet)
# router.register(r'pegawai', PetugasViewSet)
# router.register(r'barang', BarangViewSet)
# router.register(r'transaksi', TransaksiViewSet)

# urlpatterns = [
#   path('', include(router.urls)),
# ]

customer_list = CustomerViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
customer_detail = CustomerViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'
})

# Petugas URLs
petugas_list = PetugasViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
petugas_detail = PetugasViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'
})

# Barang URLs
barang_list = BarangViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
barang_detail = BarangViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'
})

# Transaksi URLs
transaksi_list = TransaksiViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
transaksi_detail = TransaksiViewSet.as_view({
  'get': 'retrieve',
  'put': 'update',
  'patch': 'partial_update',
  'delete': 'destroy'
})

# URL eksplisit untuk setiap ViewSet
urlpatterns = format_suffix_patterns ([
  path('', views.api_root),
  path('customers/', customer_list, name='customer-list'),
  path('customers/<int:pk>/', customer_detail, name='customer-detail'),
  path('pegawai/', petugas_list, name='petugas-list'),
  path('pegawai/<int:pk>/', petugas_detail, name='petugas-detail'),
  path('barang/', barang_list, name='barang-list'),
  path('barang/<int:pk>/', barang_detail, name='barang-detail'),
  path('transaksi/', transaksi_list, name='transaksi-list'),
  path('transaksi/<int:pk>/', transaksi_detail, name='transaksi-detail'),
  
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
])