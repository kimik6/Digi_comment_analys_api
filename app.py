import streamlit as st
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

# Load the tokenizer and the fine-tuned model
tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-base-parsbert-uncased")
model2 = TFAutoModelForSequenceClassification.from_pretrained("kimik76/test_trainer")

# Dictionary of responses
# RESPONSES = ["Class 0", "Class 1", "Class 2"]  # Update with actual class names if available

RESPOSES = {
    0 : "پیشنهاد میکنم",
    1 : "پیشنهاد نمیکنم",
    2 : "مطمئن نیستم"
}
# Streamlit app
st.title("Text Classification with ParsBERT")

# Input text box
user_input = st.text_input("نظر شما راجب محصول چیست؟")

if user_input:
    # Prepare the inputs
    inputs = tokenizer(user_input, return_tensors="tf")

    # Get logits from the model
    logits = model2(**inputs).logits

    # Get the predicted class
    predicted_class = tf.argmax(logits, axis=-1).numpy()[0]

    # Display the result
    st.write(f"نظر تحلیلی مدل بر اساس نظر کاربر : {RESPOSES[int(predicted_class)]}")
