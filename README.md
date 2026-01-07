# 🤖 AI-Chatbot-NLP

AI-powered chatbot using NLP techniques for intent classification and automated customer support. Built with Python, NLTK, spaCy, TensorFlow, and Flask/Streamlit deployment.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements an intelligent chatbot using Natural Language Processing (NLP) techniques. The chatbot can understand user intents, extract relevant information from user queries, and generate appropriate responses. It supports both command-line interaction and web-based deployment using Streamlit.

## ✨ Features

- **Intent Classification**: Uses NLP to classify user queries into predefined intents
- **Text Preprocessing**: Tokenization, lemmatization, and stop-word removal
- **Feature Extraction**: Bag-of-Words and TF-IDF vectorization
- **Multiple Deployment Options**: Flask and Streamlit web interfaces
- **Extensible Architecture**: Easy to add new intents and responses
- **Multiple NLP Libraries**: NLTK, spaCy, and TensorFlow support
- **Multi-turn Conversations**: Maintains conversation history

## 📁 Project Structure

```
AI-Chatbot-NLP/
├── src/
│   ├── __init__.py
│   └── chatbot.py          # Main ChatBot class
├── data/
│   └── intents.json        # Intent definitions and patterns
├── app.py                  # Streamlit web application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
└── .gitignore            # Git ignore rules
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivraj1182/AI-Chatbot-NLP.git
   cd AI-Chatbot-NLP
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download required NLTK data**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet')"
   ```

## 💻 Usage

### Using Streamlit Web Application

```bash
streamlit run app.py
```

The web interface will open at `http://localhost:8501`

### Using Python Script

```python
from src.chatbot import ChatBot

# Initialize the chatbot
chatbot = ChatBot('data/intents.json')

# Get response to user input
response = chatbot.chat("Hello!")
print(response)
```

## 🛠️ Technologies Used

### Core Libraries
- **NLTK**: Natural Language Toolkit for text processing
- **spaCy**: Industrial-strength NLP library
- **TensorFlow/Keras**: Deep learning framework
- **scikit-learn**: Machine learning library

### Web Frameworks
- **Streamlit**: Rapid web application development
- **Flask**: Lightweight web framework (optional)

### Data & Utilities
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization

## 📊 Key Work Done

✅ Collected and structured intent-response dataset (data/intents.json)
✅ Implemented text preprocessing pipeline (tokenization, lemmatization, stop-word removal)
✅ Built intent classification model using Bag-of-Words
✅ Implemented feature extraction and vectorization
✅ Created rule-based fallback logic for unrecognized queries
✅ Developed Streamlit web interface
✅ Added multi-turn conversation support
✅ Implemented proper error handling

## 🎓 Learning Outcomes

- Proficiency in NLP preprocessing and feature engineering
- Intent classification techniques
- Web application deployment using Streamlit
- Building scalable chatbot architectures
- Handling multi-turn conversations
- Integration of multiple NLP libraries

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shivraj1182**

- GitHub: [@shivraj1182](https://github.com/shivraj1182)
- Email: shivraj1182@example.com

## 🙏 Acknowledgments

- NLTK documentation and community
- spaCy for excellent NLP tools
- Streamlit for making web app development simple
- TensorFlow/Keras for deep learning capabilities

---

**Made with ❤️ for NLP enthusiasts**
