"""Genera un dataset clínico completamente ficticio de pacientes de Puebla."""

from __future__ import annotations

import csv
import math
import random
from pathlib import Path


SEMILLA = 230389
NUM_PACIENTES = 5_000
RUTA_SALIDA = Path(__file__).resolve().parents[1] / "data" / "pacientes_puebla_5000.csv"

# Coordenadas centrales aproximadas de localidades válidas del estado de Puebla.
LOCALIDADES = [
    ("Puebla", "Heroica Puebla de Zaragoza", 19.0414, -98.2063, 26),
    ("Tehuacán", "Tehuacán", 18.4615, -97.3928, 11),
    ("San Martín Texmelucan", "San Martín Texmelucan de Labastida", 19.2843, -98.4389, 8),
    ("Atlixco", "Atlixco", 18.9089, -98.4361, 8),
    ("San Pedro Cholula", "Cholula de Rivadavia", 19.0641, -98.3035, 7),
    ("Huauchinango", "Huauchinango", 20.1767, -98.0528, 6),
    ("Teziutlán", "Teziutlán", 19.8175, -97.3599, 6),
    ("Amozoc", "Amozoc de Mota", 19.0450, -98.0442, 5),
    ("Izúcar de Matamoros", "Izúcar de Matamoros", 18.6016, -98.4654, 5),
    ("Xicotepec", "Xicotepec de Juárez", 20.2750, -97.9611, 4),
    ("Zacatlán", "Zacatlán", 19.9348, -97.9613, 4),
    ("Cuautlancingo", "San Juan Cuautlancingo", 19.0895, -98.2732, 4),
    ("Tecamachalco", "Tecamachalco", 18.8814, -97.7336, 3),
    ("Acatlán", "Acatlán de Osorio", 18.2025, -98.0486, 2),
    ("Chignahuapan", "Chignahuapan", 19.8380, -98.0317, 1),
]


def limitar(valor: float, minimo: float, maximo: float) -> float:
    """Limita un número al intervalo indicado."""
    return max(minimo, min(maximo, valor))


def probabilidad_logistica(valor: float) -> float:
    """Convierte un valor en una probabilidad entre cero y uno."""
    return 1 / (1 + math.exp(-valor))


def calcular_riesgo(paciente: dict[str, object]) -> tuple[int, str]:
    """Calcula un puntaje reproducible y lo transforma en tres niveles."""
    puntos = 0
    edad = int(paciente["edad"])
    imc = float(paciente["imc"])
    sistolica = int(paciente["presion_sistolica"])
    diastolica = int(paciente["presion_diastolica"])
    glucosa = int(paciente["glucosa_mg_dl"])
    colesterol = int(paciente["colesterol_mg_dl"])

    puntos += int(edad >= 55) + int(edad >= 70)
    puntos += int(imc >= 25) + int(imc >= 30)
    puntos += int(sistolica >= 130 or diastolica >= 80)
    puntos += int(sistolica >= 140 or diastolica >= 90)
    puntos += int(glucosa >= 100) + int(glucosa >= 126)
    puntos += int(colesterol >= 200) + int(colesterol >= 240)
    puntos += {"Nunca": 0, "Exfumador": 1, "Actual": 2}[str(paciente["tabaquismo"])]
    puntos += int(paciente["actividad_fisica"] == "Baja")
    puntos += 2 * int(paciente["diabetes"] == "Sí")
    puntos += 2 * int(paciente["hipertension"] == "Sí")
    puntos += 2 * int(paciente["antecedentes_familiares"] == "Sí")

    if puntos <= 4:
        nivel = "bajo"
    elif puntos <= 9:
        nivel = "medio"
    else:
        nivel = "alto"
    return puntos, nivel


