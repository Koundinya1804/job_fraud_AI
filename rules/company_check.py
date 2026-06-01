def analyze_company(text):

    text = text.lower()

    warnings = []

    trusted_companies = [
        "microsoft",
        "google",
        "amazon",
        "meta",
        "apple",
        "ibm",
        "oracle",
        "intel"
    ]

    if any(company in text for company in trusted_companies):
        return []

    free_email_domains = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com"
    ]

    if any(domain in text for domain in free_email_domains):
        warnings.append("Company uses free email domain")

    if "website" not in text and "www" not in text:
        warnings.append("Company website not mentioned")

    return warnings