import re

class Regex():
    def find(self,regex,string,index=0):
        try:
            pattern = re.compile(regex, re.VERBOSE)
            return pattern.findall(string)[index]
        except:
            return None
        
    def is_match(self,regex, text):
        pattern = re.compile(regex)
        return pattern.search(text) is not None

    def get_date(self,string):
        if(type(string)!=str):
            return None
        
        try:            
            date = self.find("\d{4,}",string)
            
            # look for date, if contains more than 4 digits
            if(date):
                return int(date)
            
            # look for date, but match only if followed by th
            pattern = (
            "\d+"        #Positive lookbehind of w
            "("
                "?=th"    #lookahead of th
            ")"
            )
            if self.is_match(pattern,string):
                century = self.find(pattern,string)
                return int(century)*100-100
            
            return None
        except:
            return None
        
    def get_country(self,string):
        if(type(string)!=str):
            return None
        sep = string.split(',')
        return sep[-1]
        

    def get_width(self,string):
        if(type(string)!=str):
            return None
        
        is_contain_w = 'w' in string
        
        if(is_contain_w):        
            pattern = (
            "(?<=w)"        #Positive lookbehind of w
            "("
                "\d+,\d+"    #Decimal numbers with comma(,) separator
                "|\d+\.\d+"  #Decimal numbers with dot(.) separator
                "|\d+"       #Integer numbers
            ")"
            )
            return self.find(pattern,string)
        else:
            pattern = (
            "("
                "\d+,\d+"    #Decimal numbers with comma(,) separator
                "|\d+\.\d+"  #Decimal numbers with dot(.) separator
                "|\d+"       #Integer numbers
            ")"
            )
            return self.find(pattern,string)
    
    def get_height(self,string):
        if(type(string)!=str):
            return None
        
        is_contain_h = 'h' in string
        
        if(is_contain_h):        
            pattern = (
            "(?<=h)"        #Positive lookbehind of h
            "("
                "\d+,\d+"    #Decimal numbers with comma(,) separator
                "|\d+\.\d+"  #Decimal numbers with dot(.) separator
                "|\d+"       #Integer numbers
            ")"
            )
            return self.find(pattern,string)
        else:
            pattern = (
            "("
                "\d+,\d+"    #Decimal numbers with comma(,) separator
                "|\d+\.\d+"  #Decimal numbers with dot(.) separator
                "|\d+"       #Integer numbers
            ")"
            )
            return self.find(pattern,string,1)
    
    def get_measure(self,string):
        
        if(type(string)!=str):
            return None
        
        return self.find("(cm|mm|in)",string)

