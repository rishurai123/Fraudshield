from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaction
import plotly.express as px
import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.utils.timezone import datetime, timedelta
from .models import Transaction
from collections import Counter



def index_view(request):
    return render(request, 'index.html')


def transaction_data(request):
    transactions = Transaction.objects.all().values()
    return JsonResponse(list(transactions), safe=False)

def transaction_chart(request):
    transactions = Transaction.objects.all()
    
    
    df = pd.DataFrame(list(transactions.values()))

    if df.empty:
        return JsonResponse({"error": "No data available"}, status=400)
    
   
    fig = px.bar(df, x='user_id', y='amount', color='is_fraudulent', 
                 hover_data=['transaction_type', 'merchant', 'location'],
                 title="Transaction Amount by User")
    
    chart_html = fig.to_html(full_html=False)
    
    return render(request, 'chart.html', {'chart': chart_html})

client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]
collection = db["transactions"]

def update_transaction(request):
    if request.method == "POST":
        try:
            transaction_id = request.POST.get("transaction_id")  
            new_amount = float(request.POST.get("amount", 0))  
            new_fraud_status = request.POST.get("is_fraudulent", "false").lower() == "true"  

          
            filter_query = {"_id": ObjectId(transaction_id)}
            update_data = {"$set": {"amount": new_amount, "is_fraudulent": new_fraud_status}}

      
            result = collection.update_one(filter_query, update_data)

            if result.modified_count > 0:
                return JsonResponse({"message": "Transaction updated successfully!"})
            else:
                return JsonResponse({"message": "No changes made or transaction not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Invalid request method"}, status=405)


def get_payment_count(request):
    try:
        payment_count = collection.count_documents({"transaction_type": "payment"})
        return JsonResponse({"payment_count": payment_count})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def get_fraud_count(request):
    try:
        fraud_count = collection.count_documents({"is_fraudulent": True})
        return JsonResponse({"fraud_count": fraud_count})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def get_safe_payments(request):
    try:
        safe_transactions = collection.aggregate([
            {"$match": {"is_fraudulent": False}},  
            {"$group": {"_id": None, "total_safe_amount": {"$sum": "$amount"}}}
        ])
        total_safe_amount = next(safe_transactions, {}).get("total_safe_amount", 0)
        return JsonResponse({"safe_payment_total": total_safe_amount})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def get_unsafe_payment_amount(request):
    try:
        unsafe_transactions = collection.aggregate([
            {"$match": {"is_fraudulent": True}}, 
            {"$group": {"_id": None, "total_unsafe_amount": {"$sum": "$amount"}}}
        ])
        total_unsafe_amount = next(unsafe_transactions, {}).get("total_unsafe_amount", 0)
        return JsonResponse({"unsafe_payment_amount": total_unsafe_amount})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def get_user_statistics(request):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["your_database"]
    collection = db["transactions"]

    fraud_transactions = collection.count_documents({"is_fraudulent": True})
    safe_transactions = collection.count_documents({"is_fraudulent": False})

    fraud_amount = collection.aggregate([
        {"$match": {"is_fraudulent": True}},
        {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ])

    safe_amount = collection.aggregate([
        {"$match": {"is_fraudulent": False}},
        {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ])

    fraud_amount = next(fraud_amount, {"total": 0})["total"]
    safe_amount = next(safe_amount, {"total": 0})["total"]

    return JsonResponse({
        "fraud_count": fraud_transactions,
        "safe_count": safe_transactions,
        "fraud_amount": fraud_amount,
        "safe_amount": safe_amount
    })

def get_daily_sales(request):
    today = datetime.today().date()
    last_7_days = today - timedelta(days=7)  

    transactions = (
        Transaction.objects.filter(time__gte=last_7_days)
        .values("time", "amount")
    )

    sales_data = {}

    for transaction in transactions:
        date = transaction["time"].date().strftime("%Y-%m-%d")  
        amount = transaction["amount"]

        if date in sales_data:
            sales_data[date] += amount
        else:
            sales_data[date] = amount

    sales_list = [{"date": k, "amount": v} for k, v in sorted(sales_data.items())]

    return JsonResponse({"sales": sales_list})

def get_daily_sales(request):
    """Fetch daily sales data from MongoDB"""
    today = datetime.today()
    start_date = today - timedelta(days=7) 

    transactions = Transaction.objects.filter(time__gte=start_date)

    sales_data = {}
    for txn in transactions:
        date_str = txn.time.strftime('%Y-%m-%d')
        sales_data[date_str] = sales_data.get(date_str, 0) + txn.amount

    sales_list = [{"date": date, "amount": amount} for date, amount in sales_data.items()]

    return JsonResponse({"sales": sales_list}, safe=False)

def get_geolocation_data(request):
    """Fetch top 8 locations from transaction data"""
    transactions = Transaction.objects.values_list("location", flat=True)
   
    location_counts = Counter(transactions)

    top_locations = location_counts.most_common(8)

    data = [{"location": loc, "count": count} for loc, count in top_locations]

    return JsonResponse({"locations": data})


def get_transaction_history(request):
    """Fetch the latest transactions from MongoDB"""
    transactions = Transaction.objects.order_by("-time")[:10]  
    data = [
        {
            "transaction_id": txn.transaction_id,
            "user_id": txn.user_id,
            "amount": f"${txn.amount:.2f}",
            "transaction_type": txn.transaction_type.capitalize(),
            "merchant": txn.merchant,
            "time": txn.time.strftime("%b %d, %Y, %I:%M%p"),
            "location": txn.location,
            "is_fraudulent": txn.is_fraudulent,
        }
        for txn in transactions
    ]
    
    return JsonResponse({"transactions": data})