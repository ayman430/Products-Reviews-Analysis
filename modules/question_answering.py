import faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter
import numpy as np 
import pandas as pd
from langchain.prompts import PromptTemplate
from sentence_transformers import SentenceTransformer
import warnings
warnings.filterwarnings("ignore")

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# get llm model 
# api key
GOOGLE_API_KEY = 'AIzaSyA1JZtSuvWkn6S5UP0zgKVi698H2h2S0ww'
# create gemini-pro chat model 
q_a_llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=GOOGLE_API_KEY)

# embeddings model
embed_model = SentenceTransformer('intfloat/multilingual-e5-small')
# get data frame 
df = pd.read_csv('reviews.csv')
#create prompt 
template = """ You are helpful chatbot assistant you are given query {query} and context {context}/
you job is answer the query from the context, give a coherent and short answer./
if you don not know explain the context in short sentences./
for example if you don not find query answer in the context say:/
i don't have information about you question but context provide: then explain context 
"""
prompt = PromptTemplate(
    input_variables=['query', 'context'],
    template = template
)
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100
)

class QuestionAnswering:
    def __init__(self, llm, prompt, df, embedding_model, splitter):
        self.reviews_df = df
        self.prompt = prompt
        self.llm = llm
        self.embed_model = embedding_model
        self.splitter = splitter

        # Split reviews into chunks
        self.text_chunks = self.splitter.split_text(
            text=' '.join(self.reviews_df['reviews'])
        )

        # Compute embeddings for the text chunks
        self.embeddings = self.embed_model.encode(self.text_chunks).astype('float32')

        # Create FAISS index once
        d = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(d)
        self.index.add(self.embeddings)

    def question_answer(self, query_text):
        # Embedding query 
        query_embeds = self.embed_model.encode([query_text]).astype('float32')

        # Search for similar sentences
        distances, indices = self.index.search(query_embeds, k=7)

        # Get the most similar chunks
        most_similar_list = [self.text_chunks[i] for i in indices[0]]
        context = ' '.join(most_similar_list)

        # Prepare prompt
        prompt_value = self.prompt.format(query=query_text, context=context)

        # Invoke LLM to get the answer
        response = self.llm.invoke(prompt_value)

        return response.content

if __name__ == '__name__':
    print('take an object from class')
    q_a = QuestionAnswering(q_a_llm, prompt, df, embed_model, splitter)
    
    query_text = 'what is battery capacity?'
    print(f'query: {query_text}')

    answer = q_a.question_answer(query_text)
    print(f'answer: {answer}')