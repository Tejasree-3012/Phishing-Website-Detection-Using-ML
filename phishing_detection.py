import re

def predict_phishing(url):
    """Analyzes a URL for phishing indicators."""
    url_lower = url.lower()
    reasons = []
    
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url_lower):
        reasons.append("Uses an IP address instead of a domain name")
        
    if "@" in url_lower:
        reasons.append("Contains an '@' symbol to hide the real destination")
        
    if len(url) > 75:
        reasons.append("URL is unusually long")
        
    if url_lower.count('.') > 3:
        reasons.append("Contains an unusually high number of subdomains")
        
    keywords = ['login', 'verify', 'update', 'secure', 'banking', 'account']
    found_keywords = [kw for kw in keywords if kw in url_lower]
    if found_keywords:
        reasons.append(f"Contains suspicious keywords ({', '.join(found_keywords)})")

    if re.search(ip_pattern, url_lower) or len(reasons) >= 2:
        return f"Phishing Detected! Reasons: {', '.join(reasons)}."
    elif len(reasons) == 1:
        return f"Suspicious. Reason: {reasons[0]}."
    else:
        return "Safe. No suspicious patterns found."

def analyze_file_content(file_content):
    """Analyzes text inside a file for malicious code."""
    content_lower = file_content.lower()
    reasons = []

    if "<form" in content_lower and "action=" in content_lower:
        reasons.append("Contains an embedded data submission form")

    if "<script" in content_lower:
        reasons.append("Contains hidden code/scripts")

    if "password" in content_lower and ("verify" in content_lower or "update" in content_lower):
        reasons.append("Asks for password verification/updates")
        
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, content_lower):
        reasons.append("Contains raw IP addresses hidden in the text")

    if len(reasons) >= 2:
        return f"Malicious File Detected! Reasons: {', '.join(reasons)}."
    elif len(reasons) == 1:
        return f"Suspicious File. Reason: {reasons[0]}."
    else:
        return "Safe File. No obvious malicious patterns found inside."