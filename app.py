import streamlit as st
import graphviz

# Configuración básica de la página
st.set_page_config(page_title="Diagrama de Ensayo", layout="centered")

st.title("Diagrama de Flujo: Ensayo de Suelos")
st.write("Este diagrama detalla el proceso de análisis granulométrico y por tamizado.")

# Crear el objeto Graphviz
dot = graphviz.Digraph(comment='Diagrama de Ensayo de Suelos')
dot.attr(rankdir='TB', size='8,10') # TB = Top to Bottom (De arriba a abajo)

# Configurar estilos generales
dot.attr('node', fontname='Helvetica', shape='box', style='rounded,filled', fillcolor='#f8f9fa', color='#dee2e6')
dot.attr('edge', fontname='Helvetica', color='#6c757d')

# Nodos Comunes
dot.node('A', 'INICIO', shape='ellipse', fillcolor='#2ecc71', color='#27ae60', fontcolor='white')
dot.node('B', 'Registrar datos del proyecto\ny de la muestra')
dot.node('C', 'Identificar y describir\nvisualmente la muestra')
dot.node('D', '¿Pasa el tamiz\nde 2.0 mm (No. 10)?', shape='diamond', fillcolor='#f1c40f', color='#f39c12')

# Nodos Rama Izquierda (No pasa)
dot.node('E', 'Análisis por tamizado:\nFracción retenida')
dot.node('F', 'Separar fracción en la\nserie de tamices')
dot.node('G', 'Realizar tamizado mecánico\n(verificar <1% de paso)')
dot.node('H', 'Pesar cada fracción retenida\n(Tolerancia máx. 1%)')

# Nodos Rama Derecha (Sí pasa)
dot.node('I', 'Análisis granulométrico:\nFracción pasante')
dot.node('J', 'Determinar corrección\ncompuesta del hidrómetro')
dot.node('K', 'Calcular humedad higroscópica\n(Secado a 110°C)')
dot.node('L', 'Dispersar muestra con\nhexametafosfato de sodio')

# Nodo de Cierre
dot.node('M', 'FIN', shape='ellipse', fillcolor='#e74c3c', color='#c0392b', fontcolor='white')

# Conexiones
dot.edges(['AB', 'BC', 'CD'])

# Aristas con etiquetas para la decisión
dot.edge('D', 'E', label=' NO')
dot.edge('D', 'I', label=' SÍ')

dot.edges(['EF', 'FG', 'GH'])
dot.edges(['IJ', 'JK', 'KL'])

dot.edge('H', 'M')
dot.edge('L', 'M')

# Renderizar el gráfico en Streamlit
st.graphviz_chart(dot, use_container_width=True)

# Opcional: Agregar un botón para mostrar más detalles
with st.expander("Ver detalles técnicos del proceso"):
    st.markdown("""
    **Notas técnicas del proceso original:**
    *   **Tamices:** Serie de (3"), (2"), (1 ½"), (1"), (3/4"), (3/8"), (No. 4) y (No. 10).
    *   **Hidrómetro 151 H / 152 H:** La corrección varía según el modelo.
    *   **Dispersión:** Usar 50g para limos/arcillas o 100g para arenas con 125 ml de solución (40 g/litro).
    """)
