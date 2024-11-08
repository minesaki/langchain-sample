from langchain.indexes import VectorstoreIndexCreator
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.tools import BaseTool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings

from lib import print_debug


# env var "OPENAI_API_KEY" is implicitly used for credentials
class LangChainService:

    model_name = "gpt-4o-mini"
    embedding_model_name = "text-embedding-3-small"
    model = ChatOpenAI(model_name=model_name)
    # parser = StrOutputParser()
    messages = []

    def __init__(self):
        pass

    def ask_without_history(self, prompt) -> str:
        message = [HumanMessage(prompt)]
        ret = self.model.invoke(message)
        return ret.content
        # Another example, using LCEL (LangChain Expression Language)
        # chain = self.model | parser
        # return chain.invoke(message)

    def ask(self, prompt) -> str:
        self.messages.append(HumanMessage(prompt))
        ret = self.model.invoke(self.messages)
        return ret.content

    def ask_with_func(self, tools: list[BaseTool], prompt: str) -> str:
        messages = [HumanMessage(prompt)]
        model_with_tool = self.model.bind_tools(tools)  # Bind given functions as tools

        # First call
        ret = model_with_tool.invoke(messages)
        messages.append(ret)

        # Return response if no function calling is required by LLM
        if not ret.tool_calls:
            return ret.content

        # Execute tools specified by LLM and add results to prompt
        for tool_call in ret.tool_calls:
            print_debug("  [tool_call] ", tool_call)
            tool_name = tool_call["name"].lower()
            tool = self.__find_first_tool_by_name(tools, tool_name)
            tool_result = tool.invoke(tool_call)
            print_debug("  [Added prompt] ", tool_result)
            messages.append(tool_result)

        # Second call (with function calling results)
        ret2 = model_with_tool.invoke(messages)
        return ret2.content

    def ask_with_embedding(self, prompt, index: VectorstoreIndexCreator):
        return index.query(prompt, self.model)

    def execute_embedding(self, data: list[str]) -> VectorstoreIndexCreator:
        docs = []
        for d in data:
            docs.append(Document(d))
        index = VectorstoreIndexCreator(
            vectorstore_cls=InMemoryVectorStore,
            embedding=OpenAIEmbeddings(model=self.embedding_model_name),
        ).from_documents(docs)
        return index

    def __find_first_tool_by_name(self, tools: list[BaseTool], name: str):
        return next((f for f in tools if f.name == name))
