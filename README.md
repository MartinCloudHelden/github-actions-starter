# Erste CI-Pipeline mit GitHub Actions

## Ziel

Du erstellst selbst eine GitHub-Actions-Pipeline für ein fertiges Python-Programm. Die Pipeline soll bei Änderungen automatisch die vorhandenen Tests ausführen. Das Programm enthält absichtlich **einen Fehler**. Zuerst machst du einen fehlgeschlagenen Testlauf sichtbar. Danach findest und behebst du den Fehler anhand des Testberichts.

**Du entwickelst keinen neuen Anwendungscode und keine neuen Tests.** Du erstellst eine Workflow-Datei und änderst später eine kleine Stelle im vorhandenen Programm.

## Was das Programm tun soll

`shop/versand.py` berechnet Versandkosten für einen Warenwert in Euro:

| Warenwert | Versandkosten |
|---|---:|
| Unter 50,00 € | 4,90 € |
| Ab 50,00 € einschließlich | 0,00 € |
| Negativ | Fehler (`ValueError`) |

`gesamtpreis` addiert Warenwert und Versandkosten. Die Tests in `tests/test_versand.py` beschreiben diese Regeln. Das Programm verwendet `Decimal`, damit Geldbeträge exakt dargestellt werden.

## Voraussetzungen

