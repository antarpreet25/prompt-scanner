def is_suspicious(prompt):
    sus_keywords = ["ignore previous", "reveal system", "bypass", "jailbreak", "forget instructions"]
    prompt_lower = prompt.lower()
    return any(keyword in prompt_lower for keyword in sus_keywords)
