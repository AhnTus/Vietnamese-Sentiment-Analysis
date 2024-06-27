from tensorflow.keras.preprocessing.text import Tokenizer 
from keras.preprocessing.sequence import pad_sequences 
from pyvi import ViTokenizer
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import string
import re
class DataPreprocessing:
    def __init__(self,path,path_generate):
        self.x_train,self.y_train=self.ReadData(path) if not None else None
        self.x_train=self.WordSeparation(self.x_train)
        self.x_train=self.CreateCorpus(self.x_train)
        self.labelEn=LabelEncoder()
        self.labelEn.fit_transform(self.y_train)
        self.generate=self.ReadData_ge(path_generate)
        self.generate=self.WordSeparation(self.generate)
        self.generate=self.CreateCorpus(self.generate)
    def fit_transform_generate(self,comment):
        comment=ViTokenizer.tokenize(comment)
        comment=self.generate.texts_to_sequences([comment])
        comment=pad_sequences(comment,maxlen=151,padding='pre')
        return comment
    def remove_repeated_words(self,comment):
        words = comment.split()
        new_words = []
        for i in range(len(words)):
            if i == 0 or words[i] != words[i-1]:
                new_words.append(words[i])
        return ' '.join(new_words)
    def fit_transform(self,comment):
        comment=self.remove_punctuation(comment.lower())
        comment=ViTokenizer.tokenize(comment)
        comment=self.remove_stopword(comment)
        comment=[self.remove_repeated_words(comment)]
        comment=self.WordSeparation(comment)
        comment=self.Padding(comment,131)
        return comment
    def ReadData_ge(self,path):
        df=pd.read_csv(path,encoding='utf-8')
        return df['comment']
    def ReadData(self,path):
        df=pd.read_csv(path,encoding='utf-8')
        return df['comment'], df['label']
    def WordSeparation(self,comment):
        return [review.split() for review in comment]
    def Padding(self,comment,sequence):
        comment=self.x_train.texts_to_sequences(comment)
        comment=pad_sequences(comment,maxlen=sequence,padding='pre')
        return comment
    def CreateCorpus(self,Vi):
        tokenizer=Tokenizer(oov_token='<oov>')
        tokenizer.fit_on_texts(Vi)
        return tokenizer
    def Standardization(self,comment):
        if comment =='Positive':
            return "Đây là một bình luận mang ý nghĩa tích cực "
        elif comment =='Negative':
            return "Đây là một bình luận mang ý nghĩa tiêu cực "
        else:
            return "Đây là một bình luận mang ý nghĩa trung lập"
    def remove_punctuation(self,comment):
        # Create a translation table
        translator = str.maketrans('', '', string.punctuation)
        # Remove punctuation
        new_string = comment.translate(translator)
        # Remove redudant space and break sign
        new_string = re.sub('[\n ]+', ' ', new_string)
        # Remove emoji icon
        emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002500-\U00002BEF"  # chinese char
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u"\U00010000-\U0010ffff"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u200d"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\ufe0f"  # dingbats
                u"\u3030"
                                "]+", flags=re.UNICODE)
        new_string = re.sub(emoji_pattern, '', new_string)

        return new_string
    def read_filestopwords(self):
        with open('./data/data_stopword/vietnamese-stopwords.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            words = [line.split('\n')[0] for line in lines]
        return words
    def remove_stopword(self,comment):
        stop_words =self.read_filestopwords()
        filtered = [word for word in comment.split() if word not in stop_words]
        return ' '.join(filtered)