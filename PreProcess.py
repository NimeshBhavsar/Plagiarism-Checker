import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re

class Preprocess:
    """class Preprocess takes the file name and reads it and starts the preprocess"""
    trig = []
    """ stores the final computed trigrams """
    def __init__(self,filename):
        
        """contructor to initialise the filename and call the respective functions"""
        init_token = self.openFile(filename)
        clean_token = self.clean(init_token)
        trig_list = self.makeTrig(clean_token)
        self.trig = trig_list
         
    def openFile(self,filename):
        """Opens the file and replaces the new line and special character to space
           and tokenizes the data""" 
        f=open(filename,"r")
        orig=f.read().replace("\n"," ")
        orig = re.sub(r'[^\w\s]', '', orig)
        orig = re.sub(r'[0-9]+', '', orig)
        return word_tokenize(orig)

    def clean(self,init_token):
        """ Converts the token into lower case, removes punctuation and stopwords using
            NLTK package"""
        #lowercase
        tokens_o = [token.lower() for token in init_token]
        #stop word removal
        #punctuation removal
        stop_words=set(stopwords.words('english'))
        punctuations=['"','.','(',')',',','?',';',':',"''",'``']
        filtered_tokens = [w for w in tokens_o if not w in stop_words and not w in punctuations]
        return filtered_tokens

    def makeTrig(self,clean_token):
        """ Takes the filtered tokens and make trigrams of continuos words"""
        trigrams=[]
        for i in range(len(clean_token)-2):
            t=(clean_token[i],clean_token[i+1],clean_token[i+2])
            trigrams.append(t)
        return trigrams
