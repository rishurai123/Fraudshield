from django.contrib import admin
from django.urls import path,include
from mainApp.views import index_view,transaction_chart,transaction_data,get_payment_count,get_fraud_count,get_safe_payments,get_unsafe_payment_amount,get_user_statistics,get_daily_sales
from mainApp.views import get_geolocation_data,get_transaction_history
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='index'),
    path('chart/', transaction_chart, name='transaction_chart'),
    path('get-payment-count/', get_payment_count, name='get_payment_count'),
    path('get-fraud-count/', get_fraud_count, name='get_fraud_count'),
    path('get-safe-payments/', get_safe_payments, name='get_safe_payments'),
    path('get-unsafe-payment-amount/', get_unsafe_payment_amount, name='get_unsafe_payment_amount'),
    path("get-user-statistics/", get_user_statistics, name="get-user-statistics"),
    path("api/transactions/", transaction_data, name="transaction_data"),
    path("get-daily-sales/", get_daily_sales, name="get_daily_sales"),
    path("get-geolocation-data/", get_geolocation_data, name="get_geolocation_data"),
    path("get-transaction-history/", get_transaction_history, name="get_transaction_history"),


    
]
