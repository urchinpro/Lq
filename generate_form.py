from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.platypus import Frame, Image
from reportlab.lib.pagesizes import A4


class myForm():
    '''Work with Canvas
    '''
    def __init__(self, c, fonts):
        self.c = c
        self.fonts = fonts

    def draw_pdf(self):
        pos_y = 5
        ed_izm='* mm'
        for font in fonts:
            self.c.setFont(font, 12)
            self.c.drawString(5 * mm, pos_y * mm, font)
            pos_y +=10

        self.c.showPage()
        self.c.save()
c = canvas.Canvas("hello1.pdf", bottomup = 0)

fonts = c.getAvailableFonts()
a=myForm(c, fonts)
a.draw_pdf()