from transformers import pipeline

def getZeroShotClassification(text, labels):
    # Create a zero-shot classification pipeline using the Hugging Face library
    classifier = pipeline('zero-shot-classification')
    
    # Perform zero-shot classification on the given text
    result = classifier(text, labels)
    
    # Return the zero-shot classification result
    return result


if __name__ == '__main__':
    # Define the array of text labels
    labels = ["politics", "business", "technology", "entertainment"]
    text = ["I am so happy today", "The stock market is booming", "The new iPhone is amazing", "The movie was a huge success"]
    result = getZeroShotClassification(text, labels)
    print(result)
