with open("/home/oliver/SourceCode/git/llms/build_llm_book/chap2/the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("num chars: ", len(raw_text))
print(raw_text[:99])


import re
def preprocess_text(raw_text):
    text = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    text = [item.strip() for item in text if item.strip()]
    return text

print(preprocess_text(raw_text)[:30])

