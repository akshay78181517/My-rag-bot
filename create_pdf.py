from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors

doc = SimpleDocTemplate("textbook.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("Itemwise Sales Report", styles['Title']))
story.append(Spacer(1, 0.2 * inch))

# Table data
data = [
    ['Item Name', 'Qty', 'Value', 'Category', 'Brand', 'Unit Price'],
    ['KPN MILK BREAD 400GM', '335', '15972', 'Bread & Buns', 'KPN', '47.67'],
    ['SEASONS SWEET BUN 400GM', '291', '2910', 'Bread & Buns', 'Seasons', '10.0'],
    ['SEASONS WHEAT BREAD 350GM', '304', '15200', 'Bread & Buns', 'Seasons', '50.0'],
    ['KPN MINI MILK BREAD 180GM', '265', '7950', 'Bread & Buns', 'KOVAI CRISPS', '30.0'],
    ['KPN MINI WHEAT BREAD 180GM', '242', '7260', 'Bread & Buns', 'KOVAI CRISPS', '30.0'],
    ['KPN BANANA CUP CAKE', '22', '440', 'Bread & Buns', 'KPN', '20.0'],
    ['SEASONS MINI BUN 200G', '111', '3885', 'Bread & Buns', 'Seasons', '35.0'],
    ['TEA CAKE', '103', '5150', 'Cakes & Cookies', 'KPN', '50.0'],
    ['PUDDING CAKE', '43', '1720', 'Cakes & Cookies', 'KPN', '40.0'],
    ['KOVAI CRISPS CHIKKI SCHOOL PACK', '111', '13320', 'Confectionery', 'KOVAI CRISPS', '120.0'],
    ['KOVAI CRISPS PEANUT CHIKKI', '1615', '8075', 'Confectionery', 'KOVAI CRISPS', '5.0'],
    ['KOVAI CRISPS KAMARCUT CHIKKI', '119', '5950', 'Confectionery', 'KOVAI CRISPS', '50.0'],
    ['KOVAI CRISPS COCONUT BURFI', '44', '3080', 'Confectionery', 'KOVAI CRISPS', '70.0'],
    ['KPN OMAPODI 100GM', '88', '2800', 'Regional Snacks', 'KPN', '31.81'],
    ['KPN KAARAM MURUKKU 200G', '220', '14600', 'Regional Snacks', 'KPN', '66.36'],
    ['KPN RIBBON PAKODA 200G', '220', '15110', 'Regional Snacks', 'KPN', '68.68'],
    ['KPN CHOLAM MURUKKU 200G', '65', '4815', 'Regional Snacks', 'KPN', '74.07'],
    ['KPN MIXTURE 200G', '404', '29065', 'Regional Snacks', 'KPN', '71.94'],
    ['KPN WHITE MURUKKU 200G', '292', '19490', 'Regional Snacks', 'KPN', '66.74'],
    ['KOVAI CRISPS ATHIRASAM 6PCS', '156', '9360', 'Regional Snacks', 'KOVAI CRISPS', '60.0'],
    ['KPN MASALA PUFFED RICE 160G', '346', '19563', 'Regional Snacks', 'KPN', '56.54'],
    ['KPN KAARA SEV 100G', '28', '1400', 'Regional Snacks', 'KPN', '50.0'],
    ['KPN KAARA BOONDHI 200G', '151', '10995', 'Regional Snacks', 'KPN', '72.81'],
]

table = Table(data, colWidths=[2.2*inch, 0.5*inch, 0.7*inch, 1.2*inch, 1.0*inch, 0.7*inch])
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTSIZE', (0,0), (-1,0), 9),
    ('FONTSIZE', (0,1), (-1,-1), 8),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.lightgrey]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN', (1,0), (-1,-1), 'CENTER'),
]))

story.append(table)
doc.build(story)
print("textbook.pdf created successfully with sales data!")