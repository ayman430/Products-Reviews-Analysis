from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Load a pre-trained text classification pipeline (e.g., for sentiment analysis)
import pandas as pd
from transformers import pipeline
classifier = pipeline('sentiment-analysis')

class ProductReviewScraper:
    def __init__(self, product_url):
        self.product_url = product_url
        self.web = None
        self.reviews_list = []
        self.labels_list = []
        self.product_name = None
    
    def start_browser(self):
        # Initialize the browser
        self.web = webdriver.Chrome()
    
    def load_product_page(self):
        # Load the product page and get the product name
        self.web.get(self.product_url)
        product_element = WebDriverWait(self.web, 10).until(
            EC.presence_of_element_located((By.ID, 'productTitle'))
        )
        self.product_name = product_element.text
    
    def navigate_to_reviews_page(self):
        # Navigate to the reviews page (if possible)
        try:
            reviews_page_button_element = WebDriverWait(self.web, 60).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'See more reviews'))
            )
            reviews_page_button_element.click()
        except:
            print("Unable to find 'See more reviews' button or reviews are on the same page.")
    
    def get_total_reviews_and_pages(self):
        # Get total number of reviews and pages
        num_pages_elements = WebDriverWait(self.web, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="filter-info-section"]/div'))
        )
        pages_number = int(num_pages_elements.text.split(',')[1].split(' ')[1])
        total_reviews = int(num_pages_elements.text.split(',')[1].split(' ')[1])
        return pages_number, total_reviews
    
    def scrape_reviews(self):
        # Scraping reviews and handling pagination
        page_num = 1
        pages_number, _ = self.get_total_reviews_and_pages()
        current_page_url = self.web.current_url
        modified_url = current_page_url.replace("all_reviews", "all_reviews&pageNumber=0")
        
        while page_num <= (pages_number // 10):
            modified_url = modified_url.replace(f"pageNumber={page_num-1}", f"pageNumber={page_num}")
            self.web.get(modified_url)
            
            try:
                reviews_elements = WebDriverWait(self.web, 5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'a-size-base.review-text.review-text-content'))
                )
            except:
                page_num += 1
                continue
            
            for r in reviews_elements:
                self.reviews_list.append(r.text)
                class_result = classifier(r.text)             
                if class_result[0]['label'] == 'POSITIVE':
                    self.labels_list.append(1)
                else:
                    self.labels_list.append(0)
            
            print(f'Page Number: {page_num}')
            print(f'-----> Total reviews: {len(self.reviews_list)}')
            page_num += 1
    
    def quit_browser(self):
        # Quit the browser
        self.web.quit()
    
    def scrape_product_reviews(self):
        # High-level function to orchestrate the review scraping process
        try:
            self.start_browser()
            self.load_product_page()
            self.navigate_to_reviews_page()
            self.scrape_reviews()
            
            df = pd.DataFrame(
                {
                    'reviews': self.reviews_list,
                    'labels': self.labels_list
                }
            )
            df.to_csv('reviews.csv')
            return df, self.product_name
        finally:
            self.quit_browser()
 
if __name__ == "__main__":
    product_url = "https://www.amazon.com/SAMSUNG-Unlocked-Smartphone-Expandable-Security/dp/B0CN1QSH8Q/ref=nav_signin?ie=UTF8&th=1"
    scraper = ProductReviewScraper(product_url)
    df, product_name = scraper.scrape_product_reviews()
    print(f"Scraped {len(df)} reviews for product: {product_name}")