def generar_paciente(numero: int, rng: random.Random) -> dict[str, object]:
    """Genera un registro ficticio con relaciones clínicas plausibles."""
    edad = round(rng.triangular(18, 90, 43))
    sexo = rng.choices(["Mujer", "Hombre"], weights=[51, 49], k=1)[0]
    municipio, localidad, lat_centro, lon_centro, _ = rng.choices(
        LOCALIDADES, weights=[fila[4] for fila in LOCALIDADES], k=1
    )[0]

    tabaquismo = rng.choices(
        ["Nunca", "Exfumador", "Actual"],
        weights=[60, 12 + edad / 8, 24 if edad < 65 else 15],
        k=1,
    )[0]
    actividad = rng.choices(["Baja", "Moderada", "Alta"], weights=[34, 46, 20], k=1)[0]
    antecedentes = rng.choices(["No", "Sí"], weights=[72, 28], k=1)[0]

    estatura_media = 1.63 if sexo == "Mujer" else 1.72
    estatura = round(limitar(rng.gauss(estatura_media, 0.075), 1.45, 1.95), 2)
    ajuste_actividad = {"Baja": 2.2, "Moderada": 0.0, "Alta": -1.5}[actividad]
    imc_objetivo = limitar(rng.gauss(25.5 + ajuste_actividad + max(edad - 45, 0) * 0.025, 4.2), 17, 42)
    peso = round(imc_objetivo * estatura**2, 1)
    imc = round(peso / estatura**2, 1)

    p_diabetes = probabilidad_logistica(-5.0 + edad * 0.045 + (imc - 25) * 0.11)
    diabetes = "Sí" if rng.random() < p_diabetes else "No"
    p_hipertension = probabilidad_logistica(-5.1 + edad * 0.055 + (imc - 25) * 0.09)
    hipertension = "Sí" if rng.random() < p_hipertension else "No"

    sistolica = round(limitar(rng.gauss(108 + edad * 0.22 + (imc - 25) * 0.35 + (16 if hipertension == "Sí" else 0), 9), 90, 190))
    diastolica = round(limitar(rng.gauss(68 + edad * 0.10 + (imc - 25) * 0.25 + (9 if hipertension == "Sí" else 0), 6), 55, 120))
    # Evita combinaciones fisiológicamente incoherentes (presión de pulso < 20).
    diastolica = min(diastolica, sistolica - 20)
    glucosa = round(limitar(rng.gauss(139 if diabetes == "Sí" else 91 + max(imc - 25, 0) * 0.7, 20 if diabetes == "Sí" else 11), 65, 240))
    colesterol = round(limitar(rng.gauss(164 + edad * 0.48 + (9 if imc >= 30 else 0), 28), 110, 330))
    frecuencia = round(limitar(rng.gauss(72 + (4 if actividad == "Baja" else -3 if actividad == "Alta" else 0) + (3 if tabaquismo == "Actual" else 0), 8), 50, 120))

    paciente: dict[str, object] = {
        "id_paciente": f"PAC{numero:04d}",
        "edad": edad,
        "sexo": sexo,
        "municipio": municipio,
        "localidad": localidad,
        "latitud": round(lat_centro + rng.uniform(-0.018, 0.018), 6),
        "longitud": round(lon_centro + rng.uniform(-0.018, 0.018), 6),
        "peso_kg": peso,
        "estatura_m": estatura,
        "imc": imc,
        "presion_sistolica": sistolica,
        "presion_diastolica": diastolica,
        "glucosa_mg_dl": glucosa,
        "colesterol_mg_dl": colesterol,
        "frecuencia_cardiaca_lpm": frecuencia,
        "tabaquismo": tabaquismo,
        "actividad_fisica": actividad,
        "diabetes": diabetes,
        "hipertension": hipertension,
        "antecedentes_familiares": antecedentes,
    }
    puntaje, riesgo = calcular_riesgo(paciente)
    paciente["puntaje_riesgo"] = puntaje
    paciente["riesgo_cardiovascular"] = riesgo
    return paciente


def generar_dataset() -> list[dict[str, object]]:
    """Crea todos los registros usando una semilla fija."""
    rng = random.Random(SEMILLA)
    return [generar_paciente(numero, rng) for numero in range(1, NUM_PACIENTES + 1)]


def guardar_csv(registros: list[dict[str, object]]) -> None:
    """Guarda el dataset y crea el directorio de salida si no existe."""
    RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with RUTA_SALIDA.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(registros[0].keys()))
        escritor.writeheader()
        escritor.writerows(registros)


def main() -> None:
    registros = generar_dataset()
    guardar_csv(registros)
    print(f"Dataset generado: {RUTA_SALIDA}")
    print(f"Filas: {len(registros):,} | Columnas: {len(registros[0])}")


if __name__ == "__main__":
    main()
