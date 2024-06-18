### HTML und CSS

**HTML und CSS: Eine Einführung**

HTML (Hypertext Markup Language) und CSS (Cascading Style Sheets) sind zwei grundlegende Technologien, die gemeinsam verwendet werden, um Webseiten zu erstellen und zu gestalten. Hier ist eine kurze Erläuterung, was sie jeweils tun:

**HTML:** HTML bildet das Grundgerüst einer Webseite. Es handelt sich um eine Auszeichnungssprache, die verwendet wird, um den Inhalt einer Webseite zu strukturieren. Mit HTML werden die verschiedenen Elemente einer Webseite definiert, wie Überschriften, Absätze, Bilder, Links usw. Diese Elemente werden durch sogenannte Tags markiert, die von spitzen Klammern umschlossen sind. Zum Beispiel wird ein Absatz mit dem `<p>`-Tag markiert.

Beispiel für HTML:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Titel der Webseite</title>
</head>
<body>
    <h1>Überschrift</h1>
    <p>Dies ist ein Absatz.</p>
    <img src="bild.jpg" alt="Beschreibung des Bildes">
    <a href="https://www.beispiel.com">Link zum Beispiel</a>
</body>
</html>
```

**CSS:** CSS ist eine Stylesheet-Sprache, die verwendet wird, um das Aussehen und Layout einer Webseite zu definieren. Mit CSS können verschiedene Stileigenschaften wie Farben, Schriftarten, Abstände, Positionen usw. festgelegt werden. Indem man CSS-Regeln erstellt und sie den entsprechenden HTML-Elementen zuweist, kann man das Erscheinungsbild der Webseite gestalten.

Beispiel für CSS:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

h1 {
    color: #333333;
    text-align: center;
}

p {
    color: #666666;
    margin-bottom: 20px;
}

img {
    max-width: 100%;
    height: auto;
}
```