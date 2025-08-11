# AI News Aggregator & Content Creator

This Streamlit application automatically fetches the latest AI news, generates summaries, and creates LinkedIn articles.

## Setup

1.  **Install Python:** Make sure you have Python 3.7+ installed.

2.  **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2.  Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).

## How to Use

1.  **Manage Sources:** Use the sidebar to add or remove news sources (URLs or RSS feeds).
2.  **Select Time Period:** Choose the time frame for news aggregation.
3.  **Generate Content:** Click the "Generate News Summary and Article" button.
4.  **Export:** Download the summary in your desired format (HTML, PDF, or Word).

## Deployment on Streamlit Cloud

1.  **Push to GitHub:** Create a GitHub repository and push your code.
2.  **Create a Streamlit Cloud Account:** Sign up at [streamlit.io/cloud](https://streamlit.io/cloud).
3.  **Deploy:** Click "New app" and connect your GitHub repository.

**Note on Automation:** To have this script run automatically on a daily basis on Streamlit Cloud, you would need to use an external scheduling service to trigger the app. A simpler approach for daily emails would be to run this script on a local machine or a server with a cron job.
