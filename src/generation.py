from src.chatmodel import llm, final_prompt

answer = llm.invoke(final_prompt)
print(answer.content)