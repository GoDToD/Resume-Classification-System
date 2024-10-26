from pypdf import PdfReader
import pickle
from nltk.corpus import stopwords, names
from nltk import word_tokenize, pos_tag, ne_chunk, Tree
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import docx
import numpy as np

MALE_NAMES = set(names.words('male.txt'))
FEMALE_NAMES = set(names.words('female.txt'))
key_words_set = {
    "Web Designing": ["html", "css", "javascript", "responsive design", "ui/ux", "bootstrap", "adobe xd", "figma", "photoshop", "user interface", "user experience", "front-end", "jquery", "wireframing", "prototyping", "web graphics"],
    "Arts": ["creative arts", "visual arts", "illustration", "painting", "adobe creative suite", "design", "photoshop", "sculpture", "fine arts", "exhibitions", "animation", "graphic design", "portfolio", "concept art", "studio art", "mixed media"],
    "Advocate": ["law", "legal research", "litigation", "contract law", "court proceedings", "client counseling", "case analysis", "legal documentation", "trial preparation", "legal compliance", "dispute resolution", "intellectual property", "criminal law", "civil law", "corporate law", "legal advice", "advocacy"],
    "HR": ["recruitment", "onboarding", "employee relations", "payroll", "talent acquisition", "hr policies", "benefits administration", "performance management", "employee engagement", "hr software", "compliance", "training", "interviewing"],
    "Data Science": ["python","spicy","keras:","sklearn", "r", "machine learning", "data analysis", "statistics", "deep learning", "sql", "pandas", "numpy", "scikit-learn", "tensorflow", "data visualization", "data wrangling", "big data", "tableau", "power bi"],
    "Testing": ["test cases", "qa", "selenium", "manual testing", "automation testing", "regression testing", "junit", "postman", "bug tracking", "jenkins", "test scripts", "unit testing", "integration testing"],
    "Blockchain": ["blockchain", "ethereum", "smart contracts", "solidity", "cryptocurrency", "distributed ledger", "hyperledger", "consensus mechanisms", "wallet", "dapp", "bitcoin", "decentralized applications", "blockchain protocols", "nft"],
    "DotNet Developer": ["c#", ".net", "asp.net", "mvc", "sql server", "entity framework", "linq", "visual studio", "web api", "restful services", "javascript", "json", "angular"],
    "ETL Developer": ["etl", "data pipelines", "data transformation", "sql", "data warehouse", "informatica", "talend", "ssis", "airflow", "big data", "hadoop", "data migration", "oracle", "data integration", "pl/sql"],
    "Hadoop": ["hadoop", "hdfs", "mapreduce", "yarn", "hive", "pig", "spark", "cloudera", "data lake", "data pipelines", "big data", "flume", "zookeeper", "oozie"],
    "Database": ["database management", "sql", "oracle", "postgresql", "nosql", "mongodb", "data modeling", "pl/sql", "data warehousing", "query optimization", "etl", "indexing", "data backup"],
    "PMO": ["project management", "pmo", "stakeholder management", "resource planning", "project lifecycle", "risk management", "budgeting", "kpis", "agile", "scrum", "change management", "scope management", "reporting", "milestone planning"],
    "Network Security Engineer": ["network security", "firewall", "vpn", "ids", "ips", "tcp/ip", "encryption", "penetration testing", "malware analysis", "cybersecurity", "cisco", "fortinet", "threat management", "vulnerability assessment", "compliance"],
    "DevOps Engineer": ["devops", "ci/cd", "jenkins", "docker", "kubernetes", "aws", "azure", "terraform", "ansible", "linux", "scripting", "nagios", "monitoring", "automation"],
    "Python Developer": ["python", "django", "flask", "pandas", "numpy", "sql", "restful api", "docker", "fastapi", "oop", "data manipulation", "scikit-learn", "tensorflow"],
    "Operations Manager": ["operations management", "process improvement", "supply chain", "logistics", "kpis", "project management", "inventory control", "vendor management", "workforce management", "cost management", "operational efficiency", "scheduling", "lean manufacturing", "budgeting", "resource allocation", "risk management"],
    "Electrical Engineering": ["circuit design", "power systems", "embedded systems", "pcb design", "microcontrollers", "signal processing", "analog circuits", "digital circuits", "matlab", "control systems", "hvac", "power distribution", "transformers", "plc programming"],
    "Automation Testing": ["automation", "selenium", "junit", "pytest", "test scripts", "test automation", "jenkins", "api testing", "performance testing", "regression testing", "cucumber", "manual testing", "bug tracking", "integration testing"],
    "SAP Developer": ["sap", "abap", "sap hana", "sap fico", "sap mm", "sap sd", "bapi", "idoc", "workflow", "odata", "sap ecc", "s/4hana", "fiori"],
    "Business Analyst": ["business analysis", "data analysis", "sql", "requirements gathering", "stakeholder management", "data visualization", "tableau", "power bi", "financial modeling", "reporting", "dashboarding", "business strategy", "kpis", "gap analysis", "trend analysis"],
    "Java Developer": ["java", "spring", "hibernate", "j2ee", "microservices", "sql", "mysql", "restful api", "junit", "oop", "design patterns", "maven", "docker", "spring boot"],
    "Civil Engineer": ["civil engineering", "autocad", "construction management", "structural analysis", "surveying", "project management", "blueprints", "revit", "concrete", "road design", "hydrology", "building codes", "material testing"],
    "Health and Fitness": ["fitness training", "personal training", "nutrition", "strength training", "aerobics", "sports science", "rehabilitation", "weight loss", "physical therapy", "yoga", "endurance training", "injury prevention", "health coaching", "mental health"],
    "Sales": ["sales", "crm", "lead generation", "b2b", "b2c", "salesforce", "pipeline management", "account management", "upselling", "negotiation", "forecasting", "sales strategies"],
    "Mechanical Engineer": ["mechanical design", "cad", "solidworks", "catia", "fea", "ansys", "thermodynamics", "manufacturing", "prototyping", "hvac", "tolerance analysis", "machining", "3d modeling", "materials engineering"]
}
key_words = set()
for words_list in key_words_set.values():
    key_words.update(words_list)

