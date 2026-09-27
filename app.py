
import streamlit as st
import joblib
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Spam Message Classifier",
    page_icon="📩",
    layout="centered"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📩 Spam Message Classification")

st.write(
    "Enter a message below to check whether it is "
    "**Spam** or **Ham**."
)

# --------------------------------------------------
# FIND PROJECT FOLDER
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model and vectorizer are in the same folder as app.py
MODEL_PATH = os.path.join(
    BASE_DIR,
    "spam_classifier_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "tfidf_vectorizer.pkl"
)

# --------------------------------------------------
# CHECK MODEL FILE
# --------------------------------------------------

if not os.path.exists(MODEL_PATH):

    st.error("❌ Model file not found!")

    st.write("Python is looking for:")
    st.code(MODEL_PATH)

    st.stop()

# --------------------------------------------------
# CHECK VECTORIZER FILE
# --------------------------------------------------

if not os.path.exists(VECTORIZER_PATH):

    st.error("❌ TF-IDF vectorizer file not found!")

    st.write("Python is looking for:")
    st.code(VECTORIZER_PATH)

    st.stop()

# --------------------------------------------------
# LOAD MODEL AND VECTORIZER
# --------------------------------------------------

try:

    model = joblib.load(MODEL_PATH)

    vectorizer = joblib.load(VECTORIZER_PATH)

except Exception as e:

    st.error("❌ Error loading the model or vectorizer.")

    st.exception(e)

    st.stop()

# --------------------------------------------------
# SUCCESS MESSAGE
# --------------------------------------------------

st.success("✅ Model and vectorizer loaded successfully!")

# --------------------------------------------------
# MESSAGE INPUT
# --------------------------------------------------

message = st.text_area(
    "✍️ Enter your message:",
    placeholder="Example: Congratulations! You have won a free prize!"
)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button("🔍 Check Message"):

    if message.strip() == "":

        st.warning("⚠️ Please enter a message.")

    else:

        try:

            # Convert text into TF-IDF features
            message_vector = vectorizer.transform([message])

            # Make prediction
            prediction = model.predict(message_vector)[0]

            # --------------------------------------------------
            # CONVERT MODEL OUTPUT TO SPAM / HAM
            # --------------------------------------------------

            if prediction == 1 or str(prediction).lower() == "spam":

                result = "spam"

            elif prediction == 0 or str(prediction).lower() == "ham":

                result = "ham"

            else:

                result = str(prediction).lower()

            # --------------------------------------------------
            # DISPLAY RESULT
            # --------------------------------------------------

            if result == "spam":

                st.error("🚨 SPAM MESSAGE")

                st.write(
                    "This message has been classified as **Spam**."
                )

            elif result == "ham":

                st.success("✅ HAM MESSAGE")

                st.write(
                    "This message has been classified as "
                    "**Ham (Not Spam)**."
                )

            else:

                st.info(
                    f"Prediction: {result}"
                )

        except Exception as e:

            st.error("❌ Error during prediction.")

            st.exception(e)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Spam Message Classification using Machine Learning"
)
