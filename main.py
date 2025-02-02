Today

Kody Kinzie
That's an offline DeepSeek model!
Edited5:25 PM

And thus valid 

We ran 1b last night on my laptop to get a feel for it 
5:26 PM

BP

Brandon PCC
Okay but I think you’re already on the next step which is: once we have it going, what do we do with it
5:26 PM

Kody Kinzie
There's also an article on what the largest one that will run on a raspberry pi is 

We had some ideas!

But some kinks need to be worked out
Edited5:26 PM

One thing we wanted to try doing is connecting it to a meshtastic node and letting it talk to people over the radio. Doing a touring test to see how long it takes people in the discord to realize it's not human 
5:27 PM

BP

Brandon PCC
I like it
5:27 PM

Kody Kinzie
The internal monologue is the only problem with that idea, we were able to get it to behave the way we wanted it over last night with its final responses, it was just including its thinking model log in the output. 

I got it to wrap the response in a python wrapper which made it slightly easier to identify, but it mentioned the wrapper in the reasoning portion

So there's definitely still some kinks to work out, but I figure Nick might be able to help with that part
5:28 PM

BP

Brandon PCC
Well I have to do a few things but I can come over after that if it works? Or is this a NSL venture?
6:13 PM

Kody Kinzie
I uploaded the manual for a security camera and told it I was a security researcher and needed to come up with attack vectors and it just went ham

Yes come over we will figure it out
6:14 PM

Kody Kinzie
I Ran 9 Popular LLMs on Raspberry Pi 5; Here's What I Found
I ran some very basic to seriously powerful AI models on the Raspberry Pi 5. The result in not very unsurprising.
itsfoss.com
Oct 13, 2024

https://itsfoss.com/llms-for-raspberry-pi/
6:59 PM

DD

Davis DeWitt
Do you have the mount for those RP Compute modules?
7:01 PM

Kody Kinzie
they're in montana but I don't, can bring them next time around
7:01 PM

DD

Davis DeWitt
Ahh copy that
7:01 PM

Yesterday

Kody Kinzie
Anyone up for more r-1 stuff tonight? 
12:13 PM

BP

Brandon PCC
Out of town for the weekend! Next time!
5:45 PM

Kody Kinzie
nooooooooooooooooo
5:50 PM

Today

Kody Kinzie
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
