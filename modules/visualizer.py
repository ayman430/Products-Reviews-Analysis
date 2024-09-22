
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class ReviewVisualizer:
    def __init__(self, reviews_df):
        self.reviews_df = reviews_df

    def create_countplot(self):
        plt.figure(figsize=(6, 4))
        ax = sns.countplot(x='labels', data=self.reviews_df)

        # Calculate and annotate percentages
        total = len(self.reviews_df)
        for p in ax.patches:
            count = p.get_height()
            percentage = f'{count / total * 100:.2f}%'
            ax.annotate(percentage, (p.get_x() + p.get_width() / 2., count),
                        ha='center', va='baseline', fontsize=12, color='black')

        # Set labels
        ax.set_xticklabels(['Negative', 'Positive'])
        plt.title('Count and Percentage of Labels')
        plt.xlabel('Sentiment Label')
        plt.ylabel('Count')

        # Show plot
        plt.show()

    def neg_word_cloud(self):
        # Get negative reviews
        negative_reviews = ' '.join(self.reviews_df[self.reviews_df['labels'] == 0]['reviews'])
        
        # Generate word cloud
        wordcloud_negative = WordCloud(width=800, height=400, background_color='white').generate(negative_reviews)
        
        # Plot the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud_negative, interpolation='bilinear')
        plt.title('Negative Reviews')
        plt.axis('off')
        plt.show()

    def pos_word_cloud(self):
        # Get positive reviews
        positive_reviews = ' '.join(self.reviews_df[self.reviews_df['labels'] == 1]['reviews'])
        
        # Generate word cloud
        wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_reviews)
        
        # Plot the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud_positive, interpolation='bilinear')
        plt.title('Positive Reviews')
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    # get df
    reviews_df = pd.read_csv('F:\Projects\Products-Reviews-Analysis\\reviews.csv')
    visualizer = ReviewVisualizer(reviews_df)
    
    # Generate count plot
    visualizer.create_countplot()

    # Generate word clouds
    visualizer.neg_word_cloud()
    visualizer.pos_word_cloud()
