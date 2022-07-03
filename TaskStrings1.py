#2. Try to reverese string without using reverse function

import logging
logging.basicConfig(filename="taskstring1.txt", level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

class ReverseString:

    def reverseStr(self,strToReverse):
      try:
         return strToReverse[::-1]
      except Exception as e:
          logging.error(e)

    def splitStrAfterConversion(self,stringToSplit):
        try:
            return(stringToSplit.upper().split(" "))
        except Exception as e:
            logging.error(e)

    def StringToLower(self,StrToLower):
        try:
            return(StrToLower.lower())
        except Exception as e:
            logging.error(e)

    def StringToCapitalise(self, CapitaliseString):
        try:
            return(CapitaliseString.capitalize())
        except Exception as e:
            logging.error(e)

    def EgForExpandtabs(self, EgString):
        try:
            return(EgString.expandtabs())
        except Exception as e:
            logging.error(e)

    def StripEgs(self,stringToStrip):
        try:
            logging.info("Strip Example")
            logging.info(stringToStrip.strip())
            logging.info("lstrip() eg")
            logging.info(stringToStrip.lstrip())
            logging.info("rstrip() eg")
            logging.info(stringToStrip.rstrip())
        except Exception as e:
            logging.error(e)


    def replaceStringCharacter(self,stringToReplace):
        try:
            return(stringToReplace.replace('s','p'))
        except Exception as e:
            logging.error(e)

    def CenterFn(self,strToCenter):
        try:
            return(strToCenter.center(20,'#'))
        except Exception as e:
            logging.error(e)


StringAns= ReverseString()
logging.info(StringAns.reverseStr("My OOPS Class began"))

#3. Try to split a string after conversion of entire string in uppercase
logging.info(StringAns.splitStrAfterConversion("My OOPS class began"))

#4. try to convert the whole string into lower case
logging.info(StringAns.StringToLower("My OOPS class began"))

#5 . Try to capitalize the whole string
logging.info(StringAns.StringToCapitalise("my oops class began"))

#6. Example for expandtabs()
logging.info(StringAns.EgForExpandtabs("my\toops\tclass\tbegan"))

#7.Eg for strip(),lstrip(),rstrip()
logging.info(StringAns.StripEgs("  StringToStrip  "))

#8. Replace a string character with another character
logging.info(StringAns.replaceStringCharacter("my oops class began"))

#9. Center() example
logging.info(StringAns.CenterFn("Center"))

