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

def main():
    #with open(path,'rb') as image_file:
    url="https://github.com/bcohn13/SnapJJ/blob/CLI/bjj.jpg"

    
    response= openai.chat.completions.create(
    #prompt=f"Please describe this image: {url}",
    model="gpt-4",  # Use GPT-4 with vision capabilities
    messages=[
       {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Please describe this image: {url}"}
    ]#,
    #files=[{
    #    "file": image_file,
      #   "purpose": "answers"
    #}]
)
        
    print(response)
    

if __name__=="__main__":
   # parser=ArgumentParser()
    #parser.add_argument("Image")
    #args=parser.parse_args()
    #image=args.Image
    main()