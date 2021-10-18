from django.shortcuts import render, HttpResponse
from datetime import datetime
from predictor.models import Record
from django.contrib import messages

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Create your views here.
def main(request):
    return render(request, 'main.html')

def index1(request) :
    if request.GET :
        dict = request.GET
        data = list(dict.values())
        try:
            test = [np.array(data, dtype='float64')]
            
            df = pd.read_csv('predictor/loan.csv')
            x=df[['Married','Education','ApplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History']].values
            y=df['Loan_Status'].values

            model = LogisticRegression()
            model.fit(x, y)
            LogisticRegression()


            prediction = model.predict(test)
            approval = int(prediction[0])

            if approval == 0 :
                text = 'Your Loan cannot be approved'
            elif approval == 1 :
                text = 'Your Loan can be approved'

            context = {
                'variable':text
            }
            return render(request, 'index1.html', context)
        except:
            context = {
                'variable':"Please fill all entries"
            }
            return render(request, 'index1.html', context)
    else :
        return render(request, 'index1.html')

def index2(request) :
    if request.GET :
        dict = request.GET

        loanid = dict.get('loanid')
        married = dict.get('bol')
        graduated = dict.get('binary')
        income = dict.get('income')
        amount = dict.get('loanamount')
        period = dict.get('period')
        score = dict.get('range')
        

        data = list(dict.values())
        data = data[1:]
        try:
            test = [np.array(data, dtype='float64')]

            df = pd.read_csv('predictor/loan.csv')
            x=df[['Married','Education','ApplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History']].values
            y=df['Loan_Status'].values

            model = LogisticRegression()
            model.fit(x, y)
            LogisticRegression()

            prediction = model.predict(test)
            approval = int(prediction[0])
            text = " "
            if approval == 0 :
                text = "The person's loan request cannot be approved"
            elif approval == 1 :
                text = "The person's loan request can be approved"
            
            status = text
            
            record = Record(Loan_Id=loanid, Date = datetime.today(), Married=married, Graduated=graduated, Montly_Income = income, Loan_Amount=amount, Loan_Period=period, Credit_Score=score, Loan_status=status)
            record.save()
        
            context = {
                'variable':text
            }
                
            messages.success(request, 'Your record has been saved!')
            return render(request, 'index2.html', context)
        except:
            context = {
                'variable':"Please fill all entries"
            }
            return render(request, 'index2.html', context)
    else :
        return render(request, 'index2.html')

