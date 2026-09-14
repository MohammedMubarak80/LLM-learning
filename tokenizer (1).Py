
!pip install tiktoken
import tiktoken


#simple tokenizer
sentence ="i love python programming"
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
