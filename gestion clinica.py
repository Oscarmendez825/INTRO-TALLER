from Clinica import Clinica
class GestionClinica:
    def __init__(self):
        self.Clinica = Clinica()
    def acciones(self):
        self.Clinica.agregarMedico("Pablo")
        self.Clinica.registrarPaciente("Pablo","Peter")
        self.Clinica.registrarPaciente("Pablo","Maria")
        print("El siguiente paciente es:", self.Clinica.siguente("Pablo"))

        self.Clinica.agregarMedico("Jose")
        self.Clinica.registrarPaciente("Jose","Mario")
        self.Clinica.registrarPaciente("Jose","Carlos")
        print("El siguiente paciente es:", self.Clinica.siguente("Jose"))
