from email.policy import default


def predict_one(loan_amount):
    if loan_amount < 30000:
        prediction = 'Eligible for a loan'
    else: 
       prediction = 'Not Eligible for a loan'
    return prediction

