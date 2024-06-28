# Sentiment Analysis Project
This project explores sentiment analysis using natural language processing (NLP) techniques and machine learning models. The analysis involves evaluating the sentiment expressed in text data, focusing on understanding the polarity (positive, negative, neutral) of reviews.

## Technologies Used
### Python Libraries
* Pandas: Used for data manipulation and analysis.
* Numpy: Essential for numerical operations and array handling.
* Matplotlib: Used for data visualization, specifically for creating plots.
* Seaborn: Built on Matplotlib, used for statistical data visualization.
* NLTK (Natural Language Toolkit): Used for text processing tasks such as tokenization, tagging, and chunking.
* Transformers from Hugging Face: Used for leveraging pre-trained models like RoBERTa for sequence classification.

## Sentiment Analysis Techniques

### VADER (Valence Aware Dictionary and sEntiment Reasoner):
A lexicon and rule-based sentiment analysis tool specifically designed for social media texts.
VADER is a rule-based sentiment analysis tool specifically designed for social media texts. It does not require training on a specific dataset and instead relies on a sentiment lexicon and predefined rules:
#### Key Features:
* Lexicon-based: VADER uses a sentiment lexicon that contains words scored for their positivity, negativity, and neutrality based on human raters.
* Rule-based Analysis: It incorporates rules to handle punctuation, capitalization, degree modifiers (intensifiers), conjunctions, and emoticons to infer sentiment from text.
* Valence Scores: Each word in VADER's lexicon is associated with a sentiment score (positive, negative, neutral), and these scores are combined to compute a sentiment score for the entire text.
* Emphasis on Context: VADER considers context by adjusting sentiment scores based on special rules that account for negations and capitalizations.
#### Application in Sentiment Analysis:
* Usage: VADER is widely used for sentiment analysis tasks in social media monitoring, customer feedback analysis, and opinion mining due to its simplicity and effectiveness in handling informal and colloquial language.
* Output: Provides sentiment scores including a compound score (normalized weighted composite score), indicating the overall sentiment polarity of the text.
* Advantages: VADER works well in scenarios where context and nuances in sentiment expressions need to be captured quickly and efficiently without the need for extensive training data.

#### Comparative Analysis and Insights:
* Performance: RoBERTa generally outperforms VADER in tasks requiring nuanced understanding of sentiment, especially in formal texts or domains with specific terminology.
* Real-world Applications: VADER remains popular for real-time sentiment monitoring on social media platforms due to its efficiency and adaptability to informal language.






### RoBERTa (Robustly optimized BERT approach)
RoBERTa is a transformer-based model introduced by Facebook AI in 2019. It builds upon the architecture and pre-training methods of BERT (Bidirectional Encoder Representations from Transformers) but optimizes several key aspects:

#### Key Features:
* Pre-training Approach: RoBERTa uses larger batch sizes, more training data, and longer training times compared to BERT, resulting in improved performance on downstream tasks.
* Masked Language Model (MLM): Like BERT, RoBERTa is pre-trained on a masked language modeling objective, where it predicts masked tokens within sentences.
* Dynamic Masking: Unlike BERT, RoBERTa uses dynamic masking during pre-training, meaning it does not mask out tokens randomly but instead applies a different masking strategy to improve generalization.
* Sentence Order Prediction (SOP): RoBERTa does not perform next sentence prediction (NSP) during pre-training, focusing solely on MLM and achieving better performance by learning more robust sentence representations.

#### Application in Sentiment Analysis:
* Fine-tuning: RoBERTa can be fine-tuned on specific tasks, such as sentiment analysis, by adding a classification layer on top of its pre-trained weights.
* Output: For sentiment analysis, RoBERTa provides probabilities or scores for each class (positive, negative, neutral), allowing classification of text based on its sentiment.
* Advantages: RoBERTa excels in capturing context and semantics in text due to its deep bidirectional architecture, making it suitable for tasks requiring nuanced understanding of sentiment expressions.


## Key Insights
### Comparative Analysis:

* Compared sentiment scores derived from VADER and RoBERTa models against manually rated reviews.
* Identified instances where model predictions diverged significantly from human ratings, providing insights into model strengths and weaknesses.
### Visualization:
* Utilized Seaborn to create pair plots comparing sentiment scores across different models and actual review ratings.
* Visualized the distribution of sentiment scores for different star ratings, highlighting trends in positive, negative, and neutral sentiments.
### Learning Outcomes
#### Model Performance:
* Learned how different models interpret and score sentiment differently based on their training data and architectures.
* Explored nuances in sentiment analysis, such as handling sarcasm, context, and subjective language.
#### Data Preprocessing:
* Gained experience in preprocessing text data for sentiment analysis tasks, including tokenization, part-of-speech tagging, and handling special characters.
#### Technological Integration:
* Integrated state-of-the-art NLP models seamlessly into Python workflows using Hugging Face's Transformers library.
* Applied learned techniques to real-world datasets, enhancing understanding of practical applications of sentiment analysis in industry.
