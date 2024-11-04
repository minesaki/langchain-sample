from datetime_tool import get_current_date
from langchain_service import LangChainService
from lib import print_answer, print_prompt


def chat_history_sample():
    print("[chat_history_sample]")
    lang_chain = LangChainService()

    # without history
    print("=== Case 1: Talk without history ===")
    prompt = "What is the capital in Japan?"
    print_prompt(prompt)
    print_answer(lang_chain.ask_without_history(prompt))
    prompt = "日本語で"  # in Japanese
    print_prompt(prompt)
    print_answer(lang_chain.ask_without_history(prompt))

    # with history
    print("=== Case 2: Talk with history ===")
    prompt = "What is the capital in Japan?"
    print_prompt(prompt)
    print_answer(lang_chain.ask(prompt))
    prompt = "日本語で"  # in Japanese
    print_prompt(prompt)
    print_answer(lang_chain.ask(prompt))
    print()


def function_calling_sample():
    print("[function_calling_sample]")
    lang_chain = LangChainService()

    # without function calling
    print(f"=== Case 1: Asking today's date ({lang_chain.model_name}) ===")
    prompt = "What's the date today?"
    print_prompt(prompt)
    print_answer(lang_chain.ask_without_history(prompt))

    # with function calling
    print(f"=== Case 2: Asking today's date ({lang_chain.model_name} with function calling) ===")
    prompt = "What's the date today?"
    print_prompt(prompt)
    print_answer(lang_chain.ask_with_func([get_current_date], prompt))
    print()


def rag_sample():
    print("[rag_sample]")
    lang_chain = LangChainService()

    # Generate embedding (vector) data and store in memory
    # (This dummy person info was generated with ChatGPT)
    # (Note) This fails on my Windows PC due to error on NumPy.
    index = lang_chain.execute_embedding(
        [
            "My name is Satoshi Nakamura.",
            "I'm 32 years old.",
            "I'm a graphic designer.",
            "I was born in Kyoto prefecture.",
            "I graduated from the Faculty of Fine Arts at Kyoto University of Arts.",
            "My hobbies are outdoor activities (hiking, camping) and photography.",
            "My specialty is creating digital illustrations.",
            "My personality is easy-going, sociable, and curious.",
            "My favorite food is Japanese food in general, especially sushi.",
            "My dream is to have my own design studio",
        ]
    )

    prompt = "What's your name?"
    print_prompt(prompt)
    print_answer(lang_chain.ask_with_embedding(prompt, index))
    prompt = "Please introduce yourself."
    print_prompt(prompt)
    print_answer(lang_chain.ask_with_embedding(prompt, index))
    print()
