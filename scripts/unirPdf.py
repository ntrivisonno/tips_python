import PyPDF2

def unir_pdfs(archivo1, archivo2, archivo_salida):
    # Abrir los archivos PDF en modo de lectura binaria
    with open(archivo1, 'rb') as file1, open(archivo2, 'rb') as file2:
        # Crear objetos de lectura para ambos archivos PDF
        pdf_reader1 = PyPDF2.PdfReader(file1)
        pdf_reader2 = PyPDF2.PdfReader(file2)

        # Crear un objeto de escritura para el archivo de salida
        pdf_writer = PyPDF2.PdfWriter()

        # Agregar todas las páginas del primer archivo
        for pagina in range(len(pdf_reader1.pages)):  # Utiliza len(reader.pages)
            pdf_writer.add_page(pdf_reader1.pages[pagina])

        # Agregar todas las páginas del segundo archivo
        for pagina in range(len(pdf_reader2.pages)):  # Utiliza len(reader.pages)
            pdf_writer.add_page(pdf_reader2.pages[pagina])

        # Guardar el resultado en un nuevo archivo PDF
        with open(archivo_salida, 'wb') as file_salida:
            pdf_writer.write(file_salida)

# Ejemplo de uso
archivo1 = '/home/zeeburg/Downloads/portfolio_CAD.pdf'
archivo2 = '/home/zeeburg/Downloads/cv_Trivisonno.pdf'
archivo_salida = '/home/zeeburg/Downloads/resultadoJoinPdf.pdf'

unir_pdfs(archivo1, archivo2, archivo_salida)
