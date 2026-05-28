import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def getYears(self):
        return DAO.getYears()

    def creaGrafo(self, anno):
        self._grafo.clear()
        self._idMap.clear()

        nodi = DAO.getNodes(anno)

        for nodo in nodi:
            codice = nodo["CCode"]
            nome = nodo["StateNme"]

            self._idMap[codice] = nome
            self._grafo.add_node(nome)

        archi = DAO.get_archi(anno)

        for arco in archi:
            stato1 = self._idMap[arco["state1no"]]
            stato2 = self._idMap[arco["state2no"]]

            self._grafo.add_edge(stato1, stato2)

        for stato in self._grafo.nodes:
            n_confini = self._grafo.degree[stato]
            print(f"{stato} - {n_confini} vicini.")


    def getNCompConn(self):
        return nx.number_connected_components(self._grafo)

    def getDettagliNodi(self):
        dettagli = []

        for stato in sorted(self._grafo.nodes):
            n_vicini = self._grafo.degree[stato]
            dettagli.append((stato, n_vicini))

        return dettagli