import text2emotion
inp = "I am very angry today please Google can you open Google"
emotion = text2emotion.get_emotion(inp)
if emotion:
    print(emotion)
    print(max(zip(emotion.values(), emotion.keys()))[1])
