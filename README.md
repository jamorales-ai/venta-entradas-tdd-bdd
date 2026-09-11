# 🎟️ ETickets - MVP con TDD/BDD

## 📌 Descripción  
ETickets es un prototipo de sistema de venta de entradas para eventos, desarrollado en Python aplicando los principios de TDD (Test Driven Development) y BDD (Behavior Driven Development). El proyecto se centra en implementar un MVP (Minimum Viable Product) validado mediante pruebas unitarias y de aceptación.

---

## 🚀 Funcionalidades principales  
- Creación de eventos con aforo máximo y precio por entrada.  
- Registro de eventos en el sistema de ventas.  
- Validación de disponibilidad de entradas.  
- Venta de entradas con reglas de negocio: evento existente, cantidad válida (> 0), aforo disponible.  
- Cálculo de totales con aplicación de descuentos.  
- Manejo de errores mediante excepciones personalizadas (VentaError).  

---

## 🧪 Pruebas  
El proyecto incluye dos tipos de pruebas:  

**Pruebas unitarias (tests/test_unitarias.py):** validan casos específicos de cada funcionalidad, como creación de eventos, disponibilidad de entradas, registro de eventos, ventas válidas e inválidas y cálculo de totales con descuento.  

**Pruebas de aceptación (tests/test_aceptacion.py):** proporcionadas por el profesor, verifican el comportamiento esperado desde el punto de vista del usuario final. Ejemplos: un evento inicia con 0 entradas vendidas, se puede vender dentro del aforo disponible, no se puede vender más entradas que las permitidas y el cálculo de descuento funciona correctamente.  

**Evidencia:**  
El ciclo TDD se refleja en la ejecución de pruebas.  
- Fase ROJA: todas las pruebas fallan inicialmente (NotImplementedError).  
- Fase VERDE: tras la implementación, todas las pruebas pasan correctamente.  

Ejemplo de salida final:  

```
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\jamor\.conda\envs\spyder-env\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jamor\OneDrive\Universidad Internaciones\Tareas de UNI\Sexto Semestre\Ingeniería del Software Avanzada\Actividad 2
configfile: pytest.ini
collecting ... collected 16 items

test_aceptacion.py::test_aceptacion_crear_evento_inicia_sin_entradas_vendidas PASSED [  6%]
test_aceptacion.py::test_aceptacion_vender_entradas_dentro_del_aforo PASSED [ 12%]
test_aceptacion.py::test_aceptacion_no_se_puede_vender_mas_entradas_que_el_aforo PASSED [ 18%]
test_aceptacion.py::test_aceptacion_no_se_puede_vender_a_un_evento_inexistente PASSED [ 25%]
test_aceptacion.py::test_aceptacion_no_se_puede_vender_cantidad_invalida PASSED [ 31%]
test_aceptacion.py::test_aceptacion_calculo_de_total_con_descuento PASSED [ 37%]
test_aceptacion.py::test_aceptacion_descuento_invalido_lanza_error PASSED [ 43%]
test_unitarias.py::test_evento_inicia_con_aforo_y_precio PASSED          [ 50%]
test_unitarias.py::test_evento_hay_disponibilidad_true_y_false PASSED    [ 56%]
test_unitarias.py::test_registrar_evento_lo_guarda_en_sistema PASSED     [ 62%]
test_unitarias.py::test_vender_entradas_valido_actualiza_aforo PASSED    [ 68%]
test_unitarias.py::test_vender_entradas_evento_inexistente_lanza_error PASSED [ 75%]
test_unitarias.py::test_vender_entradas_cantidad_invalida_lanza_error PASSED [ 81%]
test_unitarias.py::test_vender_entradas_excede_aforo_lanza_error PASSED  [ 87%]
test_unitarias.py::test_calcular_total_con_descuento_valido PASSED       [ 93%]
test_unitarias.py::test_calcular_total_con_descuento_invalido_lanza_error PASSED [100%]

============================= 16 passed in 0.03s ==============================
```


---

## ⚙️ Instalación y uso  
1. Clonar el repositorio:  
   git clone https://github.com/albasagas/venta-entradas-tdd.git  
   cd venta-entradas-tdd  

2. Instalar dependencias:  
   pip install pytest  

3. Ejecutar pruebas unitarias:  
   pytest tests/test_unitarias.py -v  

4. Ejecutar todas las pruebas (unitarias + aceptación):  
   pytest -v  

---

## 📂 Estructura del proyecto  

---
venta-entradas-tdd/
│
├── venta_entradas/
│   └── modelos.py
│
├── tests/
│   ├── test_unitarias.py
│   └── test_aceptacion.py
│
└── README.md
---


---

## 👨‍💻 Autor  
José Andrés Morales Mijangos  
Universidad Internaciones — Ingeniería del Software Avanzada  
Actividad #2 — Desarrollo de producto MVP con TDD/BDD  

---
