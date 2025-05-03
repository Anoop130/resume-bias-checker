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

def extractText(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


if __name__ == "__main__":
    resume_text = extractText("")
    print(resume_text)