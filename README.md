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
