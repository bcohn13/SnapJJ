import openai
import os
from argparse import ArgumentParser

#client = openai.OpenAI(
 # api_key=os.environ.get("Open_Ai_Key")
  #)

openai.api_key=os.environ.get("Open_Ai_Key")
#completion = client.chat.completions.create(
 # model="gpt-4o-mini",
 # store=True,
 # messages=[
 #   {"role": "user", "content": "write a haiku about ai"}
 # ]
#)

#print(completion.choices[0].message)

def main(path):
    with open(path,'rb') as image_file:
        
        
        response= openai.completions.create(
        prompt="Describe this bjj image",
        model="gpt-4",  # Use GPT-4 with vision capabilities
        #messages=[
        #    {"role": "system", "content": "You are a helpful assistant."},
        #    {"role": "user", "content": "Please describe this image."}
        #],
        #files=[{
        #    "file": image_file,
         #   "purpose": "answers"
        #}]
    )
        
        print(response)
    

if __name__=="__main__":
    parser=ArgumentParser()
    parser.add_argument("Image")
    args=parser.parse_args()
    image=args.Image
    main(image)