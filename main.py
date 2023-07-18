import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("theojolliffe/bart-cnn-science")
model = AutoModelForSeq2SeqLM.from_pretrained("theojolliffe/bart-cnn-science")

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for input_str in request.text:
        # Encoding the input string as a tensor
        input_ids = torch.tensor(tokenizer.encode(input_str)).unsqueeze(0)
        # Creating an attention mask
        attention_mask = torch.ones_like(input_ids)
        # Geting the pad token id from the tokenizer
        pad_token_id = tokenizer.pad_token_id
        # Generating a response using the model
        output_ids = model.generate(input_ids, attention_mask=attention_mask, pad_token_id=pad_token_id, max_length=100, top_p=0.9, top_k=50)
        # Decoding the response and remove special tokens
        response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        # Append the response to the output list
        output.append(response)

    return SimpleText(dict(text=output))
