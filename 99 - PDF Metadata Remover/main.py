from pikepdf import Pdf

file_name = input("Temizlenecek PDF: ")
output_name = "clean_" + file_name

pdf = Pdf.open(file_name)

# Metadata'yı sil
del pdf.docinfo
# XMP Metadata'yı sil (Varsa)
if '/Metadata' in pdf.Root:
    del pdf.Root.Metadata

pdf.save(output_name)
print(f"[+] Metadata temizlendi -> {output_name}")