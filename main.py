import qrcode
upi_id=input("Enter your UPI ID = ")
#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=message


phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#make qr code for every payment app

phonepe_qr= qrcode.make(phonepe_url)
paytm_qr= qrcode.make(paytm_url)
google_pay_qr= qrcode.make(google_pay_url)

#display the qr code by using pillow library

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()



