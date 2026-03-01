def calculate_quality_score(mi,avg_complexity,smells_count):

    score = mi

    # Penalize complexity
    if avg_complexity > 10:
        score -= 15
    elif avg_complexity > 5:
        score -= 7

    # Penalize smells
    score -= smells_count * 2

    return max(0, round(score, 2))