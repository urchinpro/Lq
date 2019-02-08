from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate, NextPageTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from copy import deepcopy
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

import os.path
"""
Ниже блок переменных, заменить из реальных объектов
"""

hospital_name="ОГАУЗ \"Иркутская медикосанитарная часть № 2\""
organization_address = "г. Иркутс, ул. Байкальская 201"
organization_kod_ogrn = "1033801542576"
number_health_passport = "1"# номер id из базы
individual_fio = "Иванов Иван Иванович"
individual_sex = "м"
individual_address="г.Иркутск, ул. Сибирских-Партизан д. 8 кв. 9"
date_born="01.01.1901"
document_passport_number = "010503"
document_passport_serial = "0506"
document_polis_number = "77777777"
individual_work_organization=" ПАО Ростелеком" #реест организаций
work_organization_okved ="91.5 - Обслуживание и ремонт...."
individual_department = "отдел бухгалтерии"
individual_profession = "электромонтажник 1 разряда" #реест профессий
list_result =[]
list_doctor =[]



FONTS_FOLDER ='c:\\tmp\\iq200-pyth\\fonts1\\' #удалить с 1 по 6 строки в проекте
pdfmetrics.registerFont(
        TTFont('OpenSans', os.path.join(FONTS_FOLDER, 'OpenSans.ttf')))  # Загрузка шрифта из файла
pdfmetrics.registerFont(
        TTFont('OpenSansBold', os.path.join(FONTS_FOLDER, 'OpenSans-Bold.ttf')))  # Загрузка шрифта из файла
pdfmetrics.registerFont(
        TTFont('TimesNewRoman', os.path.join(FONTS_FOLDER, 'TimesNewRoman.ttf')))  # Загрузка шрифта из файла
pdfmetrics.registerFont(
        TTFont('PTAstraSerifBold', os.path.join(FONTS_FOLDER, 'PTAstraSerif-Bold.ttf')))  # Загрузка шрифта из файла

#http://www.cnews.ru/news/top/2018-12-10_rossijskim_chinovnikam_zapretili_ispolzovat
#Причина PTAstraSerif использовать


def form_health_passport():
        doc = canvas.Canvas("health_passport2.pdf",pagesize=landscape(A4),
                                leftMargin=10 * mm,
                                rightMargin=10 * mm, topMargin=10 * mm,
                                bottomMargin=10 * mm, allowSplitting=1,
                                title="Форма {}".format("Паспорт здоровья"))

        width, height = landscape(A4)
        styleSheet = getSampleStyleSheet()
        style = styleSheet["Normal"]
        style.fontName = "PTAstraSerifBold"
        style.fontSize = 10.5
        style.leading = 5
        styleBold = deepcopy(style)
        styleBold.fontName = "PTAstraSerifBold"
        styleCenter = deepcopy(style)
        styleCenter.alignment = TA_CENTER
        styleCenterBold = deepcopy(styleBold)
        styleCenterBold.alignment = TA_CENTER
        styleJustified = deepcopy(style)
        styleJustified.alignment = TA_JUSTIFY

        righ_frame = Frame(148.5*mm,	0*mm,	width=148.5 *mm,	height=210*mm,
                           leftPadding=6,	bottomPadding=6,	rightPadding=6, topPadding=6, showBoundary=1)
        left_frame = Frame(0 * mm, 0 * mm, width=148.5 * mm, height=210 * mm,
                           leftPadding=6, bottomPadding=6, rightPadding=6, topPadding=6, showBoundary=1)
        objs = []

        objs.append(NextPageTemplate('righ_frame'))

        objs1 = [
                Paragraph('<font face="PTAstraSerifBold">Министерство здравоохранения Российской Федерации</font>',
                          styleCenterBold),
                Spacer(1, 3 * mm),
                Paragraph('<font face="PTAstraSerifBold">{}</font>'.format(hospital_name),
                          styleCenter),
                Spacer(1, 3 * mm),
                Paragraph('<font face="PTAstraSerifBold">{}</font>'.format(organization_address),
                      styleCenter),
                Spacer(1, 3 * mm),

        ]
        objs.append(objs1)


        doc.build(objs)


form_health_passport()