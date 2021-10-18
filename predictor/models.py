from django.db import models

class Record(models.Model):
    Loan_Id = models.CharField(max_length=100)
    Date = models.DateField()
    Married = models.CharField(max_length=100)
    Graduated = models.CharField(max_length=100)
    Montly_Income = models.IntegerField()
    Loan_Amount =  models.IntegerField()
    Loan_Period = models.IntegerField()
    Credit_Score = models.CharField(max_length=100)
    Loan_status = models.CharField(max_length=100)

    def __str__(self):
        return self.Loan_Id
    