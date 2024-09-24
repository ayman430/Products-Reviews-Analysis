# Product Reviews Analysis

This project provides a dynamic platform for analyzing product reviews. It includes visual insights through graphs, summaries of both negative and positive reviews, and an advanced question-answering feature. The system allows users to ask specific questions about products, making it a comprehensive tool for customer review analysis.

## Features

1. **Review Visualizations**: Display word clouds and count plots to analyze the frequency of words in negative and positive reviews.
2. **Review Summarizations**: Get concise summaries of both negative and positive reviews.
3. **Question Answering**: Ask specific questions about the product based on the available review data and receive short, coherent answers.

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




  


  
