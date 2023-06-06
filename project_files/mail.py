import yagmail

def mail(month):
    '''
    Function used to email employer with time report for the month.
    '''
    sender = 'davvabot@gmail.com' # enter sender email
    reciever = 'jacob.ektander@gmail.com' # enter reciever email
    app_password = 'oyqm lxcw dzmt raxk' # enter google app password if gmail is used
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