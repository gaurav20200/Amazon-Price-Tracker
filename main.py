import bs4
import smtplib
import urllib.request
import time



def send_email(): #function to send the email to the user when the price of the item is equal or lower to desired price.
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sender's gmail","password")
        message = "The Item which you wanted to buy is now available at your desired price."
        s.sendmail("sender's gmail", "receiver's gmail", message)
        s.quit()




def check_price(): #function to check the price of the item 
   url='https://www.amazon.in/New-Apple-iPhone-11-64GB/dp/B08L8DV7BX/ref=sr_1_3?dchild=1&keywords=iphone&qid=1634129026&sr=8-3'
   response = urllib.request.urlopen(url).read()
   soup = bs4.BeautifulSoup(response,"html.parser")
   price = soup.find(id="priceblock_dealprice").getText()
   price = float(price.replace("₹","").replace(",",""))
   return price


while True:
        price=check_price()
        if(price<=float(40000)):
                print("helloo")
                
                send_email()
        time.sleep(3600)  #to wait for one hour after checking 
