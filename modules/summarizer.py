from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import pandas as pd

# get llm model 
# api key
GOOGLE_API_KEY = 'AIzaSyA1JZtSuvWkn6S5UP0zgKVi698H2h2S0ww'
# create gemini-pro chat model 
llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=GOOGLE_API_KEY)

prompt = PromptTemplate(
    input_variables = ['text'], 
    template = """You are helpful text summmarizer take a text /
    and summarize important points on it in a set of sequence steps,/
    return formate like this: 
    most important points in the text are:
    1-
    2- 
    ..
    ..
    .. 
    n- 
    each point not be more than 2 lines
    %input% : {text}
    """
)

class ReviewSummarizer:
    def __init__(self, reviews_df, prompt, llm):
        self.reviews_df = reviews_df
        self.prompt = prompt
        self.llm = llm

    def summarization_negative_reviews(self):
        # Join negative reviews
        negative_reviews = ' '.join(self.reviews_df[self.reviews_df['labels'] == 0]['reviews'])

        # Format prompt with negative reviews
        prompt_value = self.prompt.format(text=negative_reviews)

        # Stream and print the summarization output
        # for chunk in self.llm.stream(prompt_value):
        #     print(chunk.content, end='', flush=True)
        response = self.llm.invoke(prompt_value)
        return response.content

    def summarization_positive_reviews(self):
        # Join positive reviews
        positive_reviews = ' '.join(self.reviews_df[self.reviews_df['labels'] == 1]['reviews'])

        # Format prompt with positive reviews
        prompt_value = self.prompt.format(text=positive_reviews)

        # Stream and print the summarization output
        # for chunk in self.llm.stream(prompt_value):
        #     print(chunk.content, end='', flush=True)
        response = self.llm.invoke(prompt_value)
        return response.content


if __name__ == "__main__":
    # df
    reviews_df = pd.read_csv('F:\Projects\Products-Reviews-Analysis\\reviews.csv')

    summarizer = ReviewSummarizer(reviews_df, prompt, llm)
    
    # Summarize negative reviews
    # summarizer.summarization_negative_reviews()

    # Summarize positive reviews
    summarizer.summarization_positive_reviews()
