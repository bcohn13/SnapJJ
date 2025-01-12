import openai
import os
from argparse import ArgumentParser
import base64

import openai.cli

client = openai.OpenAI(
  api_key=os.environ.get("Open_Ai_Key")
  )

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
    #openai.images.edit(image=)
    #with open(path,'rb') as image_file:
    url="https://github.com/bcohn13/SnapJJ/blob/CLI/bjj.jpg"
    img_b64_str=base64.b64encode(url.encode())
    image=r"C:\Users\bcohn\source\repos\Snapjj\SnapJJ\bjj.jpg"
    with open(image,"rb") as image_file:
        image_binary=image_file.read()
        #img_b64_str=base64.b64encode(image_binary)
    response= client.chat.completions.create(
    #prompt=f"Please describe this image: {url}",
    model="gpt-4o-mini",  # Use GPT-4 with vision capabilities
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url
                    }
                }],
                
          },
            ],
    max_tokens=10
)
        
    print(response)
    

if __name__=="__main__":
   # parser=ArgumentParser()
    #parser.add_argument("Image")
    #args=parser.parse_args()
    #image=args.Image
    main()