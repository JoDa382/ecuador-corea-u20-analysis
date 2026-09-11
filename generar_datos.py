import pandas as pd

# 1. KPIs Globales del Partido (Francia vs Corea)[cite: 1]
team_kpis = {
    "Equipo": ["Francia", "Corea del Sur"],
    "xG_Generado": [0.82, 0.17],
    "Recepciones_Ultimo_Tercio": [132, 38],
    "Segundas_Jugadas_Ganadas": [113, 79],
    "Presiones_Directas": [47, 72]
}

# 2. Vulnerabilidad Aérea de la Portera Surcoreana[cite: 1]
gk_stats = {
    "Jugadora": ["Kim Chaebeen (18)"],
    "Centros_Recibidos": [31],
    "Intervenciones_Aereas": [1],
    "Efectividad_Salidas": ["3.2%"]
}

# Exportación a CSV
pd.DataFrame(team_kpis).to_csv("match_fra_kor_team_kpis.csv", index=False)
pd.DataFrame(gk_stats).to_csv("match_fra_kor_gk_stats.csv", index=False)
print("Archivos CSV creados exitosamente para el modelo de datos.")