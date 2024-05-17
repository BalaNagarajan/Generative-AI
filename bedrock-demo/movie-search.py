import boto3
import botocore.config
import json

def movie_search(movietype: str, year: str):
    """
    Search for movies based on the movie type and year.

    Args:
        movietype (str): The type of movies to search for.
        year (str): The year in which the movies were released.

    Returns:
        str: The details of the movies found.
    """
    # Define the prompt for the movie search
    prompt = f"""<s>[INST]Human: List the {movietype} movies released in {year} [/INST]</s>"""

    # Design the properties of the model you choose   
    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

    try:
        # Create a boto3 client for the bedrock service
        bedrock_client = boto3.client('bedrock-runtime', region_name="<AWS-REGION>", config=botocore.config.Config(read_timeout=300,retries={'max_attempts': 0}))
        #Invoke the model with the prompt
        response = bedrock_client.invoke_model(
            modelId='<MODEL-NAME>',
            body=json.dumps(body)
        )
        response_content = response.get('body').read()
        movie_data = json.loads(response_content)
        print(movie_data)
        movie_details = movie_data['generation']
        return movie_details
    except Exception as e:
        print(f"Error generating movie details: {e}")
        return ""
    
def lambda_handler(event, context):
    # Load the event data
    event = json.loads(event['body'])
    movieType = event['movieType']
    movieYear = event['movieYear']
    # Search for movie details
    movie_details = movie_search(movieType, movieYear)
    if movie_details:
        response = {'statusCode': 200,'body': json.dumps(movie_details)} 
    else:
        response = {'statusCode': 200,'body': ''} 
    
    return response
