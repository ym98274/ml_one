from  django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from . import ml_calc

def home(request):
   return render( request, 'index.html')

@csrf_exempt
def result(request):
    Customer_Age = int(request.GET["Customer_Age"])
    Gender_result = request.GET["Gender"]

    if Gender_result == 'Male' :
       Gender = 0
    else:
       Gender = 1

    Dependent_count = int(request.GET["Dependent_count"])
    Education_Level_result = request.GET["Education_Level"]
    if Education_Level_result == 'Graduate':
       Education_Level = 0
    elif Education_Level_result == 'High School':
       Education_Level = 1
    elif Education_Level_result == 'Unknown':
       Education_Level = 2
    elif Education_Level_result == 'Uneducated':
       Education_Level = 3
    elif Education_Level_result == 'College':
       Education_Level = 4
    elif Education_Level_result == 'Post-Graduate':
       Education_Level = 5
    elif Education_Level_result == 'Doctorate':
       Education_Level = 6

    Marital_Status_result = request.GET["Marital_Status"]
    if Marital_Status_result == 'Married':
       Marital_Status = 0
    elif Marital_Status_result == 'Single':
       Marital_Status = 1
    elif Marital_Status_result == 'Unknown':
       Marital_Status = 2
    elif Marital_Status_result == 'Divorced':
       Marital_Status = 3


    Income_Category_result = int(request.GET["Income_Category"])
    if Income_Category_result < 40000 :
       Income_Category = 0
    elif Income_Category_result == 40000 or Income_Category_result <= 60000 :
       Income_Category = 1
    elif Income_Category_result > 80000 or Income_Category_result <= 120000:
       Income_Category = 2
    elif Income_Category_result > 60000 or Income_Category_result <= 80000:
       Income_Category = 3
    elif Income_Category_result == 'Unknown':
       Income_Category = 4
    elif Income_Category_result > 120000:
       Income_Category = 5



    Card_Category_result = request.GET["Card_Category"]
    if Card_Category_result == 'Blue':
       Card_Category = 0
    elif Card_Category_result == 'Silver':
       Card_Category = 1
    elif Card_Category_result == 'Gold':
       Card_Category = 2
    elif Card_Category_result == 'Platinum':
       Card_Category = 3

    Months_on_book = int(request.GET["Months_on_book"])
    Total_Relationship_Count = int(request.GET["Total_Relationship_Count"])
    Months_Inactive_12_mon = int(request.GET["Months_Inactive_12_mon"])
    Contacts_Count_12_mon = int(request.GET["Contacts_Count_12_mon"])
    Credit_Limit = int(request.GET["Credit_Limit"])
    Total_Revolving_Bal = int(request.GET["Total_Revolving_Bal"])
    Total_Amt_Chng_Q4_Q1 = int(request.GET["Total_Amt_Chng_Q4_Q1"])
    Total_Trans_Amt = int(request.GET["Total_Trans_Amt"])
    Total_Trans_Ct = int(request.GET["Total_Trans_Ct"])
    Total_Ct_Chng_Q4_Q1 = int(request.GET["Total_Ct_Chng_Q4_Q1"])
    prediction = ml_calc.bank_switch_function(Customer_Age,Gender,Dependent_count,Education_Level,Marital_Status,Income_Category,Card_Category,Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1)
    return render( request, 'result.html', {'prediction':prediction})

    

