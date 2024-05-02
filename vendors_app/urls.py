from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from vendors_app import views

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'),
    path("vendors/",views.VendorCreateListView.as_view(),name="vendors_create_list"),
    path("vendors/<str:vendor_code>/",views.RetrieveUpdateDeleteView.as_view(),name="vendors_update_show_delete"),
    path("purchase_orders/",views.PurchaseOrderCreateListView.as_view(),name="purchase_orders_create_list"),
    path("purchase_orders/<str:po_number>/",views.PurchaseOrderListUpdateDelete.as_view(),name="purchase_orders_update_show_delete"),
    path("vendors/<str:vendor_code>/performance",views.VendorPerformanceView.as_view(),name="vendor_performance"),
    path('purchase_orders/<str:po_id>/acknowledge',views.AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),

]