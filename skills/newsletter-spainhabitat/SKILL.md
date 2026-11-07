---
name: newsletter-spainhabitat
description: Crea la newsletter HTML semanal de Spainhábitat para Brevo a partir de un Word, creando la carpeta de edición y reutilizando el HTML más reciente. Solicita las URLs de imágenes de WordPress y, cuando se indiquen cambios, de los banners.
---

# Newsletter semanal de Spainhábitat

Trabaja en español sobre el repositorio de newsletters del usuario. Basta con que entregue el Word e invoque esta skill: crea la estructura y prepara el HTML. La entrega es `news_semanal_DDMMYYYY/news_spain.html`, con el Word y el estado de trabajo en `texto/`. No crees `images/` ni descargues las imágenes: el usuario facilita sus URLs de WordPress. Conserva cualquier carpeta de imágenes que ya exista en una edición anterior. No publiques en WordPress ni envíes o programes campañas en Brevo por el mero hecho de preparar el HTML.

## Seleccionar edición y plantilla

- Lee las instrucciones del repositorio y comprueba los cambios existentes. Localiza el Word adjunto o indicado por el usuario; no le pidas que cree carpetas ni copie la plantilla.
- Determina la fecha de edición a partir de la indicación del usuario y, en su ausencia, de la fecha editorial del Word. Si solo figura día y mes, resuelve el año con el contexto de la campaña y las ediciones recientes; pregunta si sigue siendo ambiguo. Si no hay fecha utilizable, pide la fecha de edición sin inventarla ni usar automáticamente el día de ejecución.
- Crea `news_semanal_DDMMYYYY/` y su subcarpeta `texto/`; copia allí el Word conservando el original. Si ya está en destino, no lo copies sobre sí mismo. Si existe un archivo distinto con el mismo nombre, no lo sobrescribas: conserva ambas versiones con nombres diferenciados e identifica la fuente vigente. Si el usuario indica una carpeta existente, respeta su nombre aunque difiera de la fecha del Word. No fijes permanentemente una edición en la skill.
- Para una edición nueva, copia el `news_spain.html` de la newsletter semanal más reciente disponible, ordenando DDMMYYYY como fecha, no alfabéticamente ni por fecha de modificación. Excluye boletines especiales y ediciones con noticias o imágenes pendientes según su estado o contenido. Una fecha de envío futura no invalida una newsletter ya preparada. Si la selección resulta ambigua o no hay plantilla utilizable, pide solo esa aclaración.
- Si la carpeta destino ya contiene un HTML, trata la petición como continuación y conserva sus cambios; no lo reemplaces automáticamente con la plantilla anterior. Registra la edición usada como base para comparar después los cambios.
- Conserva los Word, las imágenes y las ediciones históricas. No regeneres el diseño desde cero ni crees variantes `emailagent` por defecto: la convención actual es un único `news_spain.html` con imágenes remotas.
- Consulta [references/patrones.md](references/patrones.md) para reconocer bloques y particularidades reales del repositorio. Inspecciona siempre la plantilla actual antes de aplicar estos patrones.

## Leer el contenido editorial

Lee el Word proporcionado y guarda su copia en `texto/` cuando hayas determinado la edición. Para una continuación, localízalo en `texto/`. Si hay versiones competidoras sin una elección clara, pregunta cuál rige. Para DOCX, ejecuta con Python 3 el helper incluido (solo biblioteca estándar):

```text
python <ruta-de-la-skill>/scripts/leer_word.py <ruta-del-word.docx>
```

Devuelve párrafos en orden, saltos internos y enlaces asociados a cada párrafo. También muestra comentarios y campos de Word si existen. No interpreta el contenido automáticamente. Para `.doc` binario usa un lector/conversor disponible y una copia temporal; no lo trates como ZIP ni modifiques el original. Si no puedes leerlo, solicita una versión DOCX.

Construye un inventario por noticia con número, categoría, título, descripción, texto del botón (CTA), URL de destino y URL WordPress. No se requiere imagen local. Recoge también el asunto para facilitar su copia en Brevo; no conviertas el asunto en un nuevo titular visible del HTML.

- Respeta orden, redacción y número de noticias del Word. No resumas ni inventes datos para encajar en una tarjeta. Señala erratas dudosas sin corregir silenciosamente nombres o contenido editorial.
- Reconoce CTA y URL tanto en el mismo párrafo como en párrafos distintos; pueden aparecer pegados (`Más infohttps://...`). También puede haber un marcador `NOTICIA 4` pegado al final de la URL anterior: sepáralo.
- Prioriza la URL explícitamente escrita junto a la noticia sobre un hipervínculo oculto heredado. Informa de discrepancias relevantes. Si no hay URL visible, usa el destino del hipervínculo asociado al CTA; nunca el primer enlace de las relaciones del documento. Ante varios destinos plausibles, pregunta sin inventar slugs.
- Las fuentes pueden incluir YouTube u otros destinos: no fuerces todos los enlaces a Spainhábitat.

## Solicitar imágenes y continuar por etapas

Asocia cada URL recibida al número y título de su noticia. No pidas archivos locales ni supongas que existen fotos numeradas en el repositorio.

