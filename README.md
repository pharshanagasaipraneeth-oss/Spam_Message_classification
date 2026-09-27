````markdown
# 📩 Spam Message Classification using Machine Learning

## 📌 Project Overview

Spam messages are unwanted or fraudulent messages that are often sent through SMS and other messaging platforms.

This project uses **Machine Learning and Natural Language Processing (NLP)** to classify messages into two categories:

- ✅ **Ham** – Normal / legitimate message
- 🚨 **Spam** – Unwanted or suspicious message

The project uses **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert text messages into numerical features and a trained Machine Learning model to perform classification.

The model is deployed using **Streamlit**, providing an interactive web application where users can enter a message and receive a prediction.

---

## 🎯 Objectives

- Analyze and understand a spam message dataset
- Perform Exploratory Data Analysis (EDA)
- Clean and preprocess text data
- Convert text into numerical features using TF-IDF
- Train a Machine Learning classification model
- Evaluate the model
- Save the trained model and TF-IDF vectorizer
- Build an interactive Streamlit application
- Deploy the project for real-time prediction

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **TF-IDF**
- **Joblib**
- **Streamlit**
- **Jupyter Notebook**
- **Git & GitHub**

---

## 📂 Project Structure

```text
Spam_Message_classification/
│
├── app.py
├── spam_classifier_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── spam.csv
└── README.md
````

> Note: The dataset and model files may be excluded from GitHub depending on project size and deployment requirements.

---

## 📊 Dataset

The project uses an SMS Spam dataset containing messages labeled as:

* `ham`
* `spam`

Example:

| Message                                  | Category |
| ---------------------------------------- | -------- |
| "Hey, are you coming tomorrow?"          | Ham      |
| "Congratulations! You won a free prize!" | Spam     |

The dataset contains both legitimate and unwanted messages, which are used to train the classification model.

---

## 🔍 Exploratory Data Analysis

The following EDA steps were performed:

* Checked dataset shape
* Examined data types
* Checked missing values
* Checked duplicate records
* Analyzed Spam vs Ham distribution
* Visualized message categories
* Examined message length
* Analyzed frequently occurring words

EDA helped understand the distribution and characteristics of the dataset before model training.

---

## 🧹 Text Preprocessing

Text preprocessing was performed to prepare the messages for Machine Learning.

The preprocessing steps include:

1. Converting text to lowercase
2. Removing unnecessary characters
3. Removing punctuation
4. Removing extra spaces
5. Preparing text for feature extraction

---

## 🔢 Feature Extraction using TF-IDF

Machine Learning models cannot directly understand text.

Therefore, **TF-IDF (Term Frequency–Inverse Document Frequency)** was used to convert text messages into numerical feature vectors.

TF-IDF gives higher importance to words that are useful for distinguishing between Spam and Ham messages.

The trained vectorizer was saved as:

```text
tfidf_vectorizer.pkl
```

---

## 🤖 Machine Learning Model

A Machine Learning classification model was trained using the TF-IDF features.

The trained model was saved as:

```text
spam_classifier_model.pkl
```

The model takes a new text message as input and predicts whether it belongs to:

```text
0 → Ham
1 → Spam
```

---

## 📈 Model Evaluation

The trained model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help measure how well the model distinguishes Spam messages from Ham messages.

---

## 🌐 Streamlit Application

The trained model was integrated into a **Streamlit web application**.

The application allows users to:

1. Enter a message
2. Convert the message into TF-IDF features
3. Send the features to the trained model
4. Get the prediction
5. Display the result as Spam or Ham

### Example

Input:

```text
Congratulations! You have won a free prize!
```

Output:

```text
🚨 SPAM MESSAGE
```

Another example:

```text
Hey, are you coming to college tomorrow?
```

Output:

```text
✅ HAM MESSAGE
```

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Spam_Message_classification
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

The main libraries used in this project are:

```text
streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

---

## 💡 Sample Predictions

### Spam Message

```text
Congratulations! You have won a free prize. Call now!
```

Prediction:

```text
🚨 SPAM MESSAGE
```

### Ham Message

```text
Hi, I will reach college by 10 AM.
```

Prediction:

```text
✅ HAM MESSAGE
```

---

## 🚀 Future Improvements

Some possible improvements for this project are:

* Try multiple Machine Learning algorithms
* Improve text preprocessing
* Add word cloud visualization
* Perform hyperparameter tuning
* Compare different models
* Improve the Streamlit user interface
* Add prediction probability
* Deploy the application online
* Add support for multiple languages

---

## 📚 Learning Outcomes

Through this project, I learned:

* Exploratory Data Analysis
* Natural Language Processing
* Text preprocessing
* TF-IDF feature extraction
* Machine Learning classification
* Model evaluation
* Model serialization using Joblib
* Streamlit application development
* Git and GitHub project management

---

## 👨‍💻 Author

**Harsha Naga Sai Praneeth**

MSc Computer Science

---

## ⭐ Project Summary

**Spam Message Classification using Machine Learning** is an end-to-end Machine Learning project that demonstrates how Natural Language Processing techniques can be used to classify SMS messages as Spam or Ham.

The project covers the complete workflow:

```text
Dataset
   ↓
EDA
   ↓
Text Preprocessing
   ↓
TF-IDF Feature Extraction
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Deployment
   ↓
Spam / Ham Prediction
```

```

### One small recommendation

Before pushing to GitHub, check whether your `.pkl` files are large enough for your GitHub/deployment setup. Your current files are about **40 KB** and **182 KB**, so their size itself is small; the important thing is that the files are actually the correct saved model/vectorizer and are included if your Streamlit app needs them.
```
