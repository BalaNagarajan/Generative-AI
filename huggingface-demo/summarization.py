from transformers   import pipeline

def getSummarization(text):
    # Create a summarization pipeline using the Hugging Face library
    summarizer = pipeline('summarization')
    
    # Summarize the given text
    result = summarizer(text)
    
    # Return the summarized text
    return result

#Define main function
if __name__ == '__main__':
    # Define the input text for summarization
    text = "The Hugging Face is a company that is focused on natural language processing." \
           "They have developed a wide range of tools and libraries that make it easy for developers"\
           "to work with natural language processing. Their tools are widely used in the industry and"\
            "have helped many developers build powerful applications."
    
    # Call the getSummarization function to summarize the text
    result = getSummarization(text)
    
    # Print the summarized text
    print(result)

