import datetime
import json

def log_result(prompt, result):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "prompt": prompt,
        "blocked": result["blocked"],
        "reason": result["reason"],
        "response": result["response"]
    }
    print(entry)
    with open("scan_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")

def report():
    total_scanned = 0 
    total_blocked = 0 
    total_passed = 0 
    blocked_list = [] 
    with open("scan_log.jsonl", "r") as f: 
        for line in f: 
            # Skip empty lines to prevent JSON parse errors 
            if not line.strip(): 
                continue 
            # 1. Convert the string line into a Python dictionary 
            entry = json.loads(line) 
            # 2. Update your counts
            total_scanned += 1 
            if entry.get("blocked"):
                total_blocked += 1 
                blocked_list.append(entry.get("prompt", ""))
            else:
                total_passed += 1 
    return { "total_scanned": total_scanned, "total_blocked": total_blocked, "total_passed": total_passed, "blocked_list": blocked_list }
