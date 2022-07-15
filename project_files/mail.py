import yagmail

def mail(month):
    sender = 'sender@gmail.com' # enter sender email
    reciever = 'reciever@gmail.com' # enter reciever email
    app_password = 'password' # enter google app password if gmail is used
    subject = 'Time report {} [David Vävinggren]'.format(month)
    body = "Hello!\n\nTime report for {} created by davvabot is attached to this email.\n\nBest regards,\n\ndavvabot".format(month)
    attachment = "/Users/davidvavinggren/google_drive/David/programming/python/time_report/project_files/files/{}_report.txt".format(month.lower()) # enter path to file attached
    
    try:
        with yagmail.SMTP(sender, app_password) as yag:
            yag.send(reciever, subject, body, attachment)
            print('\nEmail sent successfully.')
    except:
        return False
    return