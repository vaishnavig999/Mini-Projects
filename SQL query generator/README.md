## SQL Query Generator with Streamlit and Google AI

This project empowers you to generate SQL queries effortlessly using natural language descriptions. It leverages Streamlit for the user interface and Google GenerativeAI for text generation.

### Requirements

- Python 3.9.2
- Streamlit (`pip install streamlit`)
- Google GenerativeAI library (`pip install google-generativeai`)

**Important:** Replace the placeholder `GOOGLE_API_KEY` in the code with your own API key obtained from Google Cloud(`https://aistudio.google.com/app/apikey`)

### Running the application

1. Save the code as `sql_generator.py`.
2. Install the necessary libraries:
   - If you have a `requirements.txt` file listing dependencies, run:
     ```bash
     pip install -r requirements.txt
     ```
   - Otherwise, install individually:
     ```bash
     pip install streamlit google-generativeai
     ```
3. To view this Streamlit app on a browser, run it with the following
  command:
    `streamlit run sql_generator.py`

### How to use

1. Open your web browser and navigate to `http://localhost:8501`.
2. Provide the query details in the designated text area.
3. Click the "Generate" button.
4. The generated SQL code will be displayed alongside a glimpse of the expected output.
5. You can expand the sections for "Expected Output" and "Explain SQL Query" to gain further details about the query.
