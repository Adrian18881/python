import whisper

model = whisper.load_model("base")
result = model.transcribe("adv-14/prj.01/Recording.m4a")
print(result["text"])