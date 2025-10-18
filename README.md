                                                                **Project Chronos: The AI Archeologist**
        

**Student Information**


1)Name: Kolla Taruni Venkata Ruchita  
 ID: SE24UARI086
 Branch: AI
 
2)Name: Jetti Laasya  
 ID: SE24UARI104
 Branch: AI 

 
**Project Description:**
Project Chronos is an AI-powered digital archaeologist that reconstructs incomplete, damaged, or obscure text fragments from old web archives. Many web pages, documents, or historical data may be lost or corrupted over time. Project Chronos helps researchers, historians, and archivists preserve digital history.
It uses advanced AI algorithms to analyze incomplete text and predict missing segments, ensuring the reconstructed content is coherent, contextually accurate, and faithful to the original. It examines patterns, context, and linguistic structures to repair inconsistencies in fragmented text.


*Key Functionalities:*
Text Fragment Analysis: Accepts incomplete or corrupted text, detects patterns, repeated structures, and contextual clues.
AI-Based Reconstruction: Predicts missing words, sentences, or paragraphs.
Report Generation: Produces detailed reconstruction reports.
Multi-format Support: Works with plain text, HTML snippets, and archive files.


*Applications:*
Historical document preservation
Recovery of lost academic or technical content
Digital forensics and investigative research
Enhancing web archiving tools


*Features:*
AI-driven reconstruction of text fragments
Supports multiple file types
Generates comprehensive reports
Lightweight and easy to deploy
Step-by-step guidance for fragment analysis


*Project Files:*
-main.py - The program entry point. Accepts text fragments and triggers reconstruction.
-reconstruction.py – Contains the core AI logic for analyzing and reconstructing text fragments.
-requirements.txt – Lists all Python dependencies.
-.env – Stores API keys (keep private).
-reconstruction_report.txt – Output file generated after reconstruction (ignored in Git).
-README.md – This file, with project description, setup instructions, and usage guide.



**Setup Instructions:**
1.Clone the Repository: Open cmd and run: 
git clone https://github.com/ruchitakolla-dotcom/project-chronos
cd project-chronos

This helps you copy all project files to the local machine and navigate into the project folder.

2.Create a Virtual Environment: Open cmd and run: 
python -m venv venv

venv\Scripts\activate

This helps in creating a virtual environment that manage Python dependencies.

3.Install Dependencies: Open cmd and run: 
pip install -r requirements.txt

This helps in installing all the required packages for Project Chronos to run.

4.Set Up API Keys
Create a .env file in the project root folder:
Add your API key:
GEMINI_API_KEY=your_google_gemini_api_key
Save .env and keep it private.
Update .gitignore: this helps in ignoring sensitive and unnecessary files:
.env
__pycache__/
*.pyc
reconstruction_report.txt

#Final running:
git clone https://github.com/ruchitakolla-dotcom/project-chronos

cd project-chronos

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python main.py "Ths is 3sha"


**Usage:**
We need to verify the setup.
Run the program to check if everything works:
python main.py
After everything runs well run it with a input like:
python main.py "Ths is 3sha"


The AI will reconstruct the text and generate a detailed report.

