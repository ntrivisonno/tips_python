import fitz  # PyMuPDF
from PIL import Image
import io

def compress_pdf(input_file, output_file, quality=10):
    # Abrimos el archivo PDF original
    pdf = fitz.open(input_file)
    new_pdf = fitz.open()  # Creamos un nuevo PDF vacío para almacenar las páginas comprimidas
    
    for page_num in range(len(pdf)):
        page = pdf[page_num]
        new_page = new_pdf.new_page(width=page.rect.width, height=page.rect.height)  # Creamos una nueva página en el PDF
        
        # Recorre todas las imágenes en la página
        images = page.get_images(full=True)
        
        for img in images:
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_data = base_image["image"]
            
            # Convertimos la imagen a un objeto PIL
            image = Image.open(io.BytesIO(image_data))
            
            # Comprimimos la imagen y guardamos en un buffer
            buffer = io.BytesIO()
            image.save(buffer, format="JPEG", quality=quality)
            compressed_image = buffer.getvalue()
            
            # Insertamos la imagen comprimida en la nueva página
            new_page.insert_image(page.rect, stream=compressed_image)
    
    # Guardamos el nuevo PDF comprimido
    new_pdf.save(output_file)
    pdf.close()
    new_pdf.close()

# Uso de la función con nombres de archivo flexibles
name_archivo_original = 'Traduccion certificado antecedentes penales.pdf'
name_archivo_comprimido = 'Traduccion certificado antecedentes penales2.pdf' 
compress_pdf(name_archivo_original, name_archivo_comprimido, quality=5)
