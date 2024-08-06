



import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from sklearn.preprocessing import LabelEncoder


#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
pickle_in2= open("labelencoder.pkl","rb")
classifier2=pickle.load(pickle_in2)
#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(nitrogen,phosphorous,potassium,temparture,humidity,ph,rainfall):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    sample_probabilities = classifier.predict_proba([[nitrogen,phosphorous,potassium,temparture,humidity,ph,rainfall]])
# Get the top 5 class indices with highest probabilities
    top_5_indices = np.argsort(sample_probabilities[0])[::-1][:5]
    print("Top5",top_5_indices)
    # Get the corresponding crop names
    top_5_crops = classifier2.inverse_transform(top_5_indices)
    print(top_5_crops)
    top_5_probabilities = sample_probabilities[0][top_5_indices]
    return list(zip(top_5_crops, top_5_probabilities))

def main():
    st.title("Crop Recommendation System")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Crop ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    nitrogen = st.text_input("Nitrogen","Type Here")
    phosphorous = st.text_input("Phosphorus","Type Here")
    potassium = st.text_input("Potassium","Type Here")
    temparture = st.text_input("Temperature","Type Here")
    humidity = st.text_input("Humidity","Type Here")
    ph = st.text_input("PH","Type Here")
    rainfall= st.text_input("Rainfall","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(nitrogen,phosphorous,potassium,temparture,humidity,ph,rainfall)
        top_5_message = "Top 5 Probabilities:\n"
        for crop, probability in result:
            top_5_message += f'{crop}: {probability:.2f}\n'
        st.success(top_5_message)

if __name__=='__main__':
    main()
    
    
    