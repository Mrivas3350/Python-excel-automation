import pandas as pd

input_file = "input/ventas_raw.xlsx"
output_file = "output/reporte_final.xlsx"

df = pd.read_excel(input_file)

# Normalizar nombres de columnas (quita espacios, pasa a minúsculas)
df.columns = df.columns.str.strip().str.lower()

# Limpieza básica
df.dropna(inplace=True)

# Calcular total por fila
df["total"] = df["cantidad"] * df["precio_unitario"]

# Resúmenes
resumen_cliente = df.groupby("cliente")["total"].sum().reset_index()
resumen_producto = df.groupby("producto")["total"].sum().reset_index()

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Datos Limpios", index=False)
    resumen_cliente.to_excel(writer, sheet_name="Resumen por Cliente", index=False)
    resumen_producto.to_excel(writer, sheet_name="Resumen por Producto", index=False)

print("Reporte generado correctamente.")

