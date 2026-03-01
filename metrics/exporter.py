import csv
from pathlib import Path


# -----------------------------
# CSV EXPORT
# -----------------------------
def export_csv(results, output="report.csv"):

    keys = results[0].keys()

    with open(output,
              "w",
              newline="",
              encoding="utf-8") as f:

        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(results)

    return output


# -----------------------------
# HTML EXPORT
# -----------------------------
def export_html(results,
                output="report.html"):

    html = """
    <html>
    <head>
    <title>Code Quality Report</title>
    <style>
        table {border-collapse: collapse;}
        th, td {
            border:1px solid black;
            padding:8px;
        }
        th {background:#222;color:white;}
    </style>
    </head>
    <body>
    <h2>Code Quality Metrics</h2>
    <table>
    <tr>
    """

    for key in results[0].keys():
        html += f"<th>{key}</th>"

    html += "</tr>"

    for row in results:
        html += "<tr>"
        for val in row.values():
            html += f"<td>{val}</td>"
        html += "</tr>"

    html += "</table></body></html>"

    Path(output).write_text(html,
                            encoding="utf-8")

    return output