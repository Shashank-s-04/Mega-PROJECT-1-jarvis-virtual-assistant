from openai import OpenAI
client = OpenAI(
    api_key="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"
)

completion = client. chat. completions. create(
model="gpt-3.5-turbo",
messages=[
{"role": "system", "content": "You are a virtual assistant named jarvis skilled general taks in alexa and google cloud "},
{"role": "user", "content": "What is coding"}
]
)
print(completion.choices[0].message)