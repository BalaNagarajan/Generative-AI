from transformers import pipeline

def getTextGeneration(text):
    # Create a text generation pipeline using the Hugging Face library
    generator = pipeline('text-generation')
    
    # Generate text based on the given input text
    result = generator(text)
    
    # Return the generated text
    return result

# define main function
if __name__ == '__main__':
    # Define the input text for text generation
    text = "Once upon a time"
    
    # Call the getTextGeneration function to generate text
    result = getTextGeneration(text)
    
    # Print the generated text
    print(result)

