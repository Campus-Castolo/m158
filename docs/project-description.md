# WordPress CMS Migration

WordPress basiert auf einer Client-serverbasierten Architektur und verwendet eine MySQL-Datenbank zur Speicherung von Inhalten, Einstellungen und Benutzerinformationen. Die Dateistruktur umfasst den WordPress-Kern, der in PHP geschrieben ist und die grundlegenden Funktionen wie Benutzerverwaltung, Datenbankinteraktion und Seitenrendering steuert. Das Aussehen der Website wird durch Themes bestimmt, die HTML und CSS verwenden, um das Design und Layout festzulegen.

Die Datenbank enthält Tabellen für Beiträge, Seiten, Benutzer und weitere Informationen. PHP-Dateien innerhalb des WordPress-Kerns verarbeiten Anfragen, interagieren mit der Datenbank und generieren dynamisch HTML-Seiten. Themes bestehen aus PHP-Dateien für Templates und Funktionen sowie CSS-Dateien für das Styling. Plugins, ebenfalls in PHP geschrieben, erweitern die Funktionalität von WordPress durch Hinzufügen von benutzerdefinierten Funktionen.

Die Trennung von Inhalt (Datenbank), Logik (PHP) und Präsentation (HTML/CSS) ermöglicht eine flexible Anpassung und Erweiterung. Die Kommunikation zwischen Server und Client erfolgt über HTTP, wobei der Server die vom Benutzer angeforderten Seiten dynamisch generiert. Insgesamt bildet diese Struktur die Grundlage für die Benutzerfreundlichkeit, Flexibilität und Erweiterbarkeit von WordPress als Content-Management-System.



## Ausgangslage

Die WordPress Applikation unter der URL https://m158.geekz.ch/ (Sie erhalten weiter unten die FTP-Zugangsdaten für das Backup) soll auf einen neuen Server migriert werden. Ihre Aufgabe besteht darin, die neue Zielumgebung aufzusetzen und im Anschluss die Applikation von A nach B zu migrieren. WordPress Migrationsplugins sind nicht erlaubt.

Der neue Webserver soll unter Linux ausgeführt werden. Sie sind aber frei in er Wahl der Linux Distribution, Webserver und Datenbankserver, solange diese für WordPress geeignet sind.



## Bewertung

### Die 5 Phasen

Im Idealfall findet nach jeder Phase eine Bewertung statt. Die Summe der Bewertung der Phasen ergeben Ihre Modulnote für die LB2.

[LB2 in 5 Phasen eingeteilt](https://www.canva.com/design/DAGE0-f_l6s/XaV7MXZydNbe91pl6_tZLw/view?utm_content=DAGE0-f_l6s&utm_campaign=designshare&utm_medium=link&utm_source=editor)

> [!IMPORTANT]
>
> Lassen Sie jede Phase von der Lehrkraft korrigieren, bevor Sie mit der nächsten Phase fortfahren.
>



### GIT-Repository

Jede Studentin und jeder Student erstellt sein eigenes Repository. Dieses Repository dient als Speicherort für alle Inhalte zu M158 - LB2. Es wird empfohlen ein öffentliches Repository zu erstellen, damit die Lehrperson jederzeit darauf zugreifen kann. Speichern Sie den Link zum Repository in Ihrem privaten Teams-Kanal.

#### Struktur des Repositorys

- 01 - Dokumentation (Ihre Doku nach dieser [Vorlage](../../04_Unterrichtsressourcen/05_Vorlage) gegliedert)
- 02 - WordPress (Files für die Migration)
  - Backup
  - Application
  - Config
  - 
- 03 - Diverses
  - Vorlage Bewertungsraster (Siehe Abschnitt Bewertung)
  - Logins
  - Links



> [!TIP]
>
> SmartGit ist für schulische Zwecke kostenlos und vereinfacht das Handling 
> https://www.syntevo.com/register-non-commercial/#academic



 ###  Bewertung im Detail

**Für die Bewertung von LB2 wird Ihre Dokumentation im GIT-Repository angeschaut (GIT)**

- Jede Schülerin und jeder Schüler wird nach der [Kompetenzmatrix](https://gitlab.com/ch-tbz-it/Stud/m158/-/blob/main/08_Kompetenznachweise/Kompetenzmatrix-LB2.md) im [Bewertungsraster](https://gitlab.com/ch-tbz-it/Stud/m158/-/blob/main/02_Projekt%20Migration/WordPress-Web-App-Migration/LB2%20BewertungsrasterV25.xlsx) bewertet. Kompetenzmatrix und Bewertungsrasters decken sich 1 zu1. Das Bewertungsraster ist lediglich eine Excel-Datei in welchem auch Ihr aktueller Stand festgehalten wird.

  > [!WARNING]
  >
  > Für jeden Schüler wird ein privater Teamkanal eingerichtet. Dort wird das Bewertungsraster verlinkt und Sie können jederzeit sehen, wo sie stehen. Nur der Lehrer hat Schreibrechte.
  

> [!IMPORTANT]
>
> Jegliche Kommunikation mit der Lehrperson im Bezug auf die LB2 muss dringend über den privaten Kanal erfolgen. Markieren Sie die Lehrperson mit @Name_der_Lehrperson im Teams, damit  diese eine Notifikation erhält.

> [!IMPORTANT]
>
> Speichern Sie das Bewertungsraster lokal ab und füllen Sie es mit Ihrem Namen aus und speichern Sie dieses in Ihr GIT-Repo unter "03 - Diverses -> Vorlage Bewertungsraster %Ihr_Name%"

## Vorgehen

1. Erstellen Sie ein neues öffentliches Repository fürs M158(LB2)

2. Speichern Sie die URL des Repositorys in Ihren privaten Teams-Kanal

3. Laden Sie das Bewertungsraster herunter und speichern Sie dieses ausgefüllt in Ihrem Teams-Kanal

4. Schreiben Sie Ihre E-Mail-Adresse auf welcher die AWS-Umgebung registriert werden soll in den privaten Teams-Kanal

5. Starten Sie mit dem Projekt.

   > [!NOTE]
   >
   > Wenn Sie an einem Punkt trotz Google, ChatGPT und andere Hilfsmittel länger als 20 Min feststecken, suchen Sie sich umgehend Hilfe. Die Lehrperson hilft Ihnen dann gerne weiter.



### FTP-Quellsystem (FULL WordPress-Backup)

User: m158

Pass: Zh42p_z82

Verbinden Sie sich mit einem FTP-Client und laden Sie das Backup für die Migration herunter. 