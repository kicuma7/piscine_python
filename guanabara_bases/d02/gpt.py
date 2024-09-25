from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar o modelo GPT-2 pré-treinado e o tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Exemplo de entrada
input_text = "Como posso programar uma inteligência artificial?"

# Tokenizar a entrada
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Gerar uma resposta
output = model.generate(input_ids, max_length=100, num_return_sequences=1)
response = tokenizer.decode(output[0], skip_special_tokens=True)

print(response)