import os
import tempfile
import zipfile
from pathlib import Path

from parser.analyzer import analyze_file
from ai_review.reviewer import AIReviewer
from metrics.metrics_engine import MetricsEngine


def extract_project(uploaded_file):

    temp_dir = tempfile.mkdtemp()

    zip_path = os.path.join(temp_dir, "project.zip")

    with open(zip_path, "wb") as f:
        f.write(uploaded_file.read())

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(temp_dir)

    return temp_dir


def get_python_files(project_path):
    return list(Path(project_path).rglob("*.py"))


def run_full_analysis(project_path):

    reviewer = AIReviewer()
    metrics_engine = MetricsEngine()

    files = get_python_files(project_path)

    analyses = []
    reviews = []

    for file in files:
        analysis = analyze_file(str(file))
        analyses.append(analysis)

        review = reviewer.generate_review(
            str(file),
            analysis.smells
        )

        reviews.append(review)

    metrics = metrics_engine.analyze_project(
        files,
        analyses
    )

    return files, analyses, reviews, metrics