def alert_email(alert_ref,alert_msg):

    """ this module allows you to fire off an alert email specified as follows:
    
    alert_ref='xxxxxxx'
    alert_msg='Your xxxxxx run is complete.'
    alert_email(alert_ref,alert_msg)
    
    but needs an smtp server to function (line 23)"""

    import smtplib
    sender = 'xxxx@xxx.xx.xx'
    receiver = 'xxxx@gmail.com'
    
    message = """From: """+sender+"""
To: """+receiver+"""
Subject: Python Alert: """+alert_ref+"""
    
This is an automatically generated e-mail message:
"""+alert_msg+""" """
    
    try:
    	smtpObj = smtplib.SMTP('smtp.xxx.xx.xx')
	smtpObj.sendmail(sender, receiver, message)         
	print "Successfully sent alert email"
    except SMTPException:
        print "Error: unable to send alert email"
