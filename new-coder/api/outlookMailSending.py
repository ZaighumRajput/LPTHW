"""http://stackoverflow.com/questions/6332577/send-outlook-email-via-python"""
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = "zaighum.rajput@nn.nl"
mail.Subject = 'Message subject'
mail.body = 'Message body'
mail.send