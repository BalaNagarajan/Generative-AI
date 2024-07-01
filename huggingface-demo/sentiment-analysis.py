from transformers import pipeline

def getSentiment(text):
    # Create a sentiment analysis pipeline using the Hugging Face library
    classifier = pipeline('sentiment-analysis')
    
    # Perform sentiment analysis on the given text
    result = classifier(text)
    
    # Return the sentiment analysis result
    return result


if __name__ == '__main__':
    # Define the text to be analyzed
    text = "I am so happy today"
    
    # Call the getSentiment function to perform sentiment analysis
    result = getSentiment(text)
    
    # Print the sentiment analysis result
    print(result)
