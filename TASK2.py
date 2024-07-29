from transformers import MarianMTModel, MarianTokenizer
import streamlit as st

stl.set_page_config(page_title="Task-2",layout="wide", initial_sidebar_state="auto", menu_items=None)

model_name = 'Helsinki-NLP/opus-mt-en-fr'
#loading Pre-trained model and tokenizer
model_en_fr = MarianMTModel.from_pretrained(model_name)
tokenizer_en_fr = MarianTokenizer.from_pretrained(model_name)

st.title("Translation English to French(Implementing Beam Search Decoding)")

#Creating an english sentence to translate
sentence = st.text_input("Enter the Text to translate to French")

#defining number beams
num_beams = 5

if sentence:
    # Tokenize the input sentence
    encoded_sentence = tokenizer_en_fr(sentence, return_tensors='pt')
    
    # Generate translation using beam search
    generated_tokens = model_en_fr.generate(**encoded_sentence, num_beams=num_beams, early_stopping=True)
    translated_sentence = tokenizer_en_fr.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    st.write("English Sentence:",sentence)
    st.write("Translated French Sentence:",translated_sentence)

