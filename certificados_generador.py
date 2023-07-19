#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import mkdir
from os.path import exists, dirname, join
import jinja2
#from entity_test import get_entity_mm
#import pdfkit
#pdfkit.from_url("http://google.com", "out.pdf")
import pdfkit


def main(debug=False):

    this_folder = dirname(__file__)
    #print('####',this_folder)

    # Create output folder
    srcgen_folder = join(this_folder, 'certificados_generados')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Load template
    template = jinja_env.get_template('certificado.template.html')

    lista_certificados = [x.split(",") for x in open("certificados1.txt",encoding='utf-8-sig').readlines()]
    print(lista_certificados[0])
    lista_certificados = [[x[0].title(),x[1]] for x in lista_certificados]
    print(lista_certificados[0])

    #print(lista_certificados[0:1])

    mode = 'presencial'
    period = 'REALIZADO ENTRE EL 10 DE OCTUBRE Y EL 16 DE NOVIEMBRE DE 2022 CON UNA INTENSIDAD ACADÉMICA DE 20 HORAS'
    title = 'ECONOMÍA SOLIDARIA NIVEL BÁSICO'
    professor = 'Luis Alfonso Bermúdez Martín'
    cont = 1

    '''
    for entity in lista_certificados[0:1]:
        print(entity[0])
    '''

    for entity in lista_certificados:
        # For each entity generate java file
        with open(join(srcgen_folder,
                       "%i %s.html" % (cont, entity[0].capitalize())), 'w') as f:
            f.write(template.render(entity=entity,cont=cont,title=title,professor=professor,mode=mode,period=period))

            # html2pdf
            '''
            filename = str(cont) +' '+ entity[0].capitalize()
            print("###", filename)
            html_path = f'./certificados_generados/{filename}.html'
            print("###", html_path)
            print(f"Now converting... ")
            pdf_path = f'./certificados_generados/{filename}.pdf'
            html2pdf(html_path, pdf_path)
            '''
        cont+=1

def html2pdf(html_path, pdf_path):
    """
    Convert html to pdf using pdfkit which is a wrapper of wkhtmltopdf
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.35in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'user-style-sheet': './style.css',
        'no-outline': None,
        'enable-local-file-access': None
    }

    pdfkit.from_file(html_path,pdf_path,options=options,css='./style.css')

    '''
    with open(html_path) as f:
        pdfkit.from_file(f, pdf_path, options=options)
    '''

if __name__ == "__main__":
    main()
