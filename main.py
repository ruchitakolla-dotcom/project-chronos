#!/usr/bin/env python3
"""
Project Chronos: The AI Archeologist
A command-line tool to reconstruct obscure digital text fragments using AI and web context.
"""

import os
import sys
import time
from dotenv import load_dotenv
from colorama import Fore, Style,init
from reconstruction import reconstruct_text, search_context, generate_report
init(autoreset=True)

def spinner(message, duration=2):
    """Show a simple spinner animation for better UX."""
    spinner_chars = "|/-\\"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in spinner_chars:
            sys.stdout.write(f"\r{Fore.YELLOW}{message} {char}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r" + " " * len(message), end="\r")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python main.py \"your fragmented text here\" OR python main.py fragments.txt" + Style.RESET_ALL)
        sys.exit(1)

    input_arg = sys.argv[1].strip()
    if not input_arg:
        print(Fore.RED + "Error: Please provide a non-empty text fragment or file path." + Style.RESET_ALL)
        sys.exit(1)

    # Allow input from .txt file with multiple fragments
    if os.path.isfile(input_arg) and input_arg.endswith(".txt"):
        with open(input_arg, "r", encoding="utf-8") as f:
            fragments = [line.strip() for line in f if line.strip()]
    else:
        fragments = [input_arg]

    print(Fore.MAGENTA + "╔════════════════════════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║              PROJECT CHRONOS: AI ARCHEOLOGIST              ║")
    print(Fore.MAGENTA + "╚════════════════════════════════════════════════════════════╝" + Style.RESET_ALL)

    for idx, fragment in enumerate(fragments, 1):
        print(Fore.CYAN + f"\n[{idx}/{len(fragments)}] Processing fragment: {fragment}" + Style.RESET_ALL)
        spinner("🔍 Scanning digital archives...")

        reconstructed = reconstruct_text(fragment)
        if not reconstructed:
            print(Fore.RED + "❌ Error: Failed to reconstruct text." + Style.RESET_ALL)
            continue

        spinner("🌐 Searching for historical context...")
        sources = search_context(reconstructed)
        if not sources:
            print(Fore.YELLOW + "⚠️  Warning: No sources found." + Style.RESET_ALL)

        report = generate_report(fragment, reconstructed, sources)
        print(Fore.GREEN + report + Style.RESET_ALL)

        filename = f"reconstruction_report_{idx}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(Fore.BLUE + f"\n📄 Report saved to '{filename}'" + Style.RESET_ALL)

    print(Fore.MAGENTA + "\n✨ All fragments processed successfully. Goodbye, time traveler!" + Style.RESET_ALL)

if __name__ == "__main__":
    load_dotenv()  # Load .env file for API keys
    main()