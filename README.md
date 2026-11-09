# Medication Information Translator

A beginner-friendly Python application that helps users understand
medication information in simple, everyday language. Users can search
for a medication, retrieve drug-label information, review warnings and
side effects, and ask an AI assistant to rewrite technical information
in a more accessible way.

The application also checks recent drug recall notices and warns users
when a searched medication appears in a recall or enforcement notice.

> **Important:** This project is for educational and informational
> purposes only. It is not a substitute for advice from a doctor or
> pharmacist, and it must not diagnose conditions or recommend starting,
> stopping, or changing medication.

## Features

-   **Medication lookup:** Search by medication name and retrieve
    available drug-label information.
-   **Plain-language explanations:** Use the Gemini API to rewrite
    technical medication information in clearer language.
-   **Key information display:** Present available usage instructions,
    warnings, side effects, and other label details.
-   **Recall awareness:** Check recent FDA drug recall and enforcement
    notices for relevant matches.
-   **Search history:** Save previous searches locally so users can
    review them later.
-   **Report saving:** Save generated reports or search results to local
    files.
-   **Input validation:** Handle empty searches, invalid medication
    names, and unexpected input.
-   **Error handling:** Gracefully handle API failures, missing results,
    network problems, and malformed responses.

## Suggested Technology Stack

  Area                 Technology
  -------------------- ------------------------------
  Language             Python
  User interface       Streamlit or Tkinter
  HTTP requests        Requests
  Data format          JSON
  AI translation       Gemini API
  Drug-label data      openFDA Drug Labeling API
  Recall information   openFDA Drug Enforcement API
  Local persistence    JSON or text files

Choose **Streamlit** for a browser-based interface that is quick to
build, or **Tkinter** for a traditional desktop application.

## Suggested APIs

### 1. openFDA Drug Labeling API

Use the drug-label endpoint to search for medication labeling
information, including available warnings, adverse reactions,
indications, and usage information.

Documentation: https://open.fda.gov/apis/drug/label/

Example endpoint:

``` text
https://api.fda.gov/drug/label.json
```

### 2. openFDA Drug Enforcement API

Use this endpoint to search FDA drug recall and enforcement reports.
Compare the searched medication against relevant recall records and show
the notice date, product description, reason, and status when available.

Documentation: https://open.fda.gov/apis/drug/enforcement/

Example endpoint:

``` text
https://api.fda.gov/drug/enforcement.json
```

### 3. Gemini API

Use Gemini to explain retrieved label content in plain language. Send
only the relevant information needed for the explanation, and instruct
the model not to add unsupported medical claims.

Documentation: https://ai.google.dev/gemini-api/docs

## How the Application Works

1.  The user enters a medication name.
2.  The application validates and cleans the input.
3.  The application requests matching drug-label records from openFDA.
4.  It extracts relevant fields, such as indications, dosage
    information, warnings, and adverse reactions, when present.
5.  The application checks openFDA enforcement records for possible
    recall matches.
6.  The retrieved information is sent to Gemini for a plain-language
    explanation.
7.  The interface displays the source information, AI explanation, and
    any possible recall alerts.
8.  The search and/or generated report is saved locally for later
    review.

## Getting Started

### Prerequisites