stop_words = set(stopwords.words('english'))

def clean_text(text,stop_words):
    # 去除数字
    text = re.sub(r'\d+', '', text)
    # 去除标点符号
    text = re.sub(r'[^\w\s]', '', text)
    # 转为小写
    text = text.lower()
    # 去除停用词
    cleaned_text = ' '.join([word for word in text.split() if word not in stop_words])
    return cleaned_text

def get_top_tfidf_keywords(text, selected_words, stop_words, max_features=10):
    """
    计算文本的TF-IDF值，并根据selected_words筛选出高TF-IDF的关键词。
    
    :param text: 输入的文本字符串
    :param selected_words: 感兴趣的词汇集合
    :param stop_words: 停用词列表
    :param max_features: TfidfVectorizer的最大特征数
    :return: 筛选出的高TF-IDF关键词及其对应的分数
    """
    # 清洗文本
    doc = [clean_text(text, stop_words)]  # 清洗并包装为列表
    
    # 初始化TF-IDF向量器
    tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_features=max_features)
    
    # 计算TF-IDF矩阵
    tfidf_matrix = tfidf_vectorizer.fit_transform(doc)
    
    # 获取词汇表和对应的TF-IDF分数
    words = tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray().flatten()

    top_n_indices = np.argsort(tfidf_scores)[::-1]  # 从高到低排序
    seen_phrases = set()  # 用于存储已经处理过的短语，避免重复
    top_words = []
    top_scores = []
    
    for i in top_n_indices:
        word = words[i]
        # 检查是否有短语包含这个 word
        for phrase in selected_words:
            if word in phrase and phrase not in seen_phrases:  # 检查该词是否在某个短语中，并且没有处理过
                top_words.append(phrase)  # 将短语作为匹配
                top_scores.append(tfidf_scores[i])
                seen_phrases.add(phrase)  # 添加到已处理短语集合
                break  # 一旦匹配短语就跳出循环
    
    # 返回筛选出的词和对应分数
    return list(zip(top_words, top_scores))

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

        row_data['name'] = extract_name(text)
        row_data['email'] = extract_email(text)
        row_data['phone'] = extract_phone(text)
        row_data['gender'] = extract_gender(text)
        row_data['key_words'] = get_top_tfidf_keywords(text, key_words, stop_words, max_features=10)    
        text = clean(text)
        text = tfidf.transform([text]).toarray()
        result = model.predict(text)
        job_title = le.inverse_transform(result)
        row_data['job_title'] = job_title[0].lstrip().rstrip()

        results.append(row_data)

    return results