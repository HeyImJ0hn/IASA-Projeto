from mod.problema import Problema
from teste.plan_traj.mod_prob.EstadoLocalidade import EstadoLocalidade
from teste.plan_traj.mod_prob.OperadorLigacao import OperadorLigacao

# Esta classe representa um problema de planeamento.
# O problema é composto por ligações, uma localização inicial e uma localização final.
# Tem também um objetivo final.
class ProblemaPlanTraj(Problema):
    def __init__(self, ligacoes, loc_inicial, loc_final):
        self.ligacoes = ligacoes
        self.loc_inicial = loc_inicial
        self.loc_final = loc_final
        self.operadores = list(OperadorLigacao)

        for ligacao in self.ligacoes:
            self.operadores.append(OperadorLigacao(ligacao.origem, ligacao.destino, ligacao.custo))
        super().__init__(EstadoLocalidade(loc_inicial), self.operadores)

    def objectivo(self, estado):
        if estado.localidade == self.loc_final:
            return True
        return False