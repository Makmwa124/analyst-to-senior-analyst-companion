# From Analyst to Senior Analyst: companion files

Free templates, worksheets and practice files for the book **From Analyst to Senior Analyst: Stakeholders, Scoping, Saying No and the Other Skills That Get Analysts Promoted** by Mathew Kariuki.

The book follows Priya, an analyst at Paperbark Mutual, a fictional health insurer, through the year in which she earns her promotion. This repository holds the templates and worksheets from the book (scoping brief, stakeholder map, saying-no scripts, promotion evidence log, 1:1 agenda, 90-day plan and request log), the practice data behind the examples, and every code example, so you can use them at work or follow along.

## Download

Click the green **Code** button above, then **Download ZIP**. Unzip it somewhere sensible, such as your Documents folder.

## What's here

| Path | What it is |
| --- | --- |
| `templates/scoping_brief_template.docx` / `.md` | One-page scoping brief with prompts and a worked example (Chapter 3) |
| `templates/stakeholder_map_template.xlsx` / `.md` | Stakeholder map: scores influence and interest, works out the approach and fills in the grid (Chapter 5) |
| `templates/saying_no_scripts.docx` / `.md` | Scripts for not yet, yes if, yes but smaller and no-but-instead, plus the bad-news checklist (Chapters 6 and 8) |
| `templates/promotion_evidence_log.xlsx` / `.md` | Evidence log with a summary sheet by skill area (Chapter 13) |
| `templates/one_on_one_agenda.docx` / `.md` | 1:1 agenda for decisions, feedback and development (Chapter 13) |
| `templates/ninety_day_plan.docx` / `.md` | The 90-day plan from Appendix B as a checklist |
| `templates/request_log_template.xlsx` | Request log with the Paperbark data, a summary built from formulas, and a blank log for your own requests (Appendix D) |
| `data/requests.csv` | 184 requests to the Paperbark analytics team, July 2025 to June 2026 |
| `data/stakeholders.csv` | Ten stakeholders with influence, interest and stance |
| `data/evidence_log.csv` | Priya's eleven evidence log entries |
| `data/paperbark.db` | SQLite copy of all three tables (Chapter 9) |
| `book_code/` | Every code example, chapter by chapter |
| `scripts/make_data.py` | The script that generated the practice data |

## Quick start

The templates need nothing but Word and Excel (or any program that opens .docx and .xlsx files). Make a copy, then fill it in.

To run the code examples:

1. Install Python, then run:

   ```
   pip install pandas numpy
   ```

2. In VS Code, choose **File > Open Folder** and open this folder.
3. Run any example from this folder, for example:

   ```
   python book_code/ch04_estimates.py
   ```

Paths such as `data/requests.csv` assume this folder is your working directory.

Tested with Python 3.13 and pandas 3.0.

## Get the book

- **Paperback:** [Amazon.com](https://www.amazon.com/dp/B0HPZ4R23P) · [Amazon.com.au](https://www.amazon.com.au/dp/B0HPZ4R23P)
- **Kindle:** [Amazon.com](https://www.amazon.com/dp/B0HPZ52MN7) · [Amazon.com.au](https://www.amazon.com.au/dp/B0HPZ52MN7)

## About

Paperbark Mutual and every person and business in its data are fictional. The templates, data and code are free to use for learning and at work. The book itself is © 2026 Mathew Kariuki.

Spotted a problem with a template or an example? Please open an issue.
