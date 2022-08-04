import re

class Regex():
    def find(self,regex,string):
        try:
            pattern = re.compile(regex, re.VERBOSE)
            return pattern.findall(string)[0]
        except:
            return None

    def get_integer(self,string):
        return self.find("\d+",string)

    def get_width(self,string):
        pattern = (
        "(?<=w)"        #Positive lookbehind of w
        "("
            "\d+.\d+"    #Decimal numbers
            "|\d+"       #Integer numbers
        ")"
        )
        return self.find(pattern,string)
    
    def get_height(self,string):
        pattern = (
        "(?<=h)"         #Positive lookbehind of h
        "("
            "\d+.\d+"    #Decimal numbers
            "|\d+"       #Integer numbers
        ")"
        )
        return self.find(pattern,string)
    
    def get_measure(self,string):
        return self.find("(cm|mm|in)",string)

