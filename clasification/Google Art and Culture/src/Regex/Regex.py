import re

class Regex():
    def find(self,regex,string,index=0):
        try:
            pattern = re.compile(regex, re.VERBOSE)
            return pattern.findall(string)[index]
        except:
            return None

    def get_integer(self,string):
        return self.find("\d+",string)

    def get_width(self,string):
        if(type(string)!=str):
            return None
        
        is_contain_w = 'w' in string
        
        if(is_contain_w):        
            pattern = (
            "(?<=w)"        #Positive lookbehind of w
            "("
                "\d+.\d+"    #Decimal numbers
                "|\d+"       #Integer numbers
            ")"
            )
            return self.find(pattern,string)
        else:
            pattern = (
            "("
                "\d+.\d+"    #Decimal numbers
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
                "\d+.\d+"    #Decimal numbers
                "|\d+"       #Integer numbers
            ")"
            )
            return self.find(pattern,string)
        else:
            pattern = (
            "("
                "\d+.\d+"    #Decimal numbers
                "|\d+"       #Integer numbers
            ")"
            )
            return self.find(pattern,string,1)
    
    def get_measure(self,string):
        
        if(type(string)!=str):
            return None
        
        return self.find("(cm|mm|in)",string)

