from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_full_invoice(data, output_path="output_invoice.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Draw Logo
    if data.get("logo_path"):
        c.drawImage(data["logo_path"], 30, height - 90, width=60, preserveAspectRatio=True, mask='auto')

    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, height - 50, "ELIXIR UNIVERSAL SOLUTIONS")
    c.setFont("Helvetica", 9)
    c.drawString(100, height - 65, "1848/90, 1st Floor, Shanti Nagar, Tri Nagar, New Delhi-110035")
    c.drawString(100, height - 78, "CONTACT NO-011-27380576 | GSTIN NO- 07AAEFE4283D2ZM")
    c.drawString(100, height - 91, "SAC CODE 998313 | MSME No : DL04D0012390")

    # Invoice Info Box
    c.setFont("Helvetica-Bold", 10)
    c.drawString(400, height - 50, f"Invoice No.: {data['invoice_no']}")
    c.drawString(400, height - 65, f"Dated: {data['date']}")
    c.drawString(400, height - 80, f"POS: {data['pos']}")

    # To Section
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height - 120, "To:")
    c.setFont("Helvetica", 9)
    for i, line in enumerate(data["to"]):
        c.drawString(50, height - 135 - i * 12, line)

    # GSTIN
    c.drawString(30, height - 190, f"GSTIN OF PARTY: {data['gstin']}")

    # Items Table
    table_data = [["Particulars", "Nos.", "Rate/unit", "Amount Rs."]] + data["items"]
    t = Table(table_data, colWidths=[230, 60, 80, 100])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold')
    ]))
    t.wrapOn(c, width, height)
    t.drawOn(c, 30, height - 360)

    # Totals
    y = height - 370 - (len(data["items"]) * 20)
    for label, amount in data["totals"]:
        c.drawRightString(450, y, label)
        c.drawRightString(550, y, f"{amount:.2f}")
        y -= 15

    # Footer Notes
    c.setFont("Helvetica", 8)
    c.drawString(30, y - 10, "Invoice to be paid within 7 days of receipt.")
    c.drawString(30, y - 25, "Payment only by Local Delhi Cheque/Demand Draft favouring “Elixir Universal Solutions”")
    c.drawString(30, y - 40, "Any discrepancy must be brought to our attention within 3 working days of receipt.")

    # Bank Info
    bank_info = [
        "BANK ACCOUNT DETAILS",
        "ELIXIR UNIVERSAL SOLUTIONS",
        "KOTAK MAHINDRA BANK",
        "CONNAUGHT PLACE BRANCH",
        "A/C No.- 503011045984",
        "RTGS/NEFT CODE- KKBK0004605"
    ]
    for i, line in enumerate(bank_info):
        c.drawString(30, y - 70 - i * 12, line)

    # Signature
    c.drawString(400, y - 140, "AUTHORISED SIGNATURE")

    c.save()


sample_data = {
    "logo_path": "logo.png",
    "invoice_no": "EZ/21-22/00000",
    "date": "01-07-2021",
    "pos": "Delhi",
    "to": ["ABC Company", "123 Street", "New Delhi - 110001"],
    "gstin": "07ABCDE1234FZ1",
    "items": [
        ["Towards DATA Transmission Charges - JULY, 2021", "1", "1000", "1000.00"],
        ["MBL NO : as per attached details (FCL)", "", "", ""],
        ["HBL NO : as per attached details (LCL)", "", "", ""],
        ["Job Release charges", "1", "500", "500.00"],
    ],
    "totals": [
        ("Total Charges", 1500.00),
        ("CGST @9%", 135.00),
        ("SGST @9%", 135.00),
        ("IGST @18%", 0.00),
        ("Round Off", 0.00),
        ("Total Amount Due", 1770.00),
    ]
}

generate_full_invoice(sample_data)