1. Du brauchst ein [GitHub-Konto](https://github.com/signup) und ein eigenes Repository für deine Änderungen. Das Kurs-Repository ist öffentlich. **Forke** es über **Fork → Create fork** in deinen Account. Öffne danach im Fork den Tab **Actions** und aktiviere Workflows, falls GitHub danach fragt. Erstelle deinen Pull Request später **innerhalb deines Forks**: Arbeitsbranch → `main` deines Forks. [GitHub: Repository forken](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo) · [GitHub: Workflow-Ereignisse in Forks](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflows-in-forked-repositories).
2. Wenn du lieber **klonst**, klone das Kurs-Repository über **Code → HTTPS** auf deinen Rechner. Erstelle auf GitHub ein eigenes **leeres** Repository ohne automatisch angelegte README oder `.gitignore`, setze im lokalen Klon `origin` auf dessen URL und pushe `main` dorthin. Das reine Klonen gibt dir keinen Schreibzugriff auf das Kurs-Repository. Für diesen Weg brauchst du [eingerichtetes Git](https://docs.github.com/en/get-started/git-basics/set-up-git) und eine funktionierende GitHub-Anmeldung für `git push`. [GitHub: Repository klonen](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) · [GitHub: Neues Repository erstellen](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).
3. GitHub Actions muss in **deinem** Repository erlaubt sein. Bei einem Fork prüfe zuerst den Tab **Actions**. Falls Workflows nicht laufen, kontrolliere die [Actions-Einstellungen](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).

Für den Klon-Weg kannst du die folgenden Befehle verwenden. Ersetze `KURS-OWNER`, `KURS-REPO`, `DEIN-NAME` und `DEIN-REPO` durch die tatsächlichen Namen:

```bash
git clone https://github.com/KURS-OWNER/KURS-REPO.git
cd KURS-REPO
git remote set-url origin https://github.com/DEIN-NAME/DEIN-REPO.git
git push -u origin main
```

Wenn du im Fork oder eigenen Repository arbeitest, reicht für die Workflow-Datei und die spätere Codekorrektur auch der GitHub-Browsereditor. Python auf deinem Rechner ist optional.

## Dateien in dieser Vorlage

```text
README.md                 diese Anleitung
requirements-dev.txt      Testwerkzeug pytest
shop/versand.py           fertiges Programm mit absichtlichem Fehler
tests/test_versand.py     fertige Tests
.gitignore                lokale Python-Dateien nicht einchecken
```

Es gibt **noch keine** Datei unter `.github/workflows/`. Die erstellst du selbst. Eine Workflow-Datei ist YAML; Einrückung mit Leerzeichen ist wichtig. Falls YAML neu für dich ist, hilft das [YAML-Tutorial mit Beispielen](https://www.yaml.info/learn/index.html). Die [GitHub-Workflow-Syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) erklärt die speziellen Schlüssel für Actions.

## Aufgabe

### 1. Vorbereiten und nachlesen

Lies [GitHub: Workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows) und [GitHub: Python bauen und testen](https://docs.github.com/en/actions/tutorials/build-and-test-code/python). Kläre diese Fragen, bevor du YAML schreibst:

- In welchem Verzeichnis muss eine Workflow-Datei liegen?
- Was lösen `push` und `pull_request` aus?
- Was ist der Unterschied zwischen Workflow, Job, Runner und Step?
- Wofür sind `actions/checkout` und `actions/setup-python` nötig?

Die Antworten findest du in der [Workflow-Syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), in den offiziellen Action-Repositories [checkout](https://github.com/actions/checkout) und [setup-python](https://github.com/actions/setup-python) sowie in den [GitHub-Ereignissen](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

Weitere wiederverwendbare Actions findest du im [GitHub Actions Marketplace](https://github.com/marketplace?type=actions). Prüfe bei einer Action Beschreibung, Herausgeber, benötigte Rechte und Dokumentation. Für diese Aufgabe reichen `checkout` und `setup-python`.

### 2. Deine Pipeline erstellen

Erstelle auf dem Branch `main` die Datei `.github/workflows/ci.yml`. Auf GitHub geht das über **Add file → Create new file**; gib den ganzen Pfad ein. Alternativ erstelle die Datei lokal und pushe sie.

Dein Workflow muss Folgendes tun:

1. Einen aussagekräftigen Namen bekommen.
2. Bei `push` auf `main` **und** bei `pull_request` mit Ziel `main` starten.
3. Dem eingebauten `GITHUB_TOKEN` nur `contents: read` geben.
4. Einen Job auf `ubuntu-latest` ausführen.
5. Den Repository-Code mit `actions/checkout` holen.
6. Python **3.13** mit `actions/setup-python` einrichten.
7. `python -m pip install -r requirements-dev.txt` ausführen.
8. Die Tests mit `python -m pytest -q` starten.

Die offiziellen Repositories zeigen `actions/checkout@v7` und `actions/setup-python@v7`. Verwende deren Major-Versionen oder prüfe die aktuellen Versionen direkt dort. Schreibe den Workflow anhand der Dokumentation selbst; hier steht absichtlich keine fertige YAML-Lösung. Für das Einrichten von Python verwende `with:` und `python-version: '3.13'`. Die beiden Befehle aus Punkt 7 und 8 stehen jeweils in einem `run:`-Step.

**Erwartung:** Nach dem Commit auf `main` öffnest du den Tab **Actions**, dann den neuesten Run, den Job und den Test-Step. Der Run soll **rot** sein. Das ist in diesem Projekt zunächst richtig: Die Pipeline hat einen vorhandenen Programmfehler gefunden. Notiere dir, welcher Test scheitert und welche beiden Werte verglichen werden.

### 3. Fehler beheben und Pull Request anlegen

Erstelle von `main` **in deinem eigenen Repository** einen Branch, zum Beispiel `update/shop`: Im Repository den Branch-Auswahlschalter öffnen, **View all branches → New branch** wählen und `main` als Ausgangspunkt angeben. [GitHub: Branch im Browser erstellen](https://docs.github.com/en/pull-requests/how-tos/commit-changes/managing-branches-within-your-repository).

Öffne auf diesem Branch `shop/versand.py`, vergleiche die Bedingung mit der Tabelle oben und korrigiere **nur den Programmfehler**. Ändere die Tests nicht. Committe die Änderung. Klicke danach auf **Compare & pull request** oder öffne **Pull requests → New pull request**, mit `base: main` und `compare: update/shop` **im selben Repository**. [GitHub: Pull Request erstellen](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).

**Erwartung:** Der `pull_request`-Run wird **grün**. Zeige im PR den Diff und den Check-Status. Falls der PR-Run nicht startet, kontrolliere Ziel-Branch, Dateipfad und `on:`-Abschnitt; siehe [GitHub: Workflow-Trigger prüfen](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows). Ergänze vor dem Merge die PR-Beschreibung aus Schritt 4.

### 4. Einen nachvollziehbaren Pull Request abgeben

Prüfe vor dem Abgeben den Tab **Files changed**: Enthält der PR nur die beabsichtigte Korrektur? Gib ihm einen kurzen Titel, der die Änderung beschreibt. Schreibe in die PR-Beschreibung:

1. **Ausgangslage:** Welches Verhalten war falsch? Verlinke den roten Run oder nenne den fehlgeschlagenen Test.
2. **Änderung:** Was hast du am Programm geändert und warum löst das den Fehler?
3. **Prüfung:** Verlinke den grünen PR-Run und nenne den ausgeführten Testbefehl.
4. **Umfang:** Bestätige, dass du die bestehenden Tests nicht verändert hast und keine weiteren Dateien zur Fehlerkorrektur nötig waren.

Eine andere Person soll aus Titel, Beschreibung, Diff und Checks verstehen können, **was** geändert wurde, **warum** und **wie** du es geprüft hast. Du kannst den PR mergen; der anschließende `push`-Run auf `main` soll ebenfalls grün sein. [GitHub: Änderungen im PR prüfen](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request).

## Erfolgskriterien

- Eine selbst erstellte `.github/workflows/ci.yml` liegt im Repository.
- Der erste Run auf `main` ist wegen des vorbereiteten Programmfehlers rot; der Fehler ist im Test-Log erkennbar.
- Ein Pull Request enthält die kleine Korrektur, eine nachvollziehbare Beschreibung und einen grünen Test-Run.
- Der Workflow verwendet `contents: read` und keine Secrets.
- Du kannst Trigger, Runner, Action, Step und Testbefehl am eigenen Workflow zeigen.

## Wenn etwas nicht funktioniert

| Beobachtung | Prüfe zuerst |
|---|---|
| Im Actions-Tab erscheint kein Run | Liegt die Datei exakt unter `.github/workflows/`? Wurde auf `main` gepusht? Ist Actions aktiviert? Ist `on:` korrekt eingerückt? |
| „Invalid workflow file“ | YAML-Einrückung, Doppelpunkte und Schreibweise von `jobs`, `runs-on`, `steps`, `uses`, `run`. Vergleiche mit der offiziellen Workflow-Syntax. |
| `ModuleNotFoundError: pytest` | Ist `python -m pip install -r requirements-dev.txt` vor dem Test-Step gelaufen? |
| `ModuleNotFoundError: shop` | Läuft der Befehl im Repository-Hauptverzeichnis und wurde `actions/checkout` ausgeführt? |
| Run ist schon vor der Korrektur grün | Prüfe, ob die Tests wirklich gestartet wurden und `tests/test_versand.py` noch unverändert ist. |
| PR-Run erscheint nicht | Ziel-Branch `main`, `pull_request`-Trigger, keine Merge-Konflikte; siehe GitHub-Doku zur Trigger-Fehlersuche. |

## Optional: lokal prüfen

Mit Python 3.13 kannst du das Projekt auch lokal testen. Auf Windows kann der Python-Befehl `py -3.13` statt `python` heißen.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Unter Windows PowerShell aktivierst du die Umgebung mit `.venv\Scripts\Activate.ps1`. Der erste Testlauf soll auch lokal rot sein. Die `.venv`-Dateien sind durch `.gitignore` ausgeschlossen. Für die eigentliche Aufgabe genügt der Run auf GitHub.

## Sicherheit und Quellen

Dieses Beispiel braucht **keine Secrets**. Trage keine Passwörter oder Tokens in Workflow-Dateien oder Logs ein. `permissions: contents: read` begrenzt den eingebauten Token auf Lesezugriff für Repository-Inhalte. Nutze für diese Übung das normale `pull_request`-Ereignis und keine privilegierten PR-Trigger. Ein grüner Run bedeutet nur, dass die definierten Tests erfolgreich waren.

- [GitHub: Workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows)
- [GitHub: Workflow-Syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [GitHub: Python bauen und testen](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [GitHub: `GITHUB_TOKEN`-Rechte](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token)
- [GitHub: Workflow-Runs untersuchen](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)
- [YAML-Tutorial](https://www.yaml.info/learn/index.html)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)