from cgitb import small
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

models = dict(
    mistral_7b="open-mistral-7b",
    mixtral="open-mixtral-8x7b",
    small="mistral-small-latest",
    medium="mistral-medium-latest",
    large="mistral-large-latest"
)

model = models["mistral_7b"]

client = MistralClient(api_key=api_key)

messages = [
    ChatMessage(role="user", content="What is the best French cheese?")
]

# With streaming
stream_response = client.chat_stream(model=model, messages=messages)

for chunk in stream_response:
    print(chunk.choices[0].delta.content, end="")