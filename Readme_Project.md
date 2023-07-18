# Model Used
- For this Chatbot I used sequence-to-sequence LLM Bart which is fine tuned on scientific_papers dataset. I used this LLM as it was close to giving scientific responses as I was asked to create a scientific chatbot. To make it accurate I could have used Qasper dataset or ScienceQA Dataset and fine tune the llm on one of these datasets, but as I had limited resourcces I could not do it.
- Link to the LLM https://huggingface.co/theojolliffe/bart-cnn-science

# About the dependencies and Librarires 
- For this very test i used Python 3.8.0 and openfabric-pysdk 0.1.11.
- It was throwing errors when i used Python 3.11 and openfabric-pysdk 0.2.6
- Moreover i used FlaskIO's latest version i.e 5.3.4 
- Torch 2.0.1
- transformers 4.30.2

# About the code

- The torch.tensor function encodes the input string as a tensor using the 'tokenizer' object.
- The 'unsqueeze(0)' function adds an extra dimension to the tensor, as the model expects a batch of input tensors.
- The torch.ones_like function creates an attention mask for the input tensor. This mask is used to specify which tokens in the input_ids Should be attended to by the model during the generation process. In this case, it sets all values to 1.
- The pad_token_id function gets the pad token id from the tokenizer. The pad token is used to fill sequences to a fixed length.
- Generating a response using the 'model'. The 'generate' method takes the input_ids and generates output text. It uses the attention_mask to mask out certain tokens and sets a maximum length of 100 for the generated text. The 'top_p' and 'top_k' parameters control the diversity of the generated output.
- The tokenizer.decode function decodes the generated response from 'output_ids' to a human-readable text without special tokens.
- Append the generated response to the 'output' list.

# Running the App
- To run the app simply run the start.sh file by writing ./start.sh in the terminal
- On your Browser go to the http://localhost:5000/
- Go to the swagger-ui
- Click the post tab
- Click on 'Try it out' it on button in the Parameters tab
- CLick on the execute button in the bottom of the post tab.
- Then in the Responses tab you will see the Server response. In my case Server returns the Code 200 which means success and shows the response in the json format. I have also attached the json file in the repository.

## Hoping to hear from you soon!!!
