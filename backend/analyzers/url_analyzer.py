from utils.domain_utils import extract_domain
from services.whois_service import get_domain_age
from utils.scoring_utils import calculate_risk_score


suspicious_words = [
    "login",
    "verify",
    "bank",
    "secure",
    "account",
    "update"
]


def analyze_url(url):

    signals = {
        "no_https": False,
        "suspicious_keywords": False,
        "young_domain": False,
        "typosquatting": False
    }

    # HTTPS check
    if not url.startswith("https"):
        signals["no_https"] = True

    # keyword detection
    for word in suspicious_words:
        if word in url.lower():
            signals["suspicious_keywords"] = True

    # domain extraction
    domain = extract_domain(url)

    # domain age
    age = get_domain_age(domain)

    if age is not None and age < 30:
        signals["young_domain"] = True

    score, reasons = calculate_risk_score(signals)

    return {
        "url": url,
        "risk_score": score,
        "reasons": reasons
    }