from empleado import Empleado
import pytest

@pytest.fixture
def employee_data ():
    employee_data = Empleado('Agustín', 'Estévez', 45000)
    return employee_data

def test_dar_aumento_predeterminado(employee_data):
    employee_data.dar_aumento()
    assert employee_data.salario_anual == 50000

def test_dar_aumento_personalizado(employee_data):
    employee_data.dar_aumento(8000)
    assert employee_data.salario_anual == 53000