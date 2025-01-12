from openai import OpenAI
import os
from argparse import ArgumentParser

client = OpenAI(
  api_key=os.environ.get("Open_Ai_Key")
  )


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)

if __name__=="__main__":
    parser=ArgumentParser
    parser.add_argument("Image")
    args=parser.parse_args()
    image=args.Image