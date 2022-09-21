from typing import List
from .Storage import Storage
from selenium import webdriver
import time

class Scraper:
    """
    Object to scrape the target page
    """
    
    def __init__(self, path:str,color:str):
        """
        Parameters
        ----------
        path : str
            selenium webdriver path
        color : str
            color of the page that contains this color
        """

        self.driver = webdriver.Chrome(executable_path = path)
        self.SCROLL_DOWN = 45
        self.storage = Storage()
        self.color = color
        
    def scraping_data(self)->List[dict]:        
        """Exec webscraping

        Returns
        -------
        List[dict]
            list of dict of webscraped data with shape {url,data,category}
        """
        #Scroll page until the end.
        time.sleep(3)
        self.scroll_down(self.SCROLL_DOWN)
        time.sleep(7)
        
        #Get picture pages and image links
        picture_pages =self.get_pictures_pages()
        picture_links= self.get_pictures_links()
        
        #For each picture, get theirs details.
        for (page,picture_link) in zip(picture_pages,picture_links):
            if(page==None or picture_link==None):
                break          
            #Open picture page ,get and store its information.
            self.driver.get(page)
            time.sleep(0.2)
            details = self.get_picture_details()
            self.storage.add(picture_link,details,self.color) 
        #Return retrival data
        return self.storage.get_data()
    
       
        
    def open(self):
        """Open the page that contains images of color parameter

        Parameters
        ----------
        color : str
            target color
        """
        target_page = f'https://artsandculture.google.com/color?col={self.color}'
        self.driver.get(target_page)
        
    def scroll_down(self,scrolls:int):
        """Scroll the page for load images dynamically

        Parameters
        ----------
        scrolls : int
            number of scroll by execute.
        """ 
        for j in range(0, scrolls):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  
            
    def get_picture_details(self)-> str:
        """Get all details of picture page in json format as string.

        Returns
        -------
        str
            Details of picture page in json as string.
        """        

        
        script = '''
        var details = [...document.querySelector(".ve9nKb").querySelectorAll('li')];
        var museum = document.querySelector(".To7WBf")?.childNodes?.[0]?.textContent;
        var loc = document.querySelector(".WrfKPd")?.textContent;
        var info = details.reduce((acc,item)=>{
            const text = item.textContent;
            const chunks = text.split(':');
            const key = chunks[0];
            const value = chunks.splice(1).join("")
            return {...acc,[key]:value}
        },{})
        info['museum']= museum;
        info['location']= loc;
        return JSON.stringify(info);
        '''
        details = self.driver.execute_script(script)
        return details
     
    def get_pictures_pages(self)->List[str]: 
        """Get all link picture pages

        Returns
        -------
        List[str]
            Each of the image page links in current session
        """  

        script="""
        var containers = [...document.querySelectorAll('.DuHQbc')];
        var img_elements = containers.map(contain => contain.firstElementChild);
        return img_elements.map(a => a.href)
        """

        pages = self.driver.execute_script(script)
        return pages
        
    
    def get_pictures_links(self)->List[str]:
        """Get all pictures link

        Returns
        -------
        List[str]
            Each of the picture link in current session
        """ 
        script = '''
        var containers = [...document.querySelectorAll('.DuHQbc')];
        var img_elements= containers.map(contain => contain.firstElementChild);
        return img_elements.map(a =>window.getComputedStyle(a, false).backgroundImage)
        '''
        urls_raw = self.driver.execute_script(script)
        urls = list(filter(lambda url:url!='none',urls_raw))
        links = list(map(lambda url:url.split('"')[1],urls))
        return links

