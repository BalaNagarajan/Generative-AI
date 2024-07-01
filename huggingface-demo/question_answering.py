from transformers import pipeline

def getQuestionAnswering(context, question):
    # Create a question answering pipeline using the Hugging Face library
    question_answerer = pipeline('question-answering')
    
    # Answer the given question based on the context
    result = question_answerer(question=question, context=context)
    
    # Return the question answering result
    return result

#Define main function
if __name__ == '__main__':
    # Define the context and question for question answering
    context = "The Hugging Face is a company that is focused on natural language processing."
    question = "What is Hugging Face focused on?"
    
    # Call the getQuestionAnswering function to answer the question
    result = getQuestionAnswering(context, question)
    
    # Print the question answering result
    print(result)
    