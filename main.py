#!/usr/bin/env python3
"""
Project Chronos: The AI Archeologist
A command-line tool to reconstruct obscure digital text fragments using AI and web context.
"""

import os
import sys
from dotenv import load_dotenv
from reconstruction import reconstruct_text, search_context, generate_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py \"your fragmented text here\"")
        sys.exit(1)
    
    fragment = sys.argv[1].strip()
    if not fragment:
        print("Error: Please provide a non-empty text fragment.")
        sys.exit(1)
    
    print(f"Processing fragment: {fragment}")
    
    # Step 1: Reconstruct using Gemini
    reconstructed = reconstruct_text(fragment)
    if not reconstructed:
        print("Error: Failed to reconstruct text.")
        sys.exit(1)
    
    # Step 2: Search for context
    sources = search_context(reconstructed)
    if not sources:
        print("Warning: No sources found.")
    
    # Step 3: Generate report
    report = generate_report(fragment, reconstructed, sources)
    print(report)
    
    # Optionally save to file
    with open("reconstruction_report.txt", "w") as f:
        f.write(report)
    print("\nReport saved to 'reconstruction_report.txt'")

if __name__ == "__main__":
    load_dotenv()  # Load .env file for API keys
    main()