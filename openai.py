from openai import OpenAI

client = OpenAI(
    api_key = "<Your Key Here>",
)

command = '''
'''

completion = client.chat.completions.create(
    model = "gpt-5",
    message = [{"role": "system", "content": "You are a person named Pikachu who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Pikachu"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)