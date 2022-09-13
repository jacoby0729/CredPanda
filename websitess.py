# 300 to 850

from flask import Flask 
from flask import render_template
from flask import request
app = Flask(__name__)

# define Python user-defined exceptions
class LittleInformation(Exception):
    """Too little information was provided"""
    pass

class ageError(Exception):
    """Age is less than age of retirement"""
    pass

@app.route('/', methods=["POST", "GET"])
def home():
  hi = False
  
  if request.method == "POST":
    hi = True
  if hi == True:
    x = creditScoreCalculator()
    class hello:
      y = x
    return render_template("calc.html", creditCalc=hello.y)
  else:
  	return render_template('calc.html', creditCalc=hello.y)

def creditScoreCalculator():
  # Variables obtained from HTML
  loan = bool((request.form['credit']))
  loanYears = float(1.1)
  creditNum = float(2)
  missedPaymentDate = float(request.form['paymentMissing'])
  creditLimit = float(3)
  creditBal = float(2)
  negEvent = bool((request.form['negativeEvent']))
  negEventDate = float(request.form['negativeDate'])
  
  creditScore = 725
  errors = 0
  
  try:
    if loan == False:
      raise LittleInformation()

    if 0<loanYears<10:
      creditScore += (loanYears*60/10)
    if loanYears>10:
      creditScore += 60
    # Max = 785, Min = 725

    if creditNum>9:
      creditScore -= 9*(50/9)
    if 0<=creditNum<=9:
      creditScore -= creditNum*(50/9)

    # Max = 785, Min = 675

    if 0<missedPaymentDate<0.25:
      errors += 220
    if 0.25<missedPaymentDate<0.5:
      errors += 176
    if 0.5<missedPaymentDate<1:
      errors += 132
    if 1<missedPaymentDate<2:
      errors += 88
    if missedPaymentDate>2:
      errors += 44

    # Max = 785, Min = 455

    if creditLimit > 0 and creditBal == 0:
      creditScore += 40
    if creditLimit > 0 and creditBal > 0:
      if (creditLimit*130/4)/creditBal > 170:
        creditScore += 40
      else:
        creditScore += (creditLimit*130/4)/creditBal - 130

    # Max = 825, Min = 325

    if negEvent == True:
      if 0<negEventDate<0.25:
        errors += 220
      if 0.25<negEventDate<0.5:
        errors += 200
      if 0.5<negEventDate<1:
        errors += 140
      if 1<negEventDate<2:
        errors += 120
      if 2<negEventDate<3:
        errors += 120
      if 3<negEventDate<4:
        errors += 100
      if 4<negEventDate<5:
        errors += 100
      if 5<negEventDate<6:
        errors += 80
      if 6<negEventDate<7:
        errors += 60
      if 7<negEventDate<8:
        errors += 40
      if negEventDate>8:
        errors += 20

    # Max = 825, Min = 325

    # Correcting error number
    if errors > 220:
      errors = 220
    creditScore -= errors
    creditScore = int(creditScore)
    return creditScore
    
  except LittleInformation:
    print('We do not have enough information to determine your credit score. Try again.')
  except: 
  	print('Invalid input. Try again.')


""" @app.route('/401-k')
def calc401k():
  contributionPercent = float(request.form[])/100
  salary = float(request.form[])
  salaryIncrease = float(request.form[])/100
  age = float(request.form[])
  ageRetire = float(request.form[])
  bal401k = float(request.form[])
  returnRate = float(request.form[])/100
  employerMatch = float(request.form[])/100
  matchEnds = float(request.form[])/100
  
  employeeContributions = 0
  employerContributions = 0
  total = 0
  try: 
    if ageRetire<=age:
      raise ageError()
    years = ageRetire-age
    
    tempSalary = salary
    temp401k = bal401k
    tempEmployee = 0
    tempEmployer = 0
    for i in range(int(years)):
        tempSalary = tempSalary*(1+salaryIncrease)
        tempEmployee = tempSalary*contributionPercent
				
        if (tempSalary*employerMatch*matchEnds) < (tempSalary*matchEnds):
            tempEmployer = tempSalary*employerMatch*matchEnds
        else:
            tempEmployer = tempSalary*matchEnds
        print(tempSalary+matchEnds)
        employeeContributions += tempEmployee
        employerContributions += tempEmployer
				
        temp401k += ((temp401k*returnRate) + tempEmployee + tempEmployer)
        
    total = temp401k
    print("Your 401(k) at retirement will be", total)
    return total
    
  except ageError:
    	print('Age is less than age of retirement.')
  except: 
    	print('Invalid input. Try again.') """
    
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:08:06 2022

@author: rsree
"""
""" 
class InvalidInterest(Exception):
    ""Invalid Interest Rate""

@app.route('/student-debt')
def StudentDebtCalculator():
    income = int(input("You expected income upon graduation: "))
    loan = int(input("Total loan amount: "))
    time = int(input("Payment Period in months: "))
    interest = float(input("Annual Interest Rate (%): "))/100+1
    print(interest)
    try:
        if interest<1:
            raise InvalidInterest()
        totalExpense = 0
        totalIncome = 0
        if income <= 9950:
            tax = .1
        elif income > 9950:
            tax = .12
        elif income > 40525:
            tax = .22
        elif income > 86375:
            tax = .24
        elif income > 164925:
            tax = .32
        elif income > 209425:
            tax = .35
        else:
            tax = .37
        incomePostTax = income*(1-tax)
        years = time//12
        months = time % 12
        tempLoan = loan
        amtPaid = loan/(time)
        print(amtPaid, " vs ", 25000/24)
        for i in range(years):
            amtPaid *= interest
            totalIncome += incomePostTax
            totalExpense += amtPaid*12
            tempLoan -=(amtPaid)*12
        if months != 0:
            amtPaid *= interest
            for i in range(months):
                totalIncome += incomePostTax/12
                totalExpense += (amtPaid*interest)
        diff =totalIncome-totalExpense
        print(diff)
        print(diff/totalIncome)
    
    except(InvalidInterest):
        print("Invalid interest rate, please try again.")
    except:
        print("Invalid input, please try again.")

StudentDebtCalculator()      
      

if __name__ == '__main__':
   app.run(debug = True)
     """

    

    
    
    
    
    


