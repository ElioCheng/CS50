from fpdf import FPDF

class ShirtificatePDF(FPDF):
    def header(self):
        self.set_font("Arial", size=24)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def add_shirt(self, name):
        self.image("shirtificate.png", x=0, y=30, w=210)
        self.set_font("Arial", size=32)
        self.set_text_color(255, 255, 255)
        self.ln(60)
        self.cell(0, 10, name, 0, 1, "C")

def main():
    name = input("What's your name? ").strip()
    pdf = ShirtificatePDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.add_shirt(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
