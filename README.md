# 🏥 Medical Protocol and Health Navigation Agent

### 🌐 Project Overview
The **Medical Protocol and Health Navigation Agent** is an **AI-based medical assistant** designed to help users understand their symptoms, explore possible medical protocols, and connect to nearby doctors or hospitals.  

The system uses an **agentic workflow** approach where the AI analyzes user input (symptoms), summarizes relevant medical guidelines, evaluates the risk, and suggests the next steps — such as seeking emergency care or booking a doctor’s appointment.

---

### 🧩 Work Completed So Far

#### ✅ 1. Project Proposal Implementation
The following components from the approved proposal have been successfully implemented:

- **Frontend UI (HTML/CSS/JS):**
  - A clean and responsive web interface for symptom input and displaying medical summaries.
  - Features include input forms, risk display (high/low), structured summaries, and doctor listings.

- **Backend Integration (Flask):**
  - A Flask API endpoint `/analyze` processes user input.
  - It communicates with the **Groq API (Llama-3.3-70B model)** to perform symptom reasoning and structured summarization.

- **AI Response Formatting:**
  - The system now provides clearly formatted protocol summaries, including:
    - Possible Causes  
    - Risk Level  
    - Care Guidelines  

- **Risk Assessment:**
  - Conditional logic implemented:
    - If symptoms indicate high-risk → Emergency prompt  
    - Else → Standard care guidance and appointment suggestion  

- **Doctor Data Integration:**
  - Doctor details are fetched from a **custom dataset created through web scraping**.
  - The data was collected from the **official Goa government medical directory website**.
  - This dataset includes:
    - Doctor Name  
    - Specialty  
    - Address  
    - Contact Number  

- **Data Storage:**
  - The web-scraped data is stored locally in a CSV file (`doctors_data.csv`) for use within the application.

- **Ethical Disclaimer:**
  - The frontend includes a visible disclaimer stating that the system does **not provide medical advice** and is meant for **guidance only**.

---

### 📊 Dataset Description

**Dataset Name:** `doctors_data.csv`  
**Source:** Official Goa Government Medical Directory (Web Scraped)  
**Method:** Web scraping using Python (BeautifulSoup / Requests)  

**Columns Included:**
| Column Name | Description |
|--------------|-------------|
| `name` | Doctor’s full name |
| `specialty` | Area of specialization (e.g., General Physician, Cardiologist) |
| `address` | Clinic/Hospital location |
| `phone_number` | Contact number for booking or inquiry |

**Purpose:**  
This dataset is used to display **verified and region-specific doctor information** based on the user's query and risk level.  

---

### ⚙️ System Workflow (As Implemented)

1. **User Input:**  
   The user enters their symptom (e.g., "fever" or "chest pain").  

2. **Agent Reasoning (Groq API):**  
   The system sends the input to Groq’s LLM model (Llama-3.3-70B) for interpretation and protocol reasoning.

3. **Structured Summarization:**  
   The AI returns a structured summary including causes, risk level, and recommended care.

4. **Decision Layer:**  
   - If “high-risk” → Show emergency warning and call button.  
   - Else → Show standard care and doctor directory.

5. **Action Layer:**  
   - Displays doctor details from the Goa dataset.  
   - Provides buttons to book an appointment or call emergency services.

6. **Output:**  
   The frontend displays a formatted, easy-to-read summary with actionable steps.

---

### 🧠 Technical Stack

| Component | Technology Used |
|------------|-----------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python) |
| **AI Model** | Llama-3.3-70B via Groq API |
| **Data Handling** | CSV (doctors_data.csv) |
| **Web Scraping** | Python (BeautifulSoup, Requests) |
| **Hosting (Local)** | Flask Local Server (http://127.0.0.1:5000) |

---



