import time

import openai


class ChatGPT:

    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self._api_key = api_key
        openai.api_key=api_key
        self._message_history = []
        self._model = model
        self.total_tokens = 0
        self._last_reply_message = None
        self._last_reply_status = None

    def send_message(self, message):
        """

        :param message: (str)
        :return: message (str), reply status (str)
        """
        self._message_history.append({"role": 'user', "content": message})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self._message_history)
        reply_message = completion.choices[0].message.content
        reply_status = completion.choices[0].finish_reason

        self.total_tokens = completion.usage.total_tokens
        self._last_reply_message = reply_message
        self._last_reply_status = reply_status
        self._message_history.append(completion.choices[0].message)

        return reply_message, reply_status

    def clear_history(self):
        self._message_history = []
        self.total_tokens = 0
        self._last_reply_message = self._last_reply_status = None
        print("History cleared")

    def last_reply(self):
        summary_text=f"last_message:{self._last_reply_message}\n{'-' * 10}\nreply_status:{self._last_reply_status}\n{'-' * 10}\ntotal_tokens:{self.total_tokens}"
        print(summary_text)
        return self._last_reply_message,self._last_reply_status

    def chat_history(self):
        for message_dict in self._message_history:
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