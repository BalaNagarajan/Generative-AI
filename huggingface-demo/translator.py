from transformers import pipeline

def translate_english_to_tamil(text):
    # Create a translation pipeline using the Hugging Face library
    translator = pipeline("translation", model="suriya7/English-to-Tamil")
    
    # Translate the given text from English to Tamil
    result = translator(text)
    
    # Return the translated text
    return result


# Define main function
if __name__ == '__main__':
    # Define the input text to be translated
    text = "Hello how are you"
    
    # Call the translate_english_to_tamil function to translate the text
    result = translate_english_to_tamil(text)
    
    # Print the translated text
    print(result)
