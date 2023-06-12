import openai
import gradio

openai.api_key="#api key"

messages=[{"role":"system","content":"You are a pyschologist"}]

def CustomerChatGPT(user_input):
    messages.append({"role":"user","content":user_input})
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply= response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":ChatGPT_reply})
    return ChatGPT_reply

demo=gradio.Interface(fn=CustomerChatGPT,inputs="text",outputs="text",title="ChatBot")
demo.launch(share=True)                                                                  
