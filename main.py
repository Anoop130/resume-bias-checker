#!/usr/bin/env python3
import os
import json
import subprocess
import pandas as pandas
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
def saveExtraction(fileName: str, text: str) -> bool:
    output_dir = "output_texts"
    if not os.path.isdir(output_dir):
        print(f"Directory not found: {output_dir}")
        return False
    
    fullpath = os.path.join(output_dir, fileName)

    with open(fullpath, 'w') as file:
        file.write(text)

    print(f"\n--- Saved the contents of {fileName} ---")
    return True

def extractText(pdf_path: str) -> str:
    try:
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
    except (PdfReadError, FileNotFoundError) as e:
        print(f"Could not read {pdf_path}: {e}")
        return ""


if __name__ == "__main__":
    resumes_dir = "resumes"

    if not os.path.isdir(resumes_dir):
        print(f"Directory not found: {resumes_dir}")
        exit(1)

    for fileName in os.listdir(resumes_dir):

        if not fileName.lower().endswith(".pdf"):
            continue

        fullpath = os.path.join(resumes_dir, fileName)

        print(f"\n--- Extracting from {fileName} ---")
        text = extractText(fullpath)
        saveExtraction(fileName, text)

    