
# GenQuery 2.0: Simplify Your SQL Journey

Welcome to GenQuery! This project aims to simplify data access and manipulation in SQL databases through natural language commands, educational examples, and powerful AI integration.

![gif](https://github.com/user-attachments/assets/733619ed-c962-4d83-a697-a5053fc9a406)

## Features

### 1. Natural Language SQL Query Generation
- **Query Simplification:** Generate SQL queries by simply typing your request in plain language.
- **Output Understanding:** Receive explanations for each query, breaking down the syntax and logic used.

### 2. SQL Formatter
- **Code Organization:** Format and clean up your SQL code for better readability and maintenance.

### 3. Query Explainer
- **Detailed Breakdown:** Analyze complex SQL queries with explanations for each component, making them easier to understand.

### 4. Data Analysis & Visualization
- **Visual Insights:** Generate charts and visualizations directly from your queries to better understand your data.

## Built With

![Tools](https://github.com/user-attachments/assets/ea5ecce3-b19f-4231-89c8-d867dc0a9601)

- **Languages:** Python
- **Frameworks:** Streamlit
- **Cloud Services:** Google Cloud Platform (GCP)
- **Databases:** SQLite
- **APIs:** Gemini 1.5 Pro API
- **Data Visualization:** Plotly Express
- **AI & NLP:** Google’s Generative AI tools

![Data Analysis & Visualization](https://github.com/user-attachments/assets/9a7a7086-54b9-4785-ba0e-63c0150c6a70)

## Project Architecture

- **Frontend:** Built with Streamlit for a user-friendly interface.
- **Backend:** Powered by Python and integrated with the Gemini 1.5 Pro API for AI capabilities.
- **Database:** Managed with SQLite, ensuring lightweight and efficient data management.

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/aniketandhale08/GenQuery-2.0
    ```
    ```bash
    cd GenQuery-2.0
    ```

2. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up SQLite Database:**
    - No additional setup is required for SQLite; it is lightweight and runs locally by default.

4. **Environment Variables:**
    ```bash
    export GOOGLE_API_KEY=your_google_api_key
    ```

5. **Run the Application:**
    ```bash
    streamlit run app.py
    ```
    - This will launch a web app in your default browser, usually at http://localhost:8501.

## Testing Instructions

1. **Access the Application:** Follow the setup instructions to run the application locally.
2. **Database Connection:** Ensure that SQLite is correctly configured and accessible.
3. **Run Queries:** Input natural language commands and observe the generated SQL queries and their explanations.
4. **Test Features:** Use the SQL Formatter and Query Explainer to test formatting and query explanation functionalities.

## Challenges and Learnings

1. **Integration:** Successfully integrated SQLite with the AI-powered GenQuery to manage data efficiently.
2. **User Experience:** Focused on making the tool beginner-friendly while maintaining powerful features for advanced users.

## Future Enhancements

1. **User Feedback Integration:** Gather user feedback to further improve the tool.
2. **Expanded Features:** Plan to add more data visualization options and AI-driven insights.
