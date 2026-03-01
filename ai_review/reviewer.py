import json
from ai_review.prompts import SYSTEM_PROMPT, build_prompt
from ai_review.schemas import AIReviewResult, ReviewIssue
from ai_review.severity import rank_issue
from ai_review.autofix import apply_autofix

# Example using OpenAI compatible client
from openai import OpenAI

client = OpenAI()


class AIReviewer:

    def generate_review(self, filepath, smells):

        with open(filepath, "r",
                  encoding="utf-8") as f:
            code = f.read()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": build_prompt(
                        code, smells
                    )
                }
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content

        data = json.loads(content)

        issues = []

        for item in data["issues"]:
            issue = ReviewIssue(
                title=item["title"],
                description=item["description"],
                severity=item["severity"],
                line=item["line"],
                suggestion=item["suggestion"]
            )

            issue.severity = rank_issue(issue)
            issues.append(issue)

        return AIReviewResult(
            file=filepath,
            summary=data["summary"],
            issues=issues
        )

    # ----------------------------
    # Optional Auto Fix
    # ----------------------------
    def auto_fix(self, filepath):

        with open(filepath, "r") as f:
            code = f.read()

        fixed = apply_autofix(code)

        with open(filepath, "w") as f:
            f.write(fixed)

        return fixed