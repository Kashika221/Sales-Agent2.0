# Sales-Agent2.0

An interactive AI-powered **Sales Agent** chatbot built with **Streamlit** and **Google’s Gemini generative model**. This application simulates a guided sales conversation — asking user questions about product needs, budget, features, and concerns — and returns AI-generated recommendations and responses.

## Table of Contents

* Overview
* Features
* Demo (Local)
* Requirements
* Installation
* Usage
* How It Works
* Project Structure
* Output Artifacts
* Customization
* Troubleshooting
* License

---

## Overview

**Sales-Agent2.0** is a conversational interface that functions as a basic sales agent for recommending products (e.g., phones or SaaS plans) based on user inputs. It uses the Google Generative AI API (Gemini-2.0 Flash) to generate dynamic responses in a stepwise sales dialogue. Responses and user messages are logged and can be exported to CSV/JSON for later analysis.

---

## Features

* Interactive multi-step sales conversation (name, product need, budget, key features, objections)
* AI-generated responses using the **Gemini-2.0 Flash** model
* Built with **Streamlit** for rapid GUI deployment
* Stores session logs and exports conversation transcripts as:

  * CSV
  * JSON

---

## Demo (Local)

Run the app locally and interact with it in your browser:

```bash
streamlit run app.py
```

You will see an AI Sales Agent UI that prompts you for information step by step.

---

## Requirements

This project requires:

* **Python 3.8+**
* A valid **Google Generative AI API Key**
* Internet access to query the AI service

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kashika221/Sales-Agent2.0.git
   cd Sales-Agent2.0
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   Create a `requirements.txt` with the necessary packages:

   ```
   streamlit
   google-generativeai
   pandas
   ```

   Then install:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**

   Set an environment variable `API_KEY` with your Google Generative AI key:

   ```bash
   export API_KEY="YOUR_API_KEY"        # macOS / Linux
   setx API_KEY "YOUR_API_KEY"          # Windows Powershell
   ```

---

## Usage

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Interact with the sales agent dialog in your browser:

   * Provide your **name**
   * Choose a product type (e.g., phone or SaaS plan)
   * Enter budget and desired features
   * Raise any objections or questions
   * The AI will respond accordingly

3. At the end of the conversation, two files are generated with your session log:

   * `<Name>_chat.csv`
   * `<Name>_chat.json`

---

## How It Works

* **Session State:** Uses `st.session_state` to maintain conversation history, current step, logs, and user metadata.
* **AI Interaction:** Calls Google’s generative model (`gemini-2.0-flash`) through the `google.generativeai` package to produce replies based on dynamic prompts.
* **Prompt Flow:** A static list of prompts guides the conversation stages (greeting, needs, budget, features, concerns).
* **Logging:** Each user message and AI answer is appended to an in-memory log and saved at the end of the session.

---

## Project Structure

```
Sales-Agent2.0/
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python package dependencies
├── <Name>_chat.csv / JSON     # Generated logs after conversation
└── README.md                  # This documentation
```

---

## Output Artifacts

After a session completes, the app writes:

* **CSV transcript** (`<name>_chat.csv`)
* **JSON log** (`<name>_chat.json`)

These contain a structured record of all messages exchanged during the session.

---

## Customization

You can extend or refine the agent by:

* Adding more dialogue steps and product categories
* Incorporating retrieval or a product database
* Enhancing prompt templates with richer product context
* Using a different generative model or advanced fine-tuning

---

## Troubleshooting

* **API Key error**: Ensure `API_KEY` is correctly defined in your environment.
* **Streamlit UI not showing**: Confirm that Streamlit is installed and you are running `streamlit run app.py`.
* **Model errors**: Check network connectivity and API quota for your Google Generative AI key.

---

## License

This project does not include a license file. You may add one (for example MIT or Apache-2.0) based on how you want others to use your code.

---

If you want, I can generate a polished **requirements.txt** automatically from the imports in your `app.py`.
