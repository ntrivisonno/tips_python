"""
%@author: ntrivisonno

script that plots forcesCoef form OpenFOAM
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

class Plotter:
    def __init__(self, case_folder=None):
        if case_folder is None:
            case_folder = os.getcwd()
        self.case_path = os.path.join(case_folder, "")  # Agregando el separador de directorios al final
        self.coefficients = None

    def read_coefficients(self):
        file_path = os.path.join(self.case_path, "postProcessing/forceCoeffs1/0/coefficient.dat")
        self.coefficients = pd.read_csv(file_path, skiprows=12, delim_whitespace=True, dtype=float)

        # Proceso para manejar el whitespace y eliminar la última columna
        name_cols = list(self.coefficients.columns[1:])
        self.coefficients = self.coefficients.iloc[:, :-1]
        self.coefficients.columns = name_cols

    def filter_coefficients(self):
        if self.coefficients is None:
            print("Error: No se han leído los coeficientes. Llama a read_coefficients() primero.")
            return

        # Filtramos las columnas y nos quedamos con los coeficientes totales
        self.coefficients = self.coefficients.loc[:, ~self.coefficients.columns.str.contains('\(f\)|\(r\)')]

    def plot_coefficients(self, save_figures=False):
        if self.coefficients is None:
            print("Error: No se han leído los coeficientes. Llama a read_coefficients() primero.")
            return

        figures_folder = os.path.join(self.case_path, "Figures")
        os.makedirs(figures_folder, exist_ok=True)  # Crear la carpeta si no existe

        for column in self.coefficients.columns:
            plt.figure()
            plt.plot(self.coefficients['Time'], self.coefficients[column], label=column)
            plt.xlabel('Time')
            plt.ylabel(column)
            plt.title(column)
            plt.legend()
            plt.grid()

            if save_figures:
                figure_path = os.path.join(figures_folder, f"{column}_plot.png")
                plt.savefig(figure_path, bbox_inches="tight")
                print(f"Figura guardada en: {figure_path}")

            #plt.show()

if __name__ == "__main__":
    '''
    # Indicar case_folder, por defecto directorio actual
    case_folder = "/home/zeeburg/Documents/Simulaciones/OpenFOAM/casosVarios/Ma0.15omega42.5grid2/"
    plotter = Plotter(case_folder)
    '''
    
    plotter = Plotter()
    plotter.read_coefficients()
    plotter.filter_coefficients()
    plotter.plot_coefficients(save_figures=True)

    print('#--------------------------------------------')
    print('\n FIN, OK!')
    plt.show()