Pide de una en una las URLs que falten, identificando noticia y título: «Para la noticia 1, “[título]”, pásame la URL directa de la imagen subida a WordPress». Si el usuario proporciona varias de una vez, asígnalas y pide únicamente las restantes. No repitas preguntas ya resueltas.

La URL de la imagen (`src`) es diferente de la URL de la noticia (`href`). No deduzcas rutas WordPress cambiando mes, nombre o sufijo: las subidas repetidas usan sufijos variables. No reutilices fotos remotas de la semana anterior como si fueran las nuevas. Usa una URL directa HTTP(S) de imagen, no una página de adjunto ni una ruta administrativa; solicita corrección si se recibe una de estas últimas. Comprueba su disponibilidad cuando sea posible y distingue una URL no verificada de una validada.

Mientras llegan respuestas, actualiza el texto y los enlaces conocidos. Para poder reanudar sin perder correspondencias, guarda en `texto/estado_newsletter.json` solo el inventario editorial y de banners modificados, fuentes, URLs recibidas, incidencias y pendientes. Al reanudar, contrástalo con el Word y el HTML actuales; no sobrescribas cambios posteriores con un estado antiguo. Mientras falte una imagen, sustituye su etiqueta en el borrador por un comentario identificado, por ejemplo `<!-- PENDIENTE_IMAGEN_NOTICIA_1 -->`, conservando en el estado la etiqueta original necesaria para restaurar sus dimensiones y estilos. No mantengas la imagen antigua ni inventes una URL provisional. Indica expresamente que el borrador todavía no está listo para Brevo y elimina cada marcador al recibir la URL. No marques el trabajo como completo mientras falten datos necesarios.

## Aplicar los cambios

- Edita cada bloque de noticia de forma localizada: categoría visible cuando exista, título, descripción, `alt`/`title` de su imagen, CTA y destino de todos sus enlaces. Mantén las mayúsculas de botones que use la plantilla.
- Actualiza tanto el botón HTML normal como su versión VML de Outlook (`v:roundrect`, `href` y texto en `center`). Actualiza también el enlace que envuelve la imagen y cualquier título enlazado. No hagas sustituciones globales de categorías o CTA comunes a varias noticias.
- Conserva tablas, estilos inline, clases responsive, anchos, condiciones MSO, separadores, logos, suscripción, publicaciones, redes y pie. Conserva variables de Brevo si existen; no inventes ni sustituyas su sintaxis.
- Por defecto solo cambian las noticias. Los banners mantienen imagen, enlace y posición. Si el usuario o el encargo editorial pide cambios de banners, identifica el bloque concreto, URL de imagen, destino y nueva posición; pide solo los datos ausentes. Mueve el bloque completo con su estructura de tabla y separadores pertinentes. No intercambies imagen y destino entre anunciantes.
- Para cada banner nuevo o sustituido, solicita su URL directa de imagen y el enlace de destino al hacer clic. Si el usuario indica que conserve el destino existente, no vuelvas a pedirlo. Si cambia la disposición, solicita la posición solo cuando no se haya indicado. Recoge estas respuestas por banner, sin requerir archivos locales. Comprueba sus URLs e incorpora los cambios también a las variantes de Outlook que existan.
- Si cambia el número de noticias, adapta los bloques necesarios respetando el orden editorial y la estructura existente. No descartes noticias para mantener siete. Si la disposición respecto a los banners no queda clara, pregunta por esa decisión.
- Evita reserializar todo el HTML con herramientas que eliminen comentarios condicionales. Escapa caracteres de texto y atributos correctamente, conserva UTF-8 y revisa tildes, comillas y ampersands.

## Comprobar y entregar

1. Contrasta todas las noticias con el Word: orden, categoría, título, descripción, CTA, destino e imagen. Comprueba las dos versiones de cada botón y que no queden datos de noticias anteriores en esos bloques.
2. Revisa el diff contra la base: en una actualización solo de noticias, los banners, pie, cabecera y CSS deben permanecer iguales. Informa de anomalías heredadas sin corregirlas fuera del alcance solicitado.
3. Comprueba que no haya rutas locales, `file:`, `data:`, URLs vacías ni marcadores pendientes en las imágenes de la entrega para Brevo. Revisa que las tablas y condiciones MSO conserven su estructura. No confundas un parser HTML que ignora comentarios con una comprobación de VML.
4. Si hay un visor disponible, revisa el HTML en escritorio y móvil (aprox. 600 y 375 px): títulos largos, tarjetas, imágenes, banners y botones. Esa vista no demuestra compatibilidad real en Outlook o Brevo. Si no puedes revisar visualmente o comprobar enlaces, indícalo con precisión.
5. Entrega el enlace al HTML, el asunto extraído y un resumen breve de cambios y pendientes. Distingue «borrador pendiente de imágenes» de «HTML preparado para importar». La prueba de campaña en Brevo solo se declara realizada si realmente se ha hecho.

Si el usuario pide únicamente crear o revisar esta skill, analiza las ediciones de ejemplo sin modificar su newsletter ni iniciar la recogida de imágenes.
