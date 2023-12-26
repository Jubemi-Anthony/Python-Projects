def calculateInterest(principal,rate,time, YRorMT):
    if YRorMT != 'year' and YRorMT != 'month':
        print('Please try again and enter either "Month" or "Year" for the time period!')
    TIME = float(time)
    if YRorMT == 'month':
        TIME = TIME/12

    RATE = float(rate)
    PRINCIPAL = float(principal)
    simpleInterest = (PRINCIPAL*RATE*TIME)/100

    print(f"""
        Your Interest is: {simpleInterest} to be paid per annum.
        This would mean you'll have to pay {simpleInterest/12} monthly.
        Thank you!
    """)

principal = input('What is the principal amount?: ')
rate = input('What is the interest rate?: ')
YRorMT = input('Is the interest for years or months? Enter Year or Month: ')
YRorMT = YRorMT.lower()
time = input('What is the time?: ')

calculateInterest(principal,rate,time,YRorMT)