import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        anno = self._view._txtAnno.value

        if anno is None or anno.strip() == "":
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Attenzione, inserire un anno tra 1816 e 2016.",
                                                           color="red"))
            self._view.update_page()
            return

        try:
            year = int(anno)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Attenzione, inserire un anno tra 1816 e 2016.",
                                                           color="red"))
            self._view.update_page()
            return


        if year < 1816 or year > 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Attenzione, inserire un anno tra 1816 e 2016.",
                                                           color="red"))
            self._view.update_page()
            return

        self._model.creaGrafo(year)

        n_componenti = self._model.getNCompConn()
        dettagli_nodi = self._model.getDettagliNodi()

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(
            ft.Text("Grafo correttamente creato.", color="green"))
        self._view._txt_result.controls.append(
            ft.Text(f"Il grafo ha {n_componenti} componenti connesse."))
        self._view._txt_result.controls.append(
            ft.Text("Di seguito i dettagli sui nodi:"))

        for stato, n_vicini in dettagli_nodi:
            self._view._txt_result.controls.append(
                ft.Text(f"{stato} - {n_vicini} vicini."))

        self._view.update_page()
