QUALITY_LIMITS = {
    "min_quality_score": 70,
    "max_complexity": 10,
    "min_maintainability": 60
}


def evaluate_quality(metrics):

    failures = []

    if metrics["QualityScore"] \
            < QUALITY_LIMITS["min_quality_score"]:
        failures.append(
            "Quality score below threshold"
        )

    if metrics["AvgComplexity"] \
            > QUALITY_LIMITS["max_complexity"]:
        failures.append(
            "Complexity too high"
        )

    if metrics["MaintainabilityIndex"] \
            < QUALITY_LIMITS["min_maintainability"]:
        failures.append(
            "Low maintainability"
        )

    return failures