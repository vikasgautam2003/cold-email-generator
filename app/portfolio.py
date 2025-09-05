# import os
# import pandas as pd
# import chromadb
# import uuid


# class Portfolio:
#     def __init__(self, file_path=None):
#         if file_path is None:
#             file_path = os.path.join(os.path.dirname(__file__), "resource", "my_portfolio.csv")
#         self.file_path = file_path
#         self.data = pd.read_csv(self.file_path)
#         self.chroma_client = chromadb.PersistentClient('vectorstore')
#         self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

#     def load_portfolio(self):
#         if not self.collection.count():
#             for _, row in self.data.iterrows():
#                 doc_text = str(row["Techstack"])  # ensure string
#                 self.collection.add(
#                     documents=[doc_text],
#                     metadatas=[{"links": row["Links"]}],
#                     ids=[str(uuid.uuid4())]
#                 )

#     def query_links(self, skills):
#         # If skills is a single string, wrap in list; if list, convert all items to str

#         if isinstance(skills, str):
#             query_list = [skills]
#         else:
#             query_list = [str(s) for s in skills]
#         return self.collection.query(query_texts=query_list, n_results=2).get('metadatas', [])









import os
import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path=None):
        if file_path is None:
            file_path = os.path.join(os.path.dirname(__file__), "resource", "my_portfolio.csv")
        self.file_path = file_path
        self.data = pd.read_csv(self.file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                doc_text = str(row["Techstack"])
                self.collection.add(
                    documents=[doc_text],
                    metadatas=[{"links": row["Links"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        if isinstance(skills, str):
            query_list = [skills]
        else:
            query_list = [str(s) for s in skills]
        return self.collection.query(query_texts=query_list, n_results=2).get('metadatas', [])
