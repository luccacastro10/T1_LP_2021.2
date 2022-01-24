import os

class agenda:

    def __init__(self, path):
        self._path = path

    def ler(self, lines):
        for line in lines:
            print(line)

    def escrever(self, agenda):

        nome = input("\nEntre com o nome: ")
        end = input("Entre com o endereço: ")
        contato = input("Entre com o contato: ")

        agenda.writelines( nome + ", " + end + ", " + contato + "\n")
        print("Agenda atualizada!")

    def escrever(self, agenda, nome, contato, end):
        agenda.writelines( nome + ", " + end + ", " + contato + "\n")
        print("Agenda atualizada!")

    def remover(self, agenda, lines):
        print("\nPrimeiramente busque pela informação que quer remover!")
        lineAt = self.buscar(lines)

        rmLines = []
        i = 1
        n = "\n"

        for rm in lineAt:

            if rm != lineAt[0]:
                n = ""

            cmd = input( n + "Deseja remover a linha %i da agenda? (s/n) " % rm)

            if (cmd == "s"):
                rmLines.append(rm)
            if (cmd == "n"):
                pass

        if len(rmLines) != 0:
            agenda.close()
            agendaAux = open(self._path, "w")

            for j in rmLines:
                lines.pop(j-i)
                i += 1

            for line in lines:
                agendaAux.write(line)

            agendaAux.close()
            print("Linhas removidas com sucesso!")
        else:
            print("Nenhuma linha foi removida")

    def buscar(self, lines):
        
        busca = input("\nEntre com a informação que quer buscar: ")
        j = 1
        i = 0
        lista = []
        n = "\n"

        for line in lines:
            info = line.find(busca)

            if(info != -1):
                if line != lines[0]:
                    n = ""
                line = line.split("\n")
                print(n + line[0] + " -> Linha %i" %j)
                lista.insert(i, j)
                i += 1
        
            j += 1

        if not i:
            print("Informação não encontrada!")
            
        return lista
