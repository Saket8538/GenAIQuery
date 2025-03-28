
# GenAIQuery: Simplifying SQL for Everyone with AI-Powered Natural Language Queries and Seamless Data Visualization and Integrated AI chat for general queries.

Welcome to GenAIQuery! This project aims to simplify data access and manipulation in SQL databases through natural language commands, educational examples, and powerful AI integration.


## Features
Video link-https://www.loom.com/share/ae75b063988a4089b519769638a3d2bf?sid=418c3ecc-74f8-426b-8bfb-7ec72a83f8ed
### 1. Natural Language SQL Query Generation
- **Query Simplification:** Generate SQL queries by simply typing your request in plain language.
- **Output Understanding:** Receive explanations for each query, breaking down the syntax and logic used.

### 2. SQL Formatter
- **Code Organization:** Format and clean up your SQL code for better readability and maintenance.

### 3. Query Explainer
- **Detailed Breakdown:** Analyze complex SQL queries with explanations for each component, making them easier to understand.

### 4. Data Analysis & Visualization
- **Visual Insights:** Generate charts and visualizations directly from your queries to better understand your data.

### 5. AI Chat
- **Code Generation & Chat:** Chat and generate code with LLM powere Azure OpenAI.


## Built With
![tools](https://github.com/Saket8538/GenAIQuery/blob/main/Media/azureopenai.jpeg)
![python,sqllite](https://github.com/Saket8538/GenAIQuery/blob/main/Media/sqllite%2Cpython.jpeg)
- **Languages:** Python
- **Frameworks:** Streamlit
- **Cloud Services:** Microsoft Azure
- **Databases:** SQLite
- **APIs:** Azure OpenAI API
- **Data Visualization:** Plotly Express
- **AI & NLP:** Azure Responsible AI

![dbschema](https://github.com/Saket8538/GenAIQuery/blob/main/Media/ER-diagram.png)
![visualisation](https://github.com/Saket8538/GenAIQuery/blob/main/Media/Data%20Analysis%20%26%20Visualization.png)

## Project Architecture

- **Frontend:** Built with Streamlit for a user-friendly interface.
- **Backend:** Powered by Python and integrated with the Azure OpenAI API for AI capabilities.
- **Database:** Managed with SQLite, ensuring lightweight and efficient data management.

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Saket8538/GenAIQuery.git
    ```
    ```bash
    cd GenAIQuery
    ```

2. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up SQLite Database:**
    - No additional setup is required for SQLite; it is lightweight and runs locally by default.

4. **Environment Variables:**
    ```bash
    export AZURE_OPENAI_ENDPOINT=https://your-azure-openai-endpoint.openai.azure.com/
    export AZURE_OPENAI_KEY=your_azure_openai_api_key
    export AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
    ```

5. **Run the Application:**
    ```bash
    python -m streamlit run app.py
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
