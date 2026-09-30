# Assignment 2

## 1. Self Rating

LLM: B  
Deep Learning: C  
AI: B  
ML: B  

I have basic knowledge of AI and ML and I am currently improving my practical skills. I understand the basic concepts of LLMs, prompts, embeddings and RAG. I have limited practical experience with Deep Learning, so I rated myself C.


## 2. LLM Chatbot Architecture

The main components of an LLM chatbot are:

- User Interface
- Backend/API
- LLM
- Prompt
- Conversation History
- Database
- Vector Database (if using RAG)

Basic flow:

User → Backend → Prompt + Context → LLM → Response → User

For a chatbot using company documents, I would use RAG. The documents are converted into embeddings and stored in a vector database. When the user asks a question, relevant information is retrieved and given to the LLM to generate the answer.


## 3. Vector Databases

A vector database stores data as vectors (embeddings) and helps find similar information based on meaning rather than exact keywords.

For example, I can use it for a college chatbot that answers questions from college documents and notices.

I would choose PostgreSQL with pgvector because it supports both normal database operations and vector search in the same database. It would be simple to manage for a small or medium-sized application.

Other options include Pinecone, Milvus and Weaviate.