import re
class Regex():
    def find(self,regex,string):
        try:
            return re.findall(regex, string)[0]
        except:
            return None

    def get_digit(self,string):
        return self.find("\d+",string)

