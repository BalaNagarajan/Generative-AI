import streamlit as st
from transformers import pipeline

def getSentiment(text):
    # Create a sentiment analysis pipeline using the Hugging Face library
    classifier = pipeline('sentiment-analysis')
    
    # Perform sentiment analysis on the given text
    result = classifier(text)
    
    # Return the sentiment analysis result
    return result


if __name__ == '__main__':
    #Use streamlit to create a simple web app
    st.title('Sentiment Analysis Demo')
    st.write('Enter some text to perform sentiment analysis:')
    # Define the text to be analyzed
    user_input = st.text_area('Text input')
    # Call the getSentiment function to perform sentiment analysis
    if st.button('Analyze'):
        result = getSentiment(user_input)
        # Print the sentiment analysis result
        st.write(result)

# Run the app with streamlit run sentiment-analysis-demo.py
