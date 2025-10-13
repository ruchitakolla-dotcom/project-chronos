"""
Reconstruction module for Project Chronos.
Handles AI-based text reconstruction, context search, and report generation.
Requires: google-generativeai, duckduckgo-search, python-dotenv
"""

import google.generativeai as genai
from duckduckgo_search import DDGS
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini AI (get API key from Google AI Studio)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file. Get one from https://aistudio.google.com/app/apikey")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize DuckDuckGo search
search_engine = DDGS()

def reconstruct_text(fragment: str) -> str:
    """
    Use Gemini AI to reconstruct the fragmented text.
    Example: Input "th3 qu1ck br0wn f0x" -> Output "The quick brown fox"
    """
    prompt = f"""
    You are an expert in reconstructing corrupted or fragmented digital text from old internet archives.
    The fragment is: "{fragment}"
    
    Reconstruct it to form coherent, original English text. Consider:
    - Typos, leetspeak (e.g., 3=E, 1=I, 0=O), missing letters, or garbled encoding.
    - Context from early web (1990s-2000s forums, emails, ASCII art).
    - Keep it concise (1-2 sentences max).
    - If ambiguous, choose the most likely historical/internet-related meaning.
    
    Output ONLY the reconstructed text, nothing else.
    """
    
    try:
        response = model.generate_content(prompt)
        reconstructed = response.text.strip()
        if not reconstructed:
            return "Reconstruction failed: No response from AI."
        return reconstructed
    except Exception as e:
        return f"Error in reconstruction: {str(e)}"

def search_context(reconstructed: str) -> list:
    """
    Search the web for context/sources related to the reconstructed text.
    Uses DuckDuckGo for quick, relevant results.
    """
    try:
        results = search_engine.text(reconstructed, max_results=5)
        sources = []
        for result in results:
            sources.append({
                "title": result.get("title", "No title"),
                "url": result.get("href", "No URL"),
                "snippet": result.get("body", "No snippet")
            })
        return sources
    except Exception as e:
        print(f"Search error: {str(e)}")
        return []

def generate_report(original_fragment: str, reconstructed: str, sources: list) -> str:
    """
    Generate a formatted report summarizing the archeology.
    """
    report = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
│                          PROJECT CHRONOS REPORT                               │
║                                                                              ║
│ Original Fragment: {original_fragment}                                          │
│ Reconstructed Text: {reconstructed}                                             │
│                                                                              │
│ Analysis: This fragment appears to be from an old digital source. The AI     │
│ reconstructed it by correcting common internet-era corruptions (e.g.,        │
│ leetspeak, encoding errors). Confidence: High (based on Gemini model).       │
│                                                                              │
"""

    if sources:
        report += "│ Context Sources Found (Top 5 from Web Search):                     │\n"
        for i, source in enumerate(sources, 1):
            report += f"│ {i}. {source['title'][:50]}... ({source['url'][:60]}...) │\n"
    else:
        report += "│ No relevant sources found—may be truly obscure!                          │\n"

    report += """
║                                                                              ║
│ Next Steps: Review sources for historical context. Run again with more       │
│ fragments for deeper analysis.                                               │
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    return report.strip()