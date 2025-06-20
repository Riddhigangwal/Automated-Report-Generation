import os
import csv
import statistics
from fpdf import FPDF

# Step 1: Create sample CSV if not exists
def create_sample_csv():
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Value"])
        sample_data = [23, 45, 12, 67, 34, 89, 27, 56, 78, 90]
        for num in sample_data:
            writer.writerow([num])

if not os.path.exists("data.csv"):
    create_sample_csv()

# Step 2: Read and analyze data
values = []
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            values.append(float(row["Value"]))
        except ValueError:
            continue

count = len(values)
total = sum(values)
average = total / count if count else 0
maximum = max(values) if values else 0
minimum = min(values) if values else 0
stdev = statistics.stdev(values) if count > 1 else 0

# Step 3: Generate PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Data Analysis Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Total Values: {count}", ln=True)
pdf.cell(200, 10, f"Sum: {total}", ln=True)
pdf.cell(200, 10, f"Average: {average:.2f}", ln=True)
pdf.cell(200, 10, f"Maximum: {maximum}", ln=True)
pdf.cell(200, 10, f"Minimum: {minimum}", ln=True)
pdf.cell(200, 10, f"Standard Deviation: {stdev:.2f}", ln=True)
pdf.ln(10)

pdf.set_font("Arial", "B", 12)
pdf.cell(200, 10, "Data Values:", ln=True)
pdf.set_font("Arial", size=12)
for i, val in enumerate(values, 1):
    pdf.cell(30, 10, f"{i}. {val}", ln=True)

pdf.output("report.pdf")
print("✅ Report generated successfully: report.pdf")
