import argparse
from parser import extract_python_doc
from summarizer import summarize_text
import os

def main():
    parser = argparse.ArgumentParser(description="Local Code Documentation Summarizer")
    parser.add_argument("file", help="Path to the code file")
    parser.add_argument("--output", help="Path to save summary", default="summary.txt")
    args = parser.parse_args()

    code_doc = extract_python_doc(args.file)
    if not code_doc.strip():
        print("No docstrings or comments found.")
        return

    summary = summarize_text(code_doc)

    # Save summary to file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"\n===== Summarized Documentation =====\n")
    print(summary)
    print(f"\n✅ Summary saved to: {os.path.abspath(args.output)}")

if __name__ == "__main__":
    main()
