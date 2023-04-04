# Chat-GPT API

## installation
`pip install git+https://github.com/Andalusia-Data-Science-Team/chatGPT-api`


## Usage

- reply_status
  - "stop" --> chatGPT returned all the text and reached the stop 
  - "length" --> the reply returned is not the full reply because you reached the tokens limit from chatGPT which is 4096 tokens


```python
from chatGPT_api import ChatGPT

api_key="ENTER THE API KEY HERE"
chatGPT=ChatGPT(api_key)

# send a message get reply,reply_status
reply,reply_status=chatGPT.send_message("hello chat gpt ")

```
### live-chat
- take input from the prompt , get reply from chat gpt , history tracked
- if you want to stop the live chat type 0
```python

chatGPT.live_chat()

```
### get all chat history
```python

chat_gpt.clear_history()
reply_message,reply_status=chat_gpt.send_message("hello chat-gpt")

reply_message,reply_status=chat_gpt.send_message("do you know andalusia hospitals")


chat_gpt.chat_history()

```
```
user:
hello chat-gpt

----------

chat-gpt:
Hello! How can I assist you today?

----------

user:
do you know andalusia hospitals

----------

chat-gpt:
Yes, Andalusia is a region in southern Spain that has many hospitals and healthcare facilities. Some of the most well-known hospitals in Andalusia include Hospital Universitario Virgen del Rocío in Seville, Hospital Regional Universitario de Málaga, and Hospital Universitario Reina Sofía in Córdoba. There are many other hospitals and medical centers throughout the region, providing high-quality healthcare services to locals and tourists alike.

----------

```