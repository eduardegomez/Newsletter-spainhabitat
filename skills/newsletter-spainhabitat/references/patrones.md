# Patrones observados en el repositorio

Análisis realizado sobre `news_semanal_13102026`, `news_semanal_20102026`, `news_semanal_27102026` y `news_semanal_03112026`, y la carpeta preparada `news_semanal_11112026`. Son referencias históricas, no valores que deban perpetuarse.

Actualización del flujo por indicación del usuario: las nuevas ediciones parten únicamente del Word entregado. La skill crea la carpeta de edición con `texto/` y `news_spain.html`, reutiliza el HTML semanal más reciente y solicita las URLs de imágenes y de banners modificados. No crea `images/`. Las menciones a fotos locales de este documento describen solo las ediciones históricas.

## Diseño reciente

- HTML en español, tablas de presentación de 600 px, estilos inline y media query a 600 px. Destacado azul `#275b8a`, tarjetas secundarias grises y botones con alternativa VML para Outlook.
- Cabecera con banner de anunciante y logo FEVAMA, logo Spainhábitat y suscripción.
- Una noticia destacada; banner horizontal; pareja 2–3; fila de tres banners; pareja 4–5; otra fila de tres banners; pareja 6–7; fila de dos banners.
- Pie con calendario de ferias, tres publicaciones, FEVAMA y redes. No forma parte de las siete noticias.
- Comentarios útiles: `ARTICULO DESTACADO`, `FIN ARTÍCULO DESTACADO`, `NOTICIA 2 Y NOTICIA 3`, `NOTICIA 2`, `NOTICIA 3`, `NOTICIA 4 Y NOTICIA 5`, `Noticia 4`, `Noticia 5`, `NOTICIA 6 y NOTICIA 7`, `NOTICIA 6`, `NOTICIA 7`, `INICIO FOOTER`. No todos los bloques tienen marcadores de cierre equivalentes: inspecciona sus límites reales.
- Cada noticia tiene un enlace en la imagen, otro en el botón HTML y otro en VML. El destacado no tiene la misma etiqueta de categoría visible que las tarjetas: en la copia de noviembre la categoría aparece en `alt` y `title`. No añadas una nueva etiqueta visual sin encargo.
- Botones en mayúsculas; textos editoriales en la caja original. Las noticias pueden enlazar a YouTube.

## Fuentes y discrepancias

- Word: asunto seguido de `NOTICIA N`, categoría, título, descripción y CTA con URL. Hay variaciones de saltos y párrafos; la numeración no equivale necesariamente a una lista estructurada de Word.
- En octubre aparecen marcadores pegados a la URL anterior. En el Word de noviembre aparece `Más infohttps://...`.
- Hay relaciones de hipervínculos obsoletas incluso cuando la URL visible es correcta, tanto en octubre como en la edición nueva. Recupera cada enlace con su párrafo y prioriza el texto explícito del encargo.
- Los nombres de carpeta, fecha editorial y nombre del Word pueden diferir: `03112026/texto/newsletter 3-10.docx` dice 3/11; `11112026/texto/newsletter 10-11.docx` dice 10/11. No renombres ni cambies fechas por inferencia.
- El README histórico menciona `news_spain_emailagent.html`, pero las ediciones recientes usan `news_spain.html` con URLs externas. La petición del usuario confirma esta convención.
- Rutas de fotos observadas: `https://www.spainhabitat.es/spainhabitat/wp-content/uploads/YYYY/MM/foto-N[-sufijo].jpg`. Los sufijos de octubre cambian entre ediciones; no son una regla para generar nuevas URLs.

## Caso de partida 11112026

Al analizarlo, su HTML era idéntico al de 03112026 y contenía las noticias anteriores. Ya existían siete imágenes `foto-1.jpg` a `foto-7.jpg`. El encargo es actualizar solo noticias, manteniendo banners. El Word contiene:

1. Ferias — Las empresas de Asemad refuerzan su presencia en Maderalia.
2. Premios — Un habitación compartida gana el Premio InterCIDEC 2026 (redacción literal del Word).
3. Jornada — CIR4FUN aborda el pasaporte digital del mueble en Maderalia.
4. Ferias — La oficina flexible marcó tendencia en Orgatec.
5. Empresa — Aidimme y Fevama lideran un clúster innovador de la madera y mueble en la CV.
6. Jornada — La madera transparente protagoniza una jornada en el Parque Tecnológico.
7. Producto — Vefer impulsa espumas de poliuretano con materiales renovables y reciclados.

Relee el Word al ejecutar: este inventario no sustituye a la fuente ni confirma sus imágenes remotas.

Anomalía heredada de la plantilla: el banner superior muestra SCM, pero su enlace apunta a Orgatec. En modo «solo noticias», conservarlo y señalarlo; no decidir un nuevo destino por cuenta propia.
