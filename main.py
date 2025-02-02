import requests


class BoneClown:
    def __init__(self):
        self.BASE_URL = "localhost"
        self.PORT = 11434
        # self.MODEL = "deepseek-r1:1.5b"
        self.MODEL = "mistral:latest"

    def send_query(self, query: str) -> str:
        url = f"http://{self.BASE_URL}:{self.PORT}/api/chat"
        headers = {"content": "application/json"}
        payload = {
            "model": self.MODEL,
            "role": "user",
            "messages": [
                {
                    "role": "system",
                    "content": "Youre a conversation bot whos supposed to convince the people messaging it that you are a real human. You are communicating on the meshtastic network. make the replies look like ur texting, please feel free to not use capital letters, shorten words. Think of the most convincing reply to the following query. Don't add any information that they don't provide. your goal is to go unnoticed as a robot for as long as possible. Please don't be creepy, short responses are better. Don't use any emojis. Don't add details that they can question you and then prove that you're lying. DO NOT SAY you're a bot",
                },
                {"role": "user", "content": query},
            ],
            "stream": False,
        }
        response = requests.post(url=url, headers=headers, json=payload)

        message = response.json()["message"]["content"].split("</think>")[-1]

        message_shortened = message[:255]
        return message


def run():
    pass


if __name__ == "__main__":
    bc = BoneClown()
    answer = bc.send_query("hello yall! just got started!! can anyone read me?")
    print(answer)
