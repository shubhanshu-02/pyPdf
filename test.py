from reportlab.pdfgen import canvas

c = canvas.Canvas("Initialtest.pdf")
c.drawString(100,750,"test invoice")
c.save()


print("pdf saved")