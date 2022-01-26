from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.table import Table


class Conexao_Planilha:


    def __init__(self,disciplina):
        self.disciplina = disciplina

    def CriandoArquivo_Excl():

        arquivo_excel = Workbook
        planilha1 = arquivo_excel.active
        planilha1['A1']= ''
        arquivo_excel.save('Arq.xlsx')

    def Adicionar(self,disciplina):

        arquivo_excel = load_workbook('arquivo.xlsx')


