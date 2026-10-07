import re


def is_suspicious_regex(prompt):
    # Using a list of patterns to check for various suspicious phrases.
    # Using raw strings (r'...') for regex to prevent issues with backslashes.
    # Using `\s+` for one or more whitespace characters.
    # Using `.*?` for non-greedy matching of any character.
    # Using `?` for optional characters/groups.
    patterns = [
        r"ignore\s+previous?.*?instructions?",
        r"ignore\s+\w*?(prompt|key|secret)", # To catch "ignore prompt", "ignore key", "ignore secret"
        r"bypass",
        r"jailbreak",
        r"DAN", # Stands for "Do Anything Now" a common jailbreak
        r"you\s+are\s+now",
        r"act\s+as",
        r"pretend\s+to\s+be"
    ]
    
    prompt_lower = prompt.lower()
    for pattern in patterns:
      if re.search(pattern, prompt_lower, re.IGNORECASE):
        return True
    return False