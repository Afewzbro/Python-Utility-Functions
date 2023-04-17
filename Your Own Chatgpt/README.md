# OpenAI API ChatGPT
This code demonstrates how to use the OpenAI API to generate responses for given prompts using the ChatGPT model.

## Requirements
openai package: The official OpenAI package can be installed via pip
An OpenAI API key: You need to have an OpenAI API key to use the API. You can get one by signing up at https://beta.openai.com/signup/
## Usage
Set the OpenAI API key in the code: openai.api_key = "YOUR_API_KEY"
Run the code in a terminal or an IDE
Enter the prompt to get a response from the ChatGPT model
Type 'exit' or 'quit' to stop the program
## Code explanation
1. The OpenAI library is imported and the API key is set up.
2. A while loop is started to allow the user to enter multiple prompts.
3. The model engine is set up with the text-davinci-003 engine, which is the most capable engine for text generation in OpenAI API.
4. User enters the prompt in the console.
5. The openai.Completion.create() method generates the response from the model using the prompt.
6. The response text is extracted from the API's response and printed in the console.
### Note: The maximum number of tokens that can be sent in one request is 2048. So, the max_tokens parameter in the openai.Completion.create() method should not exceed this limit.