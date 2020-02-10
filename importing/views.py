from django.shortcuts import render

import xlrd
from .models import Planilha
from .forms import UpdateDetailsForm


def index(request):
    return render(request, 'importing/index.html')


def importar(request):

    if (request.method == 'POST') and (request.FILES):
        form = UpdateDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['myfile']
            i=0
            book=xlrd.open_workbook(file_contents=excel_file.read())
            sh = book.sheet_by_index(0)
            for rx in range(1, sh.nrows):
                Planilha.objects.update_or_create(
                    demanda = str(sh.row(rx)[0].value),
                    categoria=str(sh.row(rx)[1].value),
                    data=xlrd.xldate.xldate_as_datetime(sh.row(rx)[2].value, book.datemode),
                    nome_pessoa=str(sh.row(rx)[3].value),
                    tel_pessoa=str(sh.row(rx)[4].value),
                    sexo=str(sh.row(rx)[5].value),
                )
                i=i+1

    return render(request, 'importing/importar.html')
