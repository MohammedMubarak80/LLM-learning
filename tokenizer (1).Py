
!pip install tiktoken
import tiktoken


#simple tokenizer
sentence =input("enter the text....")
token = sentence.split()
print("token=",token)
print(len(token))

#using an LLM style-tokinizer
encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(sentence)

print("token IDs =",tokens)

print("number of tokens :",len(tokens))

print("decode tokens")
for token in tokens:
  print(encoding.decode([token]))

#vector embedding
embedding =  torch.nn.Embedding(10,4)

token_id = torch.tensor([3])

vector = embedding(token_id)

print("token_id :",token_id)
print("vector :",vector)

#positional encoding

import numpy as np

# Number of tokens
sequence_length = 5

# Size of each embedding
embedding_size = 4

# Create positional encoding
position_encoding = np.zeros((sequence_length, embedding_size))

for position in range(sequence_length):
    for dimension in range(embedding_size):
        position_encoding[position][dimension] = position / (10000 ** (dimension / embedding_size))

print(position_encoding)
