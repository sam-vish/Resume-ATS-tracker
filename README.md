
# Smart ATS (Applicant Tracking System)

Smart ATS is a web application designed to help job seekers improve their resumes by comparing them against specific job descriptions. Using advanced generative AI technology, Smart ATS evaluates resumes and provides feedback on match percentage and missing keywords, aiding applicants in enhancing their resumes for better compatibility with applicant tracking systems used by employers.

## Features

- **Resume Analysis**: Analyze uploaded resumes against job descriptions to find the match percentage.
- **Keyword Identification**: Identify missing keywords that are crucial for the job application.
- **AI-Driven Insights**: Get insights and suggestions powered by Gemini AI to improve the resume.

## Installation

To set up Smart ATS, follow these steps:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/smart-ats.git
   ```

2. Navigate to the project directory:

   ```
   cd smart-ats
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Smart ATS application, execute the following command:

```
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to interact with the application.

## How It Works

1. **Upload Resume**: Users upload their resume in PDF format.
2. **Enter Job Description**: Users input the job description against which they want to compare their resume.
3. **Analysis and Feedback**: The application analyzes the resume, compares it with the job description, and provides a detailed report, including match percentage and missing keywords.

## Technology Stack

- **Streamlit**: For creating the web application.
- **PyPDF2**: To extract text from PDF files.
- **Google Generative AI**: For generating content and providing insights based on the resume and job description.

## Configuration

Before running the application, ensure that the Google API key is set in your environment variables. The `.env` file should contain:

```
GOOGLE_API_KEY=your_api_key_here
```

Load the API key in the application using the `dotenv` package.

## Contributing

Contributions to Smart ATS are welcome! Please feel free to submit pull requests, create issues, or suggest improvements.

