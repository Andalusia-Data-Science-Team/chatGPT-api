import time

import openai


class ChatGPTAPI:

    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.message_history = []
        self.model = model
        self.total_tokens = 0
        self.last_reply_message = None
        self.last_reply_status = None

    def send_message(self, message):
        self.message_history.append({"role": 'user', "content": message})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message_history)
        reply_message = completion.choices[0].message.content
        reply_status = completion.choices[0].finish_reason

        self.total_tokens = completion.usage.total_tokens
        self.last_reply_message = reply_message
        self.last_reply_status = reply_status
        self.message_history.append(completion.choices[0].message)

        return reply_message, reply_status

    def clear_history(self):
        self.message_history = []
        self.total_tokens = 0
        self.last_reply_message = self.last_reply_status = None
        print("History cleared")

    def last_reply(self):
        summary_text=f"last_message:{self.last_reply_message}\n{'-' * 10}\nreply_status:{self.last_reply_status}\n{'-' * 10}\ntotal_tokens:{self.total_tokens}"
        print(summary_text)
        return self.last_reply_message,self.last_reply_status

    def chat_history(self):
        for message_dict in self.message_history:
            sender = "user" if message_dict['role'] == 'user' else 'chat-gpt'
            print(f"{sender}:")
            print(message_dict['content'])
            print(f"\n{'-' * 10}\n")

    def live_chat(self):
        while True:
            user_input = input(">")

            if user_input == '0':
                break
            print("User:")
            print(user_input)
            print(f"\n{'-' * 10}\n")

            message, status = self.send_message(user_input)

            print("chat-gpt:")
            print(message)
            print(f"\n{'-' * 10}\n")
            time.sleep(2)