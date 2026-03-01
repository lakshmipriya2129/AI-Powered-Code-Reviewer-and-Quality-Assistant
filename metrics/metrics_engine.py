import ast
import os

from metrics.maintainability import maintainability_index
from metrics.scoring import calculate_quality_score
from metrics.coverage import estimate_coverage
from metrics.exporter import export_csv, export_html


class MetricsEngine:

    def analyze_file(self,
                     filepath,
                     analysis_result):

        with open(filepath,
                  encoding="utf-8") as f:
            code = f.read()

        tree = ast.parse(code)

        loc = len(code.splitlines())

        total_complexity = sum(
            f.complexity
            for f in analysis_result.functions
        ) or 1

        avg_complexity = (
            total_complexity /
            max(len(
                analysis_result.functions), 1)
        )

        # Approx Halstead volume
        volume = loc * avg_complexity

        comments = sum(
            1 for line in code.splitlines()
            if line.strip().startswith("#")
        )

        mi = maintainability_index(
            volume,
            total_complexity,
            loc,
            comments
        )

        smells_count = sum(
            len(v)
            for v in analysis_result.smells.values()
        )

        quality_score = calculate_quality_score(
            mi,
            avg_complexity,
            smells_count
        )

        coverage_hint = estimate_coverage(tree)

        return {
            "file": filepath,
            "LOC": loc,
            "MaintainabilityIndex": mi,
            "AvgComplexity": round(
                avg_complexity, 2),
            "QualityScore": quality_score,
            "CoverageHint": coverage_hint
        }

    # ---------------------------------
    # PROJECT LEVEL METRICS
    # ---------------------------------
    def analyze_project(self,
                        files,
                        analyses):

        results = []

        for file, analysis in zip(
                files, analyses):

            results.append(
                self.analyze_file(
                    file,
                    analysis
                )
            )

        return results

    # ---------------------------------
    # EXPORT REPORTS
    # ---------------------------------
    def export_reports(self,
                       results):

        csv_file = export_csv(results)
        html_file = export_html(results)

        return csv_file, html_file