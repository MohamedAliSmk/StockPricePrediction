import pandas as pd 
import requests
import datetime
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

class RealTimePrice:


    def __init__(self) -> None:
        None
        
        
    def web_content_div1(self, web_content,class_path):
        self.web_content_div = self.web_content.find_all('div', {'class':class_path})
        try:
            self.spans = self.web_content_div[0].find_all('fin-streamer')
            self.texts = [self.span.get_text() for self.span in self.spans]
        except IndexError:
            print('IndexError')
            self.texts= []
        return self.texts

    def real_time_price(self,Stock_symbol):
        url='https://finance.yahoo.com/quote/' + Stock_symbol +'?p='+ Stock_symbol+ '&.tsrc=fin-srch'
        try:
            self.r = requests.get(url)
            self.web_content = BeautifulSoup(self.r.text,'lxml')        
            self.texts =self.web_content_div(self.web_content,'My(6px)')
            if self.texts !=[]:
                self.price,self.change= self.texts[0],self.texts[1]
            else:
                self.price,self.change=  [] , []

        except ConnectionError:
            print('ConnectionError')
            self.price, self.change= [], []

        return self.price, self.change








