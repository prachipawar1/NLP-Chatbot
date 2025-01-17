from flask import Flask, request, jsonify
import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Read and preprocess the data
with open('C:\\Users\\prach\\nlp chatbot\\data.txt', 'r', errors='ignore') as f:
    raw = f.read().lower()

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greetings
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! you are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generate response
def response(user_response):
    chatbot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        chatbot_response = "I am sorry! I don't understand you"
    else:
        chatbot_response = sent_tokens[idx]
    sent_tokens.pop(-1)
    return chatbot_response

@app.route("/")
def home():
    return "Hello, there my name is Aneka. I will answer your queries. If you want to exit, type Bye!"

@app.route("/chat", methods=["POST"])
def chat():
    user_response = request.json.get("message")
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response in ['thanks', 'thank you']:
            return jsonify({"response": "You're welcome!"})
        elif greeting(user_response) is not None:
            return jsonify({"response": greeting(user_response)})
        else:
            return jsonify({"response": response(user_response)})
    else:
        return jsonify({"response": "Bye! Have a great time!"})

if __name__ == "__main__":
    app.run(debug=True)























# from flask import Flask, request, jsonify
# import nltk
# import random
# import string
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# app = Flask(__name__)

# # Read and preprocess the data
# with open('C:\\Users\\shubb\\whatsaap chat\\ml.txt', 'r', errors='ignore') as f:
#     raw = f.read().lower()

# sent_tokens = nltk.sent_tokenize(raw)
# word_tokens = nltk.word_tokenize(raw)

# lemmer = nltk.stem.WordNetLemmatizer()

# def LemTokens(tokens):
#     return [lemmer.lemmatize(token) for token in tokens]

# remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# # Greetings
# GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
# GREETING_RESPONSES = ["hi", "hey", "nods", "hi there", "hello", "I am glad! you are talking to me"]

# def greeting(sentence):
#     for word in sentence.split():
#         if word.lower() in GREETING_INPUTS:
#             return random.choice(GREETING_RESPONSES)

# # Generate response
# def response(user_response):
#     chatbot_response = ''
#     sent_tokens.append(user_response)
#     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
#     tfidf = TfidfVec.fit_transform(sent_tokens)
#     vals = cosine_similarity(tfidf[-1], tfidf)
#     idx = vals.argsort()[0][-2]
#     flat = vals.flatten()
#     flat.sort()
#     req_tfidf = flat[-2]
#     if req_tfidf == 0:
#         chatbot_response = "I am sorry! I don't understand you"
#     else:
#         chatbot_response = sent_tokens[idx]
#     sent_tokens.pop(-1)
    
#     # Adjust the response length to 20-30 words
#     words = chatbot_response.split()
#     if len(words) > 30:
#         chatbot_response = ' '.join(words[:30])
#     elif len(words) < 20:
#         chatbot_response += ' ' + ' '.join(words * (20 // len(words)))  # Extend the response if too short

#     return chatbot_response

# @app.route("/")
# def home():
#     return "Hello, there my name is Aneka. I will answer your queries. If you want to exit, type Bye!"

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_response = request.json.get("message")
#     user_response = user_response.lower()
#     if user_response != 'bye':
#         if user_response in ['thanks', 'thank you']:
#             return jsonify({"response": "You're welcome!"})
#         elif greeting(user_response) is not None:
#             return jsonify({"response": greeting(user_response)})
#         else:
#             return jsonify({"response": response(user_response)})
#     else:
#         return jsonify({"response": "Bye! Have a great time!"})

# if __name__ == "__main__":
#     app.run(debug=True)









# from flask import Flask, request, jsonify
# import nltk
# import random
# import string
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# app = Flask(__name__)

# # Read and preprocess the data
# with open('C:\\Users\\shubb\\whatsaap chat\\ml.txt', 'r', errors='ignore') as f:
#     raw = f.read().lower()

# sent_tokens = nltk.sent_tokenize(raw)
# word_tokens = nltk.word_tokenize(raw)

# lemmer = nltk.stem.WordNetLemmatizer()

# def LemTokens(tokens):
#     return [lemmer.lemmatize(token) for token in tokens]

# remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# # Greetings
# GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
# GREETING_RESPONSES = ["hi", "hey", "nods", "hi there", "hello", "I am glad! you are talking to me"]

# def greeting(sentence):
#     for word in sentence.split():
#         if word.lower() in GREETING_INPUTS:
#             return random.choice(GREETING_RESPONSES)

# # Generate response
# def response(user_response):
#     chatbot_response = ''
#     sent_tokens.append(user_response)
#     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
#     tfidf = TfidfVec.fit_transform(sent_tokens)
#     vals = cosine_similarity(tfidf[-1], tfidf)
#     idx = vals.argsort()[0][-2]
#     flat = vals.flatten()
#     flat.sort()
#     req_tfidf = flat[-2]
#     if req_tfidf == 0:
#         chatbot_response = "I am sorry! I don't understand you"
#     else:
#         chatbot_response = sent_tokens[idx]
#     sent_tokens.pop(-1)
#     return chatbot_response

# @app.route("/")
# def home():
#     return "Hello, there my name is Aneka. I will answer your queries. If you want to exit, type Bye!"

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_response = request.json.get("message")
#     user_response = user_response.lower()
#     if user_response != 'bye':
#         if user_response in ['thanks', 'thank you']:
#             return jsonify({"response": "You're welcome!"})
#         elif greeting(user_response) is not None:
#             return jsonify({"response": greeting(user_response)})
#         else:
#             return jsonify({"response": response(user_response)})
#     else:
#         return jsonify({"response": "Bye! Have a great time!"})

# if __name__ == "__main__":
#     app.run(debug=True)







