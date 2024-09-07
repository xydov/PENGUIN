from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
end = False


def my_AI_Answer(input):
    inputs = tokenizer(input, return_tensors="pt")
    reply_ids = model.generate(**inputs)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return reply

text= "hello"
print("sisou pichou :", my_AI_Answer(text))



while end!=True:
    text=input("->")
    if (text==True):
        print("exit")
    print("sisou pichou :", my_AI_Answer(text))






