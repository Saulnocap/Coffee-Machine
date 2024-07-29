from src.main import Cafetera, Azucarero, Vaso, MaquinaDeCafe
from unittest.mock import patch
import pytest

class TestMaquinaDeCafe:
    @pytest.fixture
    def setup(self):
        self.cafe = Cafetera(100)  # cantidad de café en oz
        self.vasosPequenos = Vaso(10, 3)  # 10 vasos de 3 oz
        self.vasosMedianos = Vaso(10, 5)  # 10 vasos de 5 oz
        self.vasosGrandes = Vaso(10, 7)  # 10 vasos de 7 oz
        self.azucar = Azucarero(50)  # cantidad de azúcar en cucharadas

        self.maquina = MaquinaDeCafe(self.cafe, self.vasosPequenos, self.vasosMedianos, self.vasosGrandes, self.azucar)

    def test_getTipoVaso(self, setup):
        assert self.maquina.getTipoVaso("pequeño") == self.vasosPequenos
        assert self.maquina.getTipoVaso("mediano") == self.vasosMedianos
        assert self.maquina.getTipoVaso("grande") == self.vasosGrandes

    @patch('builtins.input', return_value='no')
    def test_existen_vasos(self, mock_input, setup):
        assert self.maquina.getTipoVaso("pequeño") == self.vasosPequenos
        assert self.maquina.getTipoVaso("mediano") == self.vasosMedianos
        assert self.maquina.getTipoVaso("grande") == self.vasosGrandes

    @patch('builtins.input', return_value='no')
    def test_no_existen_vasos(self, mock_input, setup):
        self.vasosPequenos.setCantidadVasos(0)
        assert self.maquina.getVasoDeCafe("pequeño", 1, 1) == False

    @patch('builtins.input', return_value='no')
    def test_resta_vasos(self, mock_input, setup):
        self.maquina.getVasoDeCafe("pequeño", 1, 1)
        assert self.vasosPequenos.getCantidadVasos() == 9

    @patch('builtins.input', return_value='no')
    def test_existe_cafe(self, mock_input, setup):
        assert self.cafe.getCantidadDeCafe() == 100

    @patch('builtins.input', return_value='si')
    def test_no_existe_cafe(self, mock_input, setup):
        self.cafe.setCantidadDeCafe(0)
        assert self.maquina.getVasoDeCafe("pequeño", 1, 1) == False

    @patch('builtins.input', return_value='no')
    def test_resta_cafe(self, mock_input, setup):
        self.maquina.getVasoDeCafe("pequeño", 1, 1)
        assert self.cafe.getCantidadDeCafe() == 97

    @patch('builtins.input', return_value='no')
    def test_suficiente_azucar(self, mock_input, setup):
        assert self.azucar.getCantidadDeAzucar() == 50

    @patch('builtins.input', return_value='no')
    def test_no_suficiente_azucar(self, mock_input, setup):
        self.azucar.setCantidadDeAzucar(0)
        assert self.maquina.getVasoDeCafe("pequeño", 1, 1) == False

    @patch('builtins.input', return_value='no')
    def test_resta_azucar(self, mock_input, setup):
        self.maquina.getVasoDeCafe("pequeño", 1, 1)
        assert self.azucar.getCantidadDeAzucar() == 49

if __name__ == "__main__":
    pytest.main()
