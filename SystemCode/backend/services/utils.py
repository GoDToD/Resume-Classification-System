from pypdf import PdfReader
import pickle
from nltk.corpus import stopwords, names
from nltk import word_tokenize, pos_tag, ne_chunk, Tree
import re
import docx

MALE_NAMES = set(names.words('male.txt'))
FEMALE_NAMES = set(names.words('female.txt'))

def extract_gender(text):
    gender_pattern = re.compile(r"\b(Male|Female|Other)\b", re.IGNORECASE)
    gender_match = gender_pattern.search(text)
    result = gender_match.group(0) if gender_match else None
    if result:
        result = result.strip().lower()
    return result

def extract_phone(text):
    phone_pattern = re.compile(r"\+?\d{1,4}[-\s]?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,4}")
    phone_match = phone_pattern.search(text)
    result = phone_match.group(0) if phone_match else None
    if result:
        result = result.strip()
    return result

def extract_email(text):
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    email_match = email_pattern.search(text)
    result = email_match.group(0) if email_match else None
    if result:
        result = result.strip()
    return result

def get_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_docx_text(docx_path):
    doc = docx.Document(docx_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

def get_text(file):
    if file.filename.endswith('.pdf'):
        return get_pdf_text(file)
    elif file.filename.endswith('.docx'):
        return get_docx_text(file)
    else:
        return ''
    

def is_person_name(name):
    # NLTK 名字库匹配
    return name in MALE_NAMES or name in FEMALE_NAMES
#函数：判断提取到的实体是否是技术术语或常见名字

def extract_name(text):
    # Tokenization 和 POS Tagging
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    
    # NER：命名实体识别
    named_entities = ne_chunk(pos_tags)
    
    # 提取 PERSON 实体
    persons = []
    for subtree in named_entities:
        if isinstance(subtree, Tree) and subtree.label() == 'PERSON':
            person_name = " ".join([token for token, pos in subtree.leaves()])
            
            name_parts = person_name.split()  # 拆分成名字和姓
            
            # 检查每个部分是否是 NLTK 名字库中的名字
            valid_name_parts = [part for part in name_parts if is_person_name(part)]
            #print("valid_name",valid_name_parts )
            # 如果至少一个部分匹配 NLTK 名字库，我们认为这是一个有效名字
            if len(valid_name_parts) >= 1:
                persons.append(person_name)
    if len(persons) < 1:
        return '' 
    return persons[0].lstrip().rstrip()

def clean(text):
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

def classify_resume(files : list):
    tfidf = pickle.load(open('models\TfidfVectorizer.pkl', 'rb'))
    model = pickle.load(open('models\KNeighborsClassifier.pkl', 'rb'))
    le = pickle.load(open('models\LabelEncoder.pkl', 'rb'))
    results = []
    for file in files:
        row_data = {}
        text = get_text(file)
        print('Text:',text)

        row_data['name'] = extract_name(text)
        row_data['email'] = extract_email(text)
        row_data['phone'] = extract_phone(text)
        row_data['gender'] = extract_gender(text)
        text = clean(text)
        text = tfidf.transform([text]).toarray()
        result = model.predict(text)
        job_title = le.inverse_transform(result)
        row_data['job_title'] = job_title[0].lstrip().rstrip()

        results.append(row_data)

    return results