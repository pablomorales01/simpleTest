
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def textfile_to_pdf(input_txt, output_pdf, title="Pipeline Log"):
    c = canvas.Canvas(output_pdf, pagesize=landscape(A4))
    width, height = landscape(A4)
    left_margin = 15 * mm
    top_margin = height - 15 * mm
    line_height = 5.5 * mm

    c.setFont("Helvetica-Bold", 14)
    c.drawString(left_margin, top_margin, title)
    y = top_margin - (1.5 * line_height)
    c.setFont("Courier", 9)

    with open(input_txt, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            # wrap long lines
            while line:
                chunk = line[:160]
                line = line[160:]
                if y < 15 * mm:
                    c.showPage()
                    c.setFont("Courier", 9)
                    y = top_margin
                c.drawString(left_margin, y, chunk.rstrip())
                y -= line_height

    c.save()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tools/make_pdf.py <input_log.txt> <output.pdf>")
        sys.exit(1)
    textfile_to_pdf(sys.argv[1], sys.argv[2])
