import uvicorn
from fastapi import FastAPI, BackgroundTasks
from typing import Generator
from pydantic import BaseModel
import pandas as pd
from modules.visualizer import ReviewVisualizer
from modules.summarizer import ReviewSummarizer, llm, prompt
from modules.question_answering import QuestionAnswering,  embed_model, prompt as qa_prompt, splitter, q_a_llm

class QuestionResponse(BaseModel):
    query_text: str

# load data frame
reviews_df = pd.read_csv('reviews.csv')

# Initialize objects
visualizer = ReviewVisualizer(reviews_df)
summarizer = ReviewSummarizer(reviews_df, prompt, llm)
q_a_model   = QuestionAnswering(q_a_llm, qa_prompt, reviews_df, embed_model, splitter)

# create object from fastapi
app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Welcome to the Review Analysis API'}

@app.get("/plot-count")
async def plot_count():
    # Use the visualizer to create a count plot
    visualizer.create_countplot()
    return {"message": "Count plot displayed"}

@app.get("/wordcloud-negative")
async def wordcloud_negative():
    # Generate word cloud for negative reviews
    visualizer.neg_word_cloud()
    return {"message": "Negative word cloud displayed"}

@app.get("/wordcloud-positive")
async def wordcloud_positive():
    # Generate word cloud for positive reviews
    visualizer.pos_word_cloud()
    return {"message": "Positive word cloud displayed"}

@app.get("/summarize/negative")
async def summarize_negative():
    summary = summarizer.summarization_negative_reviews()
    return {"summary": summary}

@app.get("/summarize/positive")
async def summarize_positive():
    summary = summarizer.summarization_positive_reviews()
    return {"summary": summary}

@app.post('/QuestionAnswering')
async def q_a_endpoint(query: QuestionResponse):
    # Extract the query text from the request body
    query_text = query.query_text

    # Call the question_answer method of your model
    answer = q_a_model.question_answer(query_text)

    # Return the answer as a JSON response
    return {"query": query_text, "answer": answer}



