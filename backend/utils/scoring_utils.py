def calculate_risk_score(signals):

    score = 0
    reasons = []

    if signals["no_https"]:
        score += 20
        reasons.append("Website does not use HTTPS")

    if signals["suspicious_keywords"]:
        score += 20
        reasons.append("Suspicious keywords found in URL")

    if signals["young_domain"]:
        score += 30
        reasons.append("Domain registered recently")

    if signals["typosquatting"]:
        score += 30
        reasons.append("Domain similar to known brand")

    return score, reasons