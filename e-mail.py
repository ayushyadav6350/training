import smtplib
try:
    server= smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()       # start the server
    recever_email= input("enter your email")
    sender_email='ayushyadav9988776@gmail.com'
    password = 'hecu angy pgnd vpsl'
    server.login(sender_email,password= password)
    subject=input("what is your problem")
    body=input("thoda or detail m btao")
    message= f"subject:{subject}\n\n{body}"
    server.sendmail(sender_email,recever_email,message)
    print("mne mail send kr di h")
    server.quit()
except Exception as e:
    
    print("mail send nhi hue")