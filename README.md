# Product Reviews Analysis

This project provides a dynamic platform for analyzing product reviews. It includes visual insights through graphs, summaries of both negative and positive reviews, and an advanced question-answering feature. The system allows users to ask specific questions about products, making it a comprehensive tool for customer review analysis.

## Features

1. **Review Visualizations**: Display word clouds and count plots to analyze the frequency of words in negative and positive reviews.
2. **Review Summarizations**: Get concise summaries of both negative and positive reviews.
3. **Question Answering**: Ask specific questions about the product based on the available review data and receive short, coherent answers.

## Tech Stack

This project utilizes a variety of libraries and tools to achieve its functionalities. Below is a list of the primary libraries used:

- **FastAPI**: For building the web API endpoints that serve the review analysis, summarization, and question-answering functionalities.
- **Uvicorn**: An ASGI server used to run the FastAPI application.
- **Pandas**: For loading, manipulating, and processing the reviews data.
- **WordCloud**: For generating word clouds that visualize the most common words in positive and negative reviews.
- **Seaborn** and **Matplotlib**: For creating visualizations such as count plots of review distributions.
- **LangChain**: To handle complex language models and enable prompt management for the question-answering service.
- **LangChain Google GenAI**: To utilize the Gemini model as the large language model (LLM) for advanced language understanding and response generation.
- **Selenium**: For scraping product reviews data from various sources.
- **Transformers**: For sentiment analysis of the reviews, classifying them as positive, negative, or neutral.
- **FAISS**: For efficient similarity search and clustering of the reviews data based on text embeddings.
- **Sentence Transformers**: For generating embeddings of the text chunks to enable the question-answering service.
- **NumPy**: For numerical operations and handling arrays of embeddings and other data.

## API Endpoints
![main](https://github.com/user-attachments/assets/4693a3de-4fc7-4013-b073-1687c418df2e)

### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: A welcome message to confirm that the API is running.
- **Response**:
  ```json
  {
    "message": "Welcome to the Review Analysis API"
  }

### Question Answering

- **URL**: `/QuestionAnswering`
- **Method**: `POST`
- **Description**: Ask specific questions about the product based on review data and receive short, coherent answers.

- **Exmple 1**:
  ![image](https://github.com/user-attachments/assets/960ed816-6d45-4f5c-a4b7-d04223409e34)

- **Exmple 2**:
![image](https://github.com/user-attachments/assets/265240bf-92e0-4a4e-b71b-2e01e48cb5a3)

- **Exmple 3**:
![Screenshot_24-9-2024_184137_127 0 0 1](https://github.com/user-attachments/assets/806faf58-440a-4f38-8d00-01ee862f024d)

### Count Plot

- **URL**: `/plot-count`
- **Method**: `GET`
- **Description**: Generate a count plot that visualizes the distribution of positive and negative reviews.

- **Response**:
  - Displays a count plot in your browser that shows the number of positive and negative reviews.

   #### Output Image:
  ![count_plot](https://github.com/user-attachments/assets/d39b7827-0bc3-4907-8117-f3fa1c45b4b7)

  
  - **Example Response**:
    ```json
    {
      "message": "Count plot displayed"
    }
### Positive Word Cloud

- **URL**: `/wordcloud-positive`
- **Method**: `GET`
- **Description**: Generate a word cloud visualization for the most frequently used words in positive reviews.

- **Response**:
  - Displays a word cloud in your browser highlighting the most common words in positive reviews.

- **Example Response**:
  ```json
  {
    "message": "Positive word cloud displayed"
  }


####  Output Image:
![pos_cloud](https://github.com/user-attachments/assets/6b80f51c-f614-4f3f-ad80-3763edb34a58)

## Positive Reviews Summarization

The API provides a summarization service for positive reviews. This endpoint generates a concise summary of the main points from all positive reviews in the dataset.

### Endpoint

- **URL**: `/summarize/positive`
- **Method**: `GET`
- **Response**:
  - **summary**: A concise summary of the most relevant points from positive reviews.
```json 
{
  "summary": [
    "This phone is amazingly cheap but it still works well. It has a great camera and is lightweight. It is very secure and has a great scratch-resistant screen.",
    "The A15 is considerably heavier compared to the A10E, which has 32 GB of internal memory, while the A15 has 128 GB.",
    "Compared to the Galaxy S9, the A15 is impressive at its price point, adding 5G, a bigger screen, and better cameras.",
    "Upgrading from a Samsung Galaxy J7 to the A15 has provided a significant increase in memory and performance.",
    "The phone weighs 7.57 oz and has dimensions of 6 ¼” x 3”.",
    "Performance has slowed over the months, but it has 128 GB of internal storage and adequate sound quality.",
    "The solid build quality features a matte iridescent case that resists fingerprints and an AMOLED screen with vibrant colors.",
    "As an entry-level phone, it offers great specifications including long battery life, fingerprint unlock, three cameras, and good software support."
  ]
}





  


  
