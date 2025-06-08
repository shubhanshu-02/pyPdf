from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime

def generate_invoice(data, filename="invoice.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    print("generating")

    # Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 40, "ELIXIR UNIVERSAL SOLUTIONS")
    c.setFont("Helvetica", 10)
    c.drawString(30, height - 60, "1848/90, 1st Floor, Shanti Nagar, Tri Nagar,")
    c.drawString(30, height - 75, "New Delhi-110035, CONTACT NO-011-27380576")
    c.drawString(30, height - 90, "GSTIN NO- 07AAEFE4283D2ZM")
    c.drawString(30, height - 105, "SAC CODE 998313 MSME No : DL04D0012390")

    # Invoice Details
    c.setFont("Helvetica-Bold", 10)
    c.drawString(400, height - 40, f"Invoice No.: {data['invoice_no']}")
    c.drawString(400, height - 55, f"Dated: {data['date']}")

    # To section
    c.setFont("Helvetica", 10)
    c.drawString(30, height - 130, f"To: {data['to']}")
    c.drawString(30, height - 145, f"GSTIN OF PARTY: {data['gstin']}")

    # Table Header
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, height - 180, "Particulars")
    c.drawString(200, height - 180, "Nos.")
    c.drawString(250, height - 180, "Rate/unit")
    c.drawString(350, height - 180, "Amount Rs.")

    # Table Data
    y = height - 195
    c.setFont("Helvetica", 10)
    for item in data["items"]:
        c.drawString(30, y, item["desc"])
        c.drawString(200, y, str(item["qty"]))
        c.drawString(250, y, f"{item['rate']:.2f}")
        c.drawString(350, y, f"{item['amount']:.2f}")
        y -= 15

    # Total and Taxes
    y -= 10
    c.setFont("Helvetica-Bold", 10)
    c.drawString(250, y, "Total Charges")
    c.drawString(350, y, f"{data['total']:.2f}")
    y -= 15

    c.drawString(250, y, "CGST @9%")
    c.drawString(350, y, f"{data['cgst']:.2f}")
    y -= 15
    c.drawString(250, y, "SGST @9%")
    c.drawString(350, y, f"{data['sgst']:.2f}")
    y -= 15
    c.drawString(250, y, "IGST @18%")
    c.drawString(350, y, f"{data['igst']:.2f}")
    y -= 15
    c.drawString(250, y, "Round Off")
    c.drawString(350, y, f"{data['roundoff']:.2f}")
    y -= 15
    c.drawString(250, y, "Total Amount Due")
    c.drawString(350, y, f"{data['total_due']:.2f}")

    # Footer
    c.setFont("Helvetica", 9)
    y -= 30
    c.drawString(30, y, "Invoice to be paid within 7 days of receipt.")
    y -= 15
    c.drawString(30, y, "Payment only by Local Delhi Cheque/Demand Draft favouring “Elixir Universal Solutions”")
    y -= 15
    c.drawString(30, y, "Any discrepancy must be brought to our attention within 3 working days of receipt.")
    y -= 30
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, y, "BANK ACCOUNT DETAILS")
    y -= 15
    c.setFont("Helvetica", 10)
    c.drawString(30, y, "ELIXIR UNIVERSAL SOLUTIONS")
    y -= 15
    c.drawString(30, y, "KOTAK MAHINDRA BANK")
    y -= 15
    c.drawString(30, y, "CONNAUGHT PLACE BRANCH")
    y -= 15
    c.drawString(30, y, "A/C No.- 503011045984")
    y -= 15
    c.drawString(30, y, "RTGS/NEFT CODE- KKBK0004605")
    y -= 30

    c.drawString(400, y, "AUTHORISED SIGNATURE")

    c.save()

# Example data
invoice_data = {
    "invoice_no": "EZ/21-22/00001",
    "date": datetime.now().strftime("%d-%m-%Y"),
    "to": "ABC Traders, New Delhi",
    "gstin": "07ABCDE1234FZ1",
    "items": [
        {"desc": "DATA Transmission Charges - JULY, 2021", "qty": 1, "rate": 1000.00, "amount": 1000.00},
        {"desc": "Job Release Charges", "qty": 1, "rate": 500.00, "amount": 500.00}
    ],
    "total": 1500.00,
    "cgst": 135.00,
    "sgst": 135.00,
    "igst": 0.00,
    "roundoff": 0.00,
    "total_due": 1770.00,
}

generate_invoice(invoice_data)