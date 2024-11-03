from datetime_tool import get_current_date
from langchain_service import LangChainService
from lib import print_prompt, print_answer


def chat_history_sample():
    print('[chat_history_sample]')
    lang_chain = LangChainService()

    # without history
    print("=== Case 1: Talk without history ===")
    prompt = 'What is the capital in Japan?'
    print_prompt(prompt)
    print_answer(lang_chain.ask_without_history(prompt))
    prompt = '日本語で'
    print_prompt(prompt)
    print_answer(lang_chain.ask_without_history(prompt))

    # with history
    print("=== Case 2: Talk with history ===")
    prompt = 'What is the capital in Japan?'
    print_prompt(prompt)
    print_answer(lang_chain.ask(prompt))
    prompt = '日本語で'
    print_prompt(prompt)
    print_answer(lang_chain.ask(prompt))
    print()


def function_calling_sample():
    print('[function_calling_sample]')
    lang_chain = LangChainService()

    # without function calling
    print(f"=== Case 1: Asking today's date ({lang_chain.modelName}) ===")
    prompt = "What's the date today?"
    print_prompt(prompt)
    print_answer(lang_chain.ask_without_history(prompt))

    # with function calling
    print(f"=== Case 2: Asking today's date ({lang_chain.modelName} with function calling) ===")
    prompt = "What's the date today?"
    print_prompt(prompt)
    print_answer(lang_chain.ask_with_func([get_current_date], prompt))
    print()


def rag_sample():
    print('[rag_sample]')
    lang_chain = LangChainService()

    data = [
        "My name is Satoshi Nakamura." ,
        # "I'm 32 years old." ,
        # "I'm a graphic designer." ,
        # "I was born in Kyoto prefecture.",
        # "I graduated from the Faculty of Fine Arts at Kyoto University of Arts.",
        # "My hobbies are outdoor activities (hiking, camping) and photography.",
        # "My specialty is creating digital illustrations.",
        # "My personality is easy-going, sociable, and curious.",
        # "My favorite food is Japanese food in general, especially sushi.",
        # "My dream is to have my own design studio",
    ]
    index = lang_chain.execute_embedding(data)

    prompt = "What's your name?"
    print_prompt(prompt)
    print_answer(lang_chain.ask_with_store(prompt, index))



# Sample 1: Chat history
# chat_history_sample()

# Sample 2: Function calling
# function_calling_sample()

# Sample 3: RAG
rag_sample()