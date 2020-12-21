'''
Zadanie, ktore napisal los:)
    merge1pagePdfsDzastus(abspath) - znajdz kazdy 1-stronicowy pdf w kazdym folderze w danej abspath.
                                    stworz w kazdym folderze nowy pdf nazwany zgodnie z nazwa folderu. pdf powinien
                                    byc polaczeniem wszystkich 1-stronciowych pdfow w danym folderze

    infoMergedPdfsDzastus(abspath) - lista wszystkich pdfow oraz ich lokalizacja posrednia

    deleteMergedPdfsDzastus(abspath) - kasuje pdfy powstale w ramach def merge1pagePdfsDzastus(abspath). Zwraca info o braku
                                        elementow do skasowania, gdy takowych nie ma(gdy def merge nie byla wczesniej uzyta)

Funkcje potrzebuja 1 argumentu - abspath - umnie znajdowal sie folder na puplicie.
Odkomentuj, okresl swoja abspath i sprawdz czy dziala:)

PS: Musisz zainstalowac biblioteke PyPdf2 -> [terminal]python -m pip install PyPDF2

'''
def deleteMergedPdfsDzastus(abspath):
    import os

    sciezka = abspath
    os.chdir(sciezka)
    num = 0
    foldery = []
    trails = []
    print('Szukamy pliki, ktore moga sie nazywac: ')
    for folder, subfolders, filenames in os.walk(sciezka):
        for subfolder in subfolders:
            trail = os.path.join(os.path.realpath(folder), subfolder)
            fdr = str(subfolder) + '.pdf'
            foldery.append(fdr)
    print(foldery)
    for folder, subfolders, filenames in os.walk(sciezka):
        for subfolder in subfolders:
            trail = os.path.join(os.path.realpath(folder), subfolder)
            for plik in os.listdir(trail):
                if os.path.basename(plik) in foldery:
                    num += 1
                    os.remove(os.path.join(os.path.realpath(trail), os.path.basename(plik)))
                    # print(os.path.join(os.path.realpath(trail), os.path.basename(plik)))
    if num == 0:
        print('Brak plikow do skasowania.')
    else:
        print('Gotowe, skasowano.')



#########create Dzastus merged pdf files directly z walk
def merge1pagePdfsDzastus(abspath):

    from PyPDF2 import PdfFileReader, PdfFileWriter
    import os
    from timeit import default_timer as tajm

    start = tajm()
    os.chdir(abspath)
    sciezka = abspath
    for folder, subfolders, filenames in os.walk(sciezka):
        for subfolder in subfolders:
            trail = os.path.join(os.path.realpath(folder), subfolder)
            os.chdir(trail)
            PdfWriter = PdfFileWriter()
            for pdf in os.listdir(trail):
                if pdf.endswith('.pdf'):
                    paf = os.path.join(trail, os.path.basename(pdf))
                    PdfReader = PdfFileReader(paf)
                    if pdf.endswith('.pdf') and PdfReader.numPages == 1:
                        paf = os.path.join(trail, os.path.basename(pdf))
                        PdfReader = PdfFileReader(paf)
                        print(f'merging file...{pdf}')
                        PdfWriter.appendPagesFromReader(PdfReader)
                with open(str(f'{os.path.basename(subfolder)}.pdf'), 'wb') as newfile:
                    PdfWriter.write(newfile)
    end = tajm()
    ile = end - start
    print(f'Work done. Pdfs created in {round(ile, 2)} sec. ')



 ##############pdfy vol3 z walk
def infoMergedPdfsDzastus(abspath):
    import os
    paf = abspath
    pedeefs = []
    print(f'Pdfy w pliku:')
    for folder, subfolders, filenames in os.walk(paf):
        print(f'{os.path.basename(folder)}')
        en = 0
        for plik in filenames:
            if plik.endswith('.pdf'):
                pedeefs.append(plik)
                # print(f'    {filenames.index(plik)+1}) {plik}')
                print(f'    {en + 1}) {plik}')
                en += 1
    if (len(pedeefs) % 10) < 5:
        print(f'\nLacznie: {len(pedeefs)} pliki. ')
    else:
        print(f'\nLacznie: {len(pedeefs)} plikow. ')





######################  Odkomentuj, okresl swoja abspath i sprawdz czy dziala:)


# merge1pagePdfsDzastus('C:\\Users\\ACER\\Desktop\\Dzastusiowo')
# infoMergedPdfsDzastus('C:\\Users\\ACER\\Desktop\\Dzastusiowo')
# deleteMergedPdfsDzastus('C:\\Users\\ACER\\Desktop\\Dzastusiowo')



