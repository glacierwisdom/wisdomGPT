from langchain_core.documents import Document

#from langchain.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import DashScopeEmbeddings
from langchain.schema import Document
from langchain.storage import InMemoryStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.retrievers import ParentDocumentRetriever
import uuid
from langchain.text_splitter import CharacterTextSplitter


class Memory:
    def __init__(self, path, name):
        # 配置 RecursiveCharacterTextSplitter，使用换行符作为主要分隔符
        child_splitter = RecursiveCharacterTextSplitter(
            separators=[
                "\n\n",
                "\n",
                " ",
            ],  # 设定分隔符的优先级，首先尝试段落分割，其次是换行，最后是空格
            chunk_size=200,  # 每个分割块的最大字符数
            chunk_overlap=20,  # 分割块之间的重叠字符数，确保上下文连贯
        )
        store = InMemoryStore()  # 父文档的存储层

        self.name = name
        # self.embedding_function = OpenAIEmbeddings()
        self.embedding_function = DashScopeEmbeddings(dashscope_api_key="your_dash_scope_embedding")
        self.chroma_client = Chroma(
            embedding_function=self.embedding_function,
            persist_directory=path,
            collection_name=name,
        )
        self.retriever = ParentDocumentRetriever(
            vectorstore=self.chroma_client,
            docstore=store,
            child_splitter=child_splitter,
        )
        self.last_id = None
        self.last_doc = None

    def query(self, text, n_results=5):
        results = self.chroma_client.similarity_search(query=text, k=n_results)
        return {"documents": results}

    def get_last_memory(self):
        return self.last_doc
        # if self.last_id is None:
        #     return "无"
        # else:
        #     documents = self.chroma_client.get(ids=[self.last_id])["documents"]
        #     # documents = self.chroma_client.get_by_ids([self.last_id])
        #     return documents[0] if documents else "无"

    def add(self, documents):
        docs = [
            Document(page_content=d.page_content, metadata=d.metadata)
            for d in documents
        ]
        self.last_doc = docs[-1]
        ids = [str(uuid.uuid4()) for _ in documents]
        self.last_id = ids[-1]
        self.retriever.add_documents(documents=docs, ids=ids)


if __name__ == "__main__":
    memo = Memory(path="./chromadb", name="memo")
    # memo.add(
    #     [
    #         Document(page_content="the document in english", metadata={}),
    #         Document(page_content="the document in chinese", metadata={}),
    #     ]
    # )
    print(memo.query("english document"))
    print(memo.get_last_memory())
