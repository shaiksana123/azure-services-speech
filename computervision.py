from openai import OpenAI
endpoint = "your endpoint"
deployment_name = "gpt-5.4-mini"
api_key = "your api key"
    
client = OpenAI(
     base_url=endpoint,
     api_key=api_key
 )
    
response = client.responses.create(
     model=deployment_name,
     input=[{
         "role": "user",
         "content": [
             {"type": "input_text", "text": "what's in this image?"},
             {"type": "input_image", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkX-n4Lo6fH2-uYtvCreIQ04w_2Rn3ZzrnTVVnYzuE1Q&s=10"},
         ],
     }],
 )
    
print(f"answer: {response.output_text}")