# import sys
#
# import PyPDF2

# with open('dummy.pdf', 'rb') as pdf_file:
#     # print(pdf_file)
#     reader = PyPDF2.PdfReader(pdf_file)
#     print(len(reader.pages))
#     print(reader.pages[0])
#
#     page_reader = reader.pages[0]
#     page_reader.rotate(90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page_reader)
#     with open('new.pdf', 'wb') as file:
#         writer.write(file)

# inputs = sys.argv[1:]
#
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super-pdf1.pdf')
#
#
# pdf_combiner(inputs)

# --------------------------------------------exercise---------------------------------------------

import PyPDF2


template = PyPDF2.PdfReader(open("super-pdf1.pdf", "rb"))
water_mark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
out_put = PyPDF2.PdfWriter()
print(template)
print(out_put)

for page in template.pages:
    print(page)
    page.merge_page(water_mark.pages[0])
    out_put.add_page(page)

with open('new1.pdf', "wb") as file:
    out_put.write(file)
