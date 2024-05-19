This is the main Python script that interacts with the OpenAI API.

import os 
import openai 
from dotenv import load_dotenv 

# Load environment variables from .env file 
load_dotenv() 

# Get API key from environment variable 
openai.api_key = 
os.getenv("OPENAI_API_KEY")

# Function to get response from OpenAI API 
def get_openai_response ( prompt ) :
    response = openai.Completion.create(
      engine="text-davinci-003", 
      prompt=prompt, 
      max_tokens=150 

    )
    return 
response.choices(0).text.strip() 

if __name__ == "__main__" :
    user_prompt = "Explain the theory of relativity." 
    response = 
  get_openai_response(user_prompt) 
      print (f"Response from OpenAI :
      (response)") 