-   Python 3.10 or later
-   Internet access for API requests
-   A Gemini API key
-   Git (optional)

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd medication-information-translator
```

If you have not created a repository yet, create a project folder and
open a terminal in it.

### 2. Create and activate a virtual environment

``` bash
python -m venv .venv
```

Windows:

``` bash
.venv\Scripts\activate
```

macOS/Linux:

``` bash
source .venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` file with the packages your implementation
uses. For a Streamlit version, a starting point is:

``` text
streamlit
requests
google-genai
```

Then install them:

``` bash
pip install -r requirements.txt
```

For a Tkinter version, Tkinter is commonly included with standard Python
installations, though some Linux distributions package it separately.

### 4. Configure the Gemini API key

Create a `.env` file or use your deployment platform's secret manager.
Never commit API keys to source control.

Example `.env`:

``` text
GEMINI_API_KEY=your_api_key_here
```

If using environment variables, load the key securely in your
application. Add `.env` to `.gitignore`.

### 5. Run the application

For a Streamlit implementation:

``` bash
streamlit run app.py
```

For a Tkinter implementation, run the Python entry-point file, for
example:

``` bash
python app.py
```

The exact command depends on the filename and interface you implement.

## Suggested Project Structure

``` text
medication-information-translator/
â”œâ”€â”€ app.py                  # Application entry point and user interface
â”œâ”€â”€ medication.py           # Medication search and label parsing
â”œâ”€â”€ recall_checker.py       # Recall and enforcement lookups
â”œâ”€â”€ ai_translator.py        # Gemini API integration
â”œâ”€â”€ search_history.py       # Local search-history storage
â”œâ”€â”€ report_writer.py        # Save reports to local files
â”œâ”€â”€ requirements.txt        # Python dependencies
â”œâ”€â”€ .env                    # Local API key (do not commit)
â”œâ”€â”€ .gitignore
â”œâ”€â”€ README.md
â””â”€â”€ data/
    â””â”€â”€ search_history.json # Created by the application
```

This is a suggested structure; adapt it to the files in your actual
project.

## Python Concepts to Practice

-   **File handling:** Save search history and generated reports; read
    saved records when the application starts.
-   **Exception handling:** Handle invalid medication names, missing API
    results, request timeouts, connection errors, and invalid JSON.
-   **Regular expressions:** Normalize search terms and validate or
    clean medication-name input where appropriate.
-   **Object-oriented programming:** Create classes such as
    `Medication`, `FDAClient`, `AITranslator`, and `SearchHistory`.
-   **API integration:** Send HTTP requests, inspect status codes, parse
    JSON, and handle rate limits.
-   **Data validation:** Check for missing or empty fields before
    displaying results.

## Safety, Accuracy, and Privacy

-   Display the source and date of retrieved FDA information where
    available.
-   Make it clear that a missing recall match does **not** prove that a
    medication is free of recalls.
-   Recall searches may not identify every product variation,
    manufacturer, lot, or package. Avoid presenting a text match as a
    confirmed product-specific recall.
-   Preserve important warnings and qualifications when generating
    plain-language explanations.
-   Clearly distinguish original FDA label text from AI-generated
    explanations.
-   Do not let the AI invent dosage instructions, contraindications, or
    medical advice. If the source does not contain an answer, say that
    the information was not found.
-   Encourage users to confirm medication questions with a qualified
    healthcare professional.
-   Avoid storing personal or sensitive health information unless it is
    necessary, disclosed, and appropriately protected.
-   Keep API keys out of source code and version control.

## Testing Checklist

-   Search with a valid, common medication name.
-   Search with an unknown medication name.
-   Submit an empty search.
-   Test API timeouts and unavailable services.
-   Test responses with missing or empty label fields.
-   Test recall results with no matches and with possible matches.
-   Confirm that search history is saved and can be loaded again.
-   Confirm that generated explanations do not replace or contradict
    source warnings.
-   Verify that API keys are not exposed in logs, screenshots, or the
    repository.

## Future Improvements

-   Add filters for brand name, generic name, manufacturer, or dosage
    form.
-   Show direct links to the original FDA records.
-   Add export options such as PDF or CSV.
-   Add clearer recall matching using manufacturer and product details
    when available.
-   Add unit tests and automated API tests using mocked responses.
-   Improve accessibility and mobile layout.
-   Add timestamps and a configurable retention policy for local search
    history.

## Disclaimer

Medication information can change, and public API records may be
incomplete or delayed. This application is an educational tool, not a
medical device or a clinical decision-support system. Always read the
official medication information and consult a doctor or pharmacist for
personal medical guidance. For urgent symptoms or a suspected serious
reaction, seek appropriate medical care.
