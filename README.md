# LLM2SQL - Google Gemini

## Acknowledgement
I would like to extend my sincere thanks to  [Krish Naik](https://github.com/krishnaik06)  for his invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without his educational resources.

<br>

## About the Project
Developed a LLM-driven application that transforms natural language queries into executable SQL using **Google Gemini**, querying a custom-built [**SQLite**](https://www.sqlite.org/) database. The app features a responsive **Streamlit UI** that returns generated SQL query results in real time. This project showcases seamless integration of generative AI with structured data systems—democratizing database access with conversational intelligence.

<br>

## How to Run the Project ?
### **1. Clone the Repository**
Clone the repository to your local machine :
```bash
 git clone https://github.com/SoubhikSinha/LLM2SQL-Gemini.git
```

<br>

### **2. Create a Virtual Environment**
Navigate to the repository's root directory and create a Conda virtual environment :
```bash
conda create --prefix ./venv python=3.11 -y
```

<br>

### **3. Activate the Conda Environment**
Activate the newly created environment :
```bash
conda activate venv/
```

<br>  

### **4. Install Required Libraries**
Install all the necessary dependencies :
```bash
pip install -r requirements.txt
```

<br>

### **5. Set Up Google API Key**
Create and paste your Google API key inside  `.env`  file (if not created, create one). Get your API key from  [Google AI Studio](https://aistudio.google.com/app/apikey).

Example  `.env`  file content :
```bash
GOOGLE_API_KEY="your_api_key_here"
```

<br>

### **6. Create the SQL database**
Run the below command to create the pre-defined database :
```bash
python sql.py
```

<br>

### **7. Run the Application**
Start the Streamlit application by running :
```bash
streamlit run app.py
```

<br>

### **8. Play Around !**
Explore the capabilities of **LLM2SQL** and experience the power of natural language querying. Simply enter your questions in plain English and watch the app convert them into SQL queries, fetch results from the database, and display insights instantly—all through an intuitive Streamlit interface.
