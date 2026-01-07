"""Main Chatbot Module - Intent Classification and Response Generation"""

import json
import random
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pickle
import os

# Download required NLTK data
for resource in ['punkt', 'wordnet', 'omw-1.4', 'stopwords']:
    try:
        nltk.download(resource, quiet=True)
    except:
        pass

class ChatBot:
    """AI-powered chatbot with NLP capabilities"""
    
    def __init__(self, intents_file='data/intents.json'):
        """Initialize the chatbot with intents and vocabulary"""
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.intents = self.load_intents(intents_file)
        self.vocabulary = set()
        self.build_vocabulary()
        
    def load_intents(self, intents_file):
        """Load intents from JSON file"""
        if os.path.exists(intents_file):
            with open(intents_file, 'r') as f:
                return json.load(f)
        return {"intents": []}
    
    def preprocess_text(self, text):
        """Tokenize and lemmatize input text"""
        tokens = nltk.word_tokenize(text.lower())
        tokens = [
            self.lemmatizer.lemmatize(token) 
            for token in tokens 
            if token.isalnum() and token not in self.stop_words
        ]
        return tokens
    
    def build_vocabulary(self):
        """Build vocabulary from all intents and patterns"""
        for intent in self.intents.get('intents', []):
            for pattern in intent.get('patterns', []):
                tokens = self.preprocess_text(pattern)
                self.vocabulary.update(tokens)
    
    def extract_features(self, user_input):
        """Convert user input to feature vector (Bag of Words)"""
        tokens = self.preprocess_text(user_input)
        features = [1 if word in tokens else 0 for word in self.vocabulary]
        return np.array(features)
    
    def classify_intent(self, user_input):
        """Classify user input to an intent using simple matching"""
        user_tokens = self.preprocess_text(user_input)
        best_intent = None
        max_match = 0
        
        for intent in self.intents.get('intents', []):
            for pattern in intent.get('patterns', []):
                pattern_tokens = self.preprocess_text(pattern)
                matches = len(set(user_tokens) & set(pattern_tokens))
                
                if matches > max_match:
                    max_match = matches
                    best_intent = intent
        
        return best_intent
    
    def generate_response(self, user_input):
        """Generate response based on classified intent"""
        intent = self.classify_intent(user_input)
        
        if intent:
            response = random.choice(intent.get('responses', ['I did not understand that.']))
        else:
            response = "I did not understand that. Can you please rephrase?"
        
        return response
    
    def chat(self, user_input):
        """Process user input and return chatbot response"""
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            return "Goodbye! Have a great day."
        
        return self.generate_response(user_input)


if __name__ == "__main__":
    chatbot = ChatBot()
    print("Chatbot initialized successfully!")
