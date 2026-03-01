def normalize_severity(level: str):

    level = level.lower()

    mapping = {
        "low": "info",
        "medium": "warning",
        "high": "critical"
    }

    return mapping.get(level, level)


def rank_issue(issue):

    text = issue.description.lower()

    if "security" in text:
        return "critical"

    if "performance" in text:
        return "warning"

    return issue.severity