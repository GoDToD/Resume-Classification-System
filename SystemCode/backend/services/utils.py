from pypdf import PdfReader
import pickle
from nltk.corpus import stopwords
import re

def get_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def clean(text):
    """
    Clean the input text by removing URLs, emails, special characters, and stop words.
    
    :param text: The string to be cleaned
    :return: The cleaned string
    """

    # Compile patterns for URLs and emails to speed up cleaning process
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    
    # Remove URLs
    clean_text = url_pattern.sub('', text)
    
    # Remove emails
    clean_text = email_pattern.sub('', clean_text)
    
    # Remove special characters (keeping only words and whitespace)
    clean_text = re.sub(r'[^\w\s]', '', clean_text)
    
    # Remove stop words by filtering the split words of the text
    stop_words = set(stopwords.words('english'))
    clean_text = ' '.join(word for word in clean_text.split() if word.lower() not in stop_words)
    
    return clean_text

def classify_resume(file):
    text = get_pdf_text(file)
    text = clean(text)
    tfidf = pickle.load(open('models\TfidfVectorizer.pkl', 'rb'))
    text = tfidf.transform([text])
    model = pickle.load(open('models\KNeighborsClassifier.pkl', 'rb'))
    result = model.predict([text])
    print('Result: ',result)

    return ["Software Engineer", "Data Scientist", "Business Analyst"]