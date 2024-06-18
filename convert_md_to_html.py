import os
import markdown

# Verzeichnisse definieren
markdown_dir = 'doku'
output_dir = 'sportseite'

# Sicherstellen, dass das Ausgabeverzeichnis existiert
os.makedirs(output_dir, exist_ok=True)

# HTML-Link-Vorlagen
link_template = '<li><a href="{filename}">{title}</a></li>'

# Liste für Linksammlung
links = []

# Markdown-Dateien durchgehen und in HTML-Dateien umwandeln
for md_filename in os.listdir(markdown_dir):
    if md_filename.endswith('.md'):
        # Pfade definieren
        md_filepath = os.path.join(markdown_dir, md_filename)
        html_filename = md_filename.replace('.md', '.html')
        html_filepath = os.path.join(output_dir, html_filename)

        # Markdown-Datei lesen
        with open(md_filepath, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        # Markdown in HTML umwandeln
        html_content = markdown.markdown(md_content)

        # Link zur Linksammlung hinzufügen
        links.append(link_template.format(filename=html_filename, title=html_filename.replace('.html', '')))

# Inhalte für index.html generieren
index_content = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sportseite</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Sportseite</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                {''.join(links)}
            </ul>
        </nav>
    </header>
    <main id="content">
        <h2>Willkommen auf der Sportseite</h2>
        <p>Wählen Sie einen der obigen Links, um den entsprechenden Text anzuzeigen.</p>
    </main>
</body>
</html>'''

# index.html schreiben
index_filepath = os.path.join(output_dir, 'index.html')
with open(index_filepath, 'w', encoding='utf-8') as index_file:
    index_file.write(index_content)

# Alle HTML-Dateien erstellen und die Navigation hinzufügen
for md_filename in os.listdir(markdown_dir):
    if md_filename.endswith('.md'):
        html_filename = md_filename.replace('.md', '.html')
        html_filepath = os.path.join(output_dir, html_filename)

        # Markdown-Datei lesen
        md_filepath = os.path.join(markdown_dir, md_filename)
        with open(md_filepath, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        # Markdown in HTML umwandeln
        html_content = markdown.markdown(md_content)

        # HTML-Inhalt in eine vollständige HTML-Seite einbetten
        full_html_content = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_filename}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Sportseite</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                {''.join(links)}
            </ul>
        </nav>
    </header>
    <main id="content">
        {html_content}
    </main>
</body>
</html>'''

        # HTML-Datei schreiben
        with open(html_filepath, 'w', encoding='utf-8') as html_file:
            html_file.write(full_html_content)

print("Konvertierung abgeschlossen!")
