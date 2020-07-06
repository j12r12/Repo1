from win32com.client import Dispatch
from datetime import date
import datetime
import os

class DownloadAttachment():
    
    """
    Class to download a .csv email attachment to current working directory.
    """

    def __init__(self, date, subject):

        self.outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
        self.inbox = self.outlook.GetDefaultFolder("6")
        self.emails = self.inbox.items
        self.date = date
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.date = self.date.date()
        self.subject = subject
        self.count = 0

    def save_att(self):

        try:
            for i in self.emails:
                if i.Subject == self.subject and i.ReceivedTime.date() == self.date:
                    for att in i.Attachments:
                        self.count +=1
                        att.SaveAsFile(r"{}\\Filename - {}.csv".format(os.getcwd(), self.date))

            if self.count > 0:
                print("Email attachment downloaded successfully to current working directory.")
            else:
                print("Error - No attachment found.")
        except:
            print("Error - Attachment did not download, please check the date or subject passed.")






        


