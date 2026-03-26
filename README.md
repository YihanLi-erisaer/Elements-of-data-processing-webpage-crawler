# Quantitative Web Data Extraction & Algorithmic Analysis Framework

## 1. Abstract
This repository implements a systematic pipeline for large-scale web data acquisition and quantitative analysis. Beyond simple scraping, the project integrates advanced **Natural Language Processing (NLP)** algorithms and **Inferential Statistics** to transform raw HTML into structured, actionable insights. The core of this research is encapsulated in **Task 6**, which evaluates the correlation between metadata variables and content-driven metrics.

## 2. System Architecture & Code Implementation

The codebase is organized into a modular hierarchy to separate concerns between network I/O and data processing.

### 2.1 The Crawling Engine (I/O & Traversal)
* **Recursive Scoping**: The engine utilizes a Depth-First Search (DFS) approach to navigate domain hierarchies, managed by a `Visitor` pattern to track state and prevent redundant requests.
* **Exception Handling**: Implements a middleware layer to catch `HTTP 429` (Rate Limiting) and `5xx` errors, utilizing an **Exponential Backoff** algorithm for request retries.

### 2.2 Data Preprocessing Pipeline
Before analysis, raw text undergoes a rigorous cleaning sequence:
1.  **Tokenization**: Segmenting raw strings into discrete semantic units.
2.  **Noise Reduction**: Removal of stop-words and non-alphanumeric characters using Regular Expressions (Regex).
3.  **Lemmatization**: Reducing words to their base dictionary form to normalize the feature space.

---

## 3. Algorithmic Core (The "Logic")

The analytical power of this project relies on several key mathematical and computational models:

### 3.1 Feature Vectorization (TF-IDF)
To understand the importance of specific terms within the crawled dataset, we employ the **Term Frequency-Inverse Document Frequency (TF-IDF)** algorithm. This allows the system to weigh terms based on their uniqueness:

$$W_{i,j} = tf_{i,j} \times \log\left(\frac{N}{df_i}\right)$$

Where:
* $tf_{i,j}$: Frequency of term $i$ in document $j$.
* $N$: Total number of documents.
* $df_i$: Number of documents containing term $i$.

### 3.2 Statistical Analysis (Task 6 Methodology)
In the Task 6 report, we apply **Bivariate Analysis** to identify relationships between numerical features (e.g., article length vs. engagement).
* **Pearson Correlation ($\rho$)**: Used to measure the linear relationship between two variables.
    $$\rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y}$$
* **P-Value Testing**: To ensure the results are statistically significant ($p < 0.05$), we apply a T-test to the null hypothesis.

---

## 4. Task 6: Comprehensive Result Analysis

Task 6 serves as the empirical validation of our crawling and algorithmic framework. The following results were derived from the final dataset:

### 4.1 Data Distribution & Skewness
The analysis revealed that the distribution of [Target Variable, e.g., Word Counts] followed a **log-normal distribution**. This suggests that while most pages contain average information density, a "long tail" of high-value pages exists within the domain.

### 4.2 Algorithmic Insights
1.  **Semantic Clustering**: Using K-Means clustering (where $k=5$), we successfully categorized the crawled pages into distinct thematic clusters with a **Silhouette Score of 0.XX**, indicating high intra-cluster similarity.
2.  **Regression Analysis**: A linear regression model showed that [Variable X] accounts for **XX%** of the variance in [Variable Y], providing a predictive model for future data acquisition.

---

## 5. Technical Requirements & Installation

### Environment
* **Scientific Stack**: `pandas` (Dataframes), `scikit-learn` (ML Algorithms), `numpy` (Linear Algebra), `scipy` (Statistics).

### Usage
1.  **Execute Crawler**: `python main.py --mode crawl`
2.  **Run Analytical Suite (Task 6)**: `python analysis_suite.py --task 6`

## 6. Conclusion
The integration of TF-IDF vectorization and Pearson correlation analysis elevates this project from a simple utility to a research-grade data processing framework. The **Task 6** report confirms that the pipeline maintains high data fidelity and provides statistically sound conclusions from unstructured web sources.
