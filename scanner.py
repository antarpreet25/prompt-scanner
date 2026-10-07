import requests
import time
from dotenv import load_dotenv
import os
from scanner.layers.keyword import is_suspicious
from scanner.logger import log_result


load_dotenv()  # Load environment variables from .env file


class PromptScanner:
  def __init__(self):
    pass
   
  def scan(self, prompt):
      url = "https://api.groq.com/openai/v1/chat/completions"

      headers = {
          "Authorization" : f"Bearer {os.getenv('GROQ_API_KEY')}",
          "Content-Type" : "application/json"
      }

      data = {
              "model": "openai/gpt-oss-20b",   # free, fast, good model
              "max_tokens": 100,
              "messages": [
                            {"role": "system", "content" : "You are a concise assistant. Never exceed 25 words in your response. Do not use conversational filler."},
                            {"role": "user", "content": prompt}
                          ],
              }

      try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]


      except requests.exceptions.ConnectionError:
        print("Connection failed, attempt")
        time.sleep(5)
      except requests.exceptions.Timeout:
        print("Timed out, attempt")
        time.sleep(5)
      except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        print(f"Response body: {response.text}")  # ← shows exact error message from Groq
      return None


  def scan_safe(self, prompt):

      if is_suspicious(prompt):
        result = {"blocked": True, "reason": "suspicious pattern detected", "response": None}
      else:
        result = {"blocked": False, "reason": None, "response": self.scan(prompt)}

      log_result(prompt, result)
      return result