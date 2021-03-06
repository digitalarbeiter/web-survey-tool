# -*- coding: utf8 -*-
#
# Umfrage Kiga 2014
#

JA = [
    u"ja"
]
JA_NEIN = [
    u"ja",
    u"eher ja",
    u"teilweise",
    u"eher nein",
    u"nein",
    u"weiß nicht",
]
GUT_SCHLECHT = [
    u"gut",
    u"eher gut",
    u"teilweise",
    u"eher schlecht",
    u"schlecht",
    u"weiß nicht",
]

def survey_factory():
    survey = {}
    survey["title"] = u"Elternbefragung 2014"
    survey["questions"] = []
    survey["questions"].append({
        "type": "free-comment",
        "title": u"Elternbefragung 2014",
        "toc": u"Zur Umfrage",
        "question": u"""
<p>
Liebe Eltern! </p>
<p>
Hier findet Ihr die diesjährige schriftliche Elternbefragung,
die der Elternbeirat zusammen mit dem Erzieherinnenteam erarbeitet hat. </p>
<p>
Ziel des Fragebogens ist es, Eure Zufriedenheit mit unserem Kindergarten
abzufragen und wichtige Impulse zu geben, ihn weiterzuentwickeln. Dafür 
ist es wichtig, Eure Meinung zu verschiedenen Bereichen des 
Kindergartenlebens wie Räumlichkeiten, Informationsfluss, Wohlbefinden 
der Eltern und der Kinder zu erfahren. Diese Fragen bilden den ersten 
Teil des Fragebogens. Im zweiten Teil gehen wir kurz auf aktuelle Themen
ein. Das sind diesmal Fragen rund um das Thema Austausch.</p>
<p>
Die Ergebnisse können die Zustände im Kindergarten positiv bestätigen oder 
aber auch dazu führen, Veränderungen zu erarbeiten und umzusetzen. Indem 
Ihr also die vorliegenden Fragen beantwortet, tragt Ihr dazu bei, dass wir 
die Rahmenbedingungen im Kindergarten zu unser aller Zufriedenheit 
gestalten können. Das kommt den Eltern, den Erzieherinnen und natürlich 
ganz besonders unseren Kindern zugute. </p>
<p>
Dieses Jahr geben für jede Familie nur noch einen Vote-Code für den
Fragebogen aus. Daher bitten wir alle Elternteile bzw. alle
Erziehungsberechtigten, den Fragebogen <b>gemeinsam</b> auszufüllen.
</p>
<p>
Bei Unklarheiten sprecht uns gerne an.
</p>
<p>
Selbstverständlich werdet Ihr über die Ergebnisse informiert. </p>
<p>
Die Teilnahme an der Befragung ist freiwillig. Die Auswertung erfolgt 
anonym. </p>
<p>
Bitte füllt Eure Fragebogen bis spätestens Sonntag, den 13. April
aus. </p>
<p>
Ein großes Dankeschön schon mal für Eure Unterstützung </p>
<p>
vom Elternbeirat: Lisa  Enkler und Elke Elsäßer </p>
<p>
und vom Team: Petra Welte </p>
            """,
        "subquestions": [],
        "comment": None,
        "answer": None,
    })
    survey["questions"].append({
        "type": "free-comment",
        "title": u"Anleitung und Hilfe",
        "toc": u"Anleitung",
        "question": u"""
<h2> Fragen </h2>
<p>
  Die Fragen - die komplette Frageliste einer Umfrage findet sich in der
  rechten Spalte - sind natürlich der Schwerpunkt der Umfrage. Es gibt
  verschiedene Fragetypen: bei manchen ist eine Mehrfachauswahl erlaubt,
  bei anderen nicht; meist ist ein Feld für Kommentare, Anregungen etc.
  vorgesehen.
</p>
<p>
  Unter jeder Frage gibt es zwei Knöpfe, "Weiter" und "Zwischenspeichern".
  Normalerweise, wenn man die Umfrage in einem Rutsch ausfüllt, ist
  Zwischenspeichern nicht notwendig, und erst ganz am Schluß, bei der
  Abgabe, wird man auf "Abschicken" clicken. Wenn man aber den Fragebogen
  nicht "am Stück" ausfüllen möchte, kann man jederzeit zwischenspeichern
  und morgen weitermachen.
</p>
<p>
  Der "Weiter"-Button führt zur nächsten Frage. Um zu früheren Fragen
  zurückzukehren, könnt Ihr die Fragen im Inhaltsverzeichnis in der
  rechten Spalte anclicken. Dabei geht nichts verloren, Ihr braucht nicht
  zwischenspeichern.
</p>
<h2> Stimmabgabe </h2>
<p>
  Sind alle Fragen beantwortet, werdet Ihr im letzten Punkt nach
  Eurem <b>Vote-Code</b> gefragt. Das ist die lange Zahl auf dem
  Umfrage-Zettel. Die sorgt dafür, daß jeder nur eine Stimme abgibt,
  und daß die Stimmabgabe trotzdem anonym ist - nämlich durch eine
  anonyme Vote-Code-Ausgabe.
</p>
<p>
  Wenn Ihr nach Eingabe und Abschicken des Vote-Codes <b>keine</b>
  "Vielen Dank für Deine Teilnahme"-Seite seht, war der Vote-Code
  falsch. Vermutlich vertippt... Probiert es nochmal, <i>Eure
  Eingaben wurden behalten</i>, Ihr müßt nicht nochmal alles eintippen,
  nur den Vote-Code auf der "Fertig"-Seite; Ihr könnt direkt wieder
  dortin springen.
</p>
<h2> Mehr Hilfe </h2>
<p>
  Falls es noch Fragen gibt, bitte per Mail an patrick.schemitz@web.de
</p>
            """,
        "subquestions": [
        ],
        "comment": None,
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Meine Kinder",
        "toc": u"Meine Kinder",
        "question": u"Ich habe ein Kind in der ...",
        "answer_type": "checkbox",
        "choices": JA,
        "subquestions": [
            u"Blumengruppe",
            u"Wiesengruppe",
            u"Baumgruppe"
        ],
        "comment": None,
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Die Gebäude des Kindergartens",
        "toc": u"Die Gebäude",
        "question": u"Wie beurteilst Du im Kindergarten St. Michael...",
        "answer_type": "radio",
        "choices": GUT_SCHLECHT,
        "subquestions": [
            u"... den Garderobenbereich",
            u"... die sonstigen räumlichen Angebote",
            u"... die Sauberkeit",
            u"... das sonstige Erscheinungsbild",
            u"... die Sicherheit",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Das Erzieherinnen-Team",
        "toc": u"Das Team",
        "question": u"Welchen Eindruck hast Du vom Erzieherinnen-Team?",
        "answer_type": "radio",
        "choices": GUT_SCHLECHT,
        "subquestions": [
            u"Welchen Eindruck hast Du vom Erzieherinnen-Team?",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Der Elternbeirat",
        "toc": u"Der EB",
        "question": u"Wie beurteilst Du die Arbeit des aktuellen Elternbeirates?",
        "answer_type": "radio",
        "choices": GUT_SCHLECHT,
        "subquestions": [
            u"Arbeit des aktuellen Elternbeirates",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Umgang mit Rückmeldungen",
        "toc": u"Rückmeldungen",
        "question": u"Wie ist der Umgang mit Rückmeldungen (d.h. Nachfragen, Lob, Kritik oder Beschwerden)?",
        "answer_type": "radio",
        "choices": GUT_SCHLECHT,
        "subquestions": [
            u"Erzieherinnen-Team",
            u"Elternbeirat",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Persönliches Engagement",
        "toc": u"Engagement",
        "question": u"Möchtest Du mit persönlichem Engagement Aktivitäten im Kindergarten unterstützen?",
        "answer_type": "checkbox",
        "choices": JA,
        "subquestions": [
            u"Hauswirtschaftlicher Bereich",
            u"Baulicher Bereich",
            u"Pädagogischer Bereich",
            u"Begleitung auf Exkursionen",
            u"Sonstiges (bitte unten angeben)",
        ],
        "comment": u"Sonstiges persönliches Engagement",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Der Informationsfluß",
        "toc": u"Informationsfluß",
        "question": u"Bist Du mit dem Informationsfluß zufrieden bezüglich...",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"... alltäglicher organisatorischer Belange?",
            u"... der allgemeinen pädagogischen Arbeit?",
            u"... Euer Kind betreffend?",
            u"... getroffener oder anstehender <b>Entscheidungen des Trägers</b> (z.B. den Umbau betreffend)?",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Welche Information auf welchem Weg?",
        "toc": u"Informationswege",
        "question": u"Auf welchem Wege möchtest Du informiert werden über...",
        "answer_type": "checkbox",
        "choices": [
            u"Einzelgespräche",
            u"Tür + Angel Gespräche",
            u"Infowand",
            u"Email",
        ],
        "subquestions": [
            u"Termine (Waldtage, Sport, Veranstaltungen etc)",
            u"Allgemeine Terminänderungen",
            u"Aktionen für eine Teilgruppe (Exkursionen, Kochtage, Projekte)",
            u"Einladungen vom Team (Elternabend, Elterntreff etc)",
            u"Einladungen von Eltern oder Elternbeirat (Ausflüge, Papa-Kind-Zelten, Stammtisch)",
            u"Infos aus der Kirchengemeinde (Gottesdienste, Feste etc)",
            u"Planung und Organisation von Veranstaltungen mit Listen (Helfer, Teilnehmer)",
            u"Adressen der Eltern",
            u"Externe Informationen (Schulamt, Gesundheitsamt etc)",
            u"Reflexion nach Aktionen (Dank an Eltern etc)",
            u"Information über den Entwicklungsstand des Kindes",
            u"Kurzinfos über das Kind (Unwohlsein, Geschehnisse)",
            u"Persönliche Terminabsprachen (Geburtstagsfeier, Schulranzen mitbringen etc)",
        ],
        "comment": None,
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Regeln und Rituale",
        "toc": u"Regeln und Rituale",
        "question": u"Bist Du mit den Regeln und Ritualen des Kindergartens vertraut (z. B. Essen, Geburtstage, Abholzeiten, Hofregeln)?",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"Bist Du mit den Regeln und Ritualen des Kindergartens vertraut?"
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Gemeinsame Unternehmungen",
        "toc": u"Unternehmungen",
        "question": u"Bist Du zufrieden mit den Festen und Ausflügen, die Kinder, Team und Eltern gemeinsam unternehmen?",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"Häufigkeit von Festen",
            u"Art der Feste",
            u"Häufigkeit von Ausflügen",
            u"Art der Ausflüge",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Wohlfühlen und Zufriedenheit",
        "toc": u"Wohlfühlen",
        "question": u"",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"Fühlt sich Dein Kind im Kindergarten wohl?",
            u"Fühlst Du Dich im Kindergarten wohl?",
            u"Konntest Du Kontakte zu anderen Eltern knüpfen?",
            u"Würdest Du den Kindergarten Freunden und Bekannten empfehlen?",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Gestaltung und Gewichtung der Angebote",
        "toc": u"Angebote",
        "question": u"Wie wünschest Du Dir die Gestaltung der verschiedenen Angebote im Kindergarten?",
        "answer_type": "radio",
        "choices": [
            u"mehr",
            u"gut so",
            u"weniger",
            u"egal",
            u"weiß nicht",
        ],
        "subquestions": [
            u"Basteln, Malen",
            u"Erzählen, Vorlesen",
            u"Experimentieren",
            u"Backen, Kochen",
            u"Religiöse Erziehung",
            u"Ruhe, Entspannung",
            u"Singen, Musizieren",
            u"Tanzen, Turnen",
            u"Spielen drinnen",
            u"Spielen draußen",
            u"Werken",
            u"Erkundungen im Ort",
            u"Exkursionen, Ausflüge",
            u"Spazieren gehen",
            u"Spielplatz besuchen",
            u"Wald entdecken",
            u"Werteerziehung",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })


    survey["questions"].append({
        "type": "yes-no",
        "title": u"Aktuelles: Elternabende",
        "toc": u"Aktelles: Elternabende",
        "question": u"Im diesjährigen aktuellen Teil geht es um Austausch bei den Punkten Elternabende, Austausch Eltern-Erzieher und Austausch zwischen Eltern.<p />",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"Bist Du zufrieden mit den Elternabenden?",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "free-comment",
        "title": u"Aktuelles: Themen Elternabende",
        "toc": u"Elternabend Themen",
        "question": u"Die Idee für den letzten Elternabend zum Thema Ernährung kam von Seiten der Eltern. Das Team wünscht sich (z. B. als Input für Diskussionen) weitere Ideen für thematische Elternabende. Zu welchen Themen würdest Du Dir weitere Elternabende wünschen? (Bitte mehrere Wünsche angeben)",
        "comment": u"",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Aktuelles: Austausch zwischen Eltern und Erzieherinnen",
        "toc": u"Austausch Erzieherinnen",
        "question": u"Bist Du zufrieden mit...",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"... den Entwicklungsgesprächen?",
            u"... den Elterngesprächen bei aktuellen Bedarf?",
            u"... den Tür und Angel Gesprächen – Kurzinfos über das Kind? (Unwohlsein, Geschehnisse)",
            u"... persönlichen Terminabsprachen? (Geburtstagsfeier, Schulranzen mitbringen etc.)",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Aktuelles: Austausch zwischen Eltern",
        "toc": u"Austausch Eltern",
        "question": u"",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"Hast du grundsätzlich Interesse, Dich auch ohne Kinder mit anderen Eltern zu treffen? (z. B. Elternstammtisch, Caférunde...)",
            u"Gibt es für Dich genug Möglichkeiten, sich mit anderen Eltern auszutauschen?",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Aktuelles: Austausch zwischen Eltern II",
        "toc": u"Austausch Eltern II",
        "question": u"",
        "answer_type": "radio",
        "choices": [ u"Monatlich", u"Pro Quartal", u"Halbjährlich", u"kein Interesse" ],
        "subquestions": [
            u"Falls du Interesse hast dich mit anderen Eltern zu treffen, wie oft würdest du bevorzugen?",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })
    survey["questions"].append({
        "type": "yes-no",
        "title": u"Aktuelles: Beteiligung an einmaligen Aktionen",
        "toc": u"Aktionsbeteiligung",
        "question": u"",
        "answer_type": "radio",
        "choices": [ u"Ja", u"Nein" ],
        "subquestions": [
            u"Wärst du unabhängig davon bereit, Dich an einmaligen Aktionen (z. B. Ausflug, kreative Projekte…) in Deiner Freizeit zu beteiligen?",
        ],
        "comment": u"Anmerkungen",
        "answer": None,
    })


    survey["questions"].append({
        "type": "free-comment",
        "title": u"Anmerkungen (positiv)",
        "toc": u"Positive Anmerkungen",
        "question": u"Was Du schon immer einmal <b>an Positivem</b> zum Thema Kindergarten St. Michael loswerden wolltest (z.B. zur Eingewöhnungsphase, Vorbereitung auf die Schule, Tagesablauf, Konzept, Erzieherinnen)",
        "comment": "",
        "answer": None,
    })
    survey["questions"].append({
        "type": "free-comment",
        "title": u"Anmerkungen (negativ)",
        "toc": u"Negative Anmerkungen",
        "question": u"Was Du schon immer einmal <b>an Negativem</b> zum Thema Kindergarten St. Michael loswerden wolltest (z.B. zur Eingewöhnungsphase, Vorbereitung auf die Schule, Tagesablauf, Konzept, Erzieherinnen)",
        "comment": "",
        "answer": None,
    })
    survey["questions"].append({
        "type": "free-comment",
        "title": u"Anmerkungen zum Fragebogen",
        "toc": u"Fragebogen",
        "question": u"Hast Du Anmerkungen zum Fragebogen selbst (fehlt z.B. etwas)?",
        "comment": "",
        "answer": None,
    })
    survey["questions"].append({
        "type": "votecode",
        "title": u"Fragebogen abgeben",
        "toc": u"Fertig",
        "question": u"Um den Umfragebogen abzugeben, bitte gib hier den <b>Vote-Code</b> ein. Der Vote-Code steht auf dem Stück Papier, daß Du zur Umfrage erhalten hast (das mit den Gummibärchen). Achtung: jeder Vote-Code kann genau einmal benutzt werden!",
        "comment": "",
        "answer": None,
    })
    return survey


if __name__ == "__main__":
    import sys
    import wst.survey_service
    service = wst.survey_service.SurveyService(
        host=("127.0.0.1", 8000),
        #host=("88.198.106.203", 8080),
        survey_factory=survey_factory,
        temp_dir="/tmp",
        vote_code_file="data/votecodes.json",
        submitted_survey_dir="/tmp/surveys",
    )
    if len(sys.argv) == 3 and sys.argv[1] == "--generate-votecodes":
        service.generate_votecodes(int(sys.argv[2]))
    elif len(sys.argv) == 3 and sys.argv[1] == "--evaluate":
        service.evaluate(sys.argv[2])
    elif len(sys.argv) == 2 and sys.argv[1] == "--print-votecodes":
        title = "Kindergarten St. Michael Elternumfrage 2014"
        url = "http://digitalarbeiter.de:8080/"
        service.print_votecodes(title, url)
    elif len(sys.argv) == 2 and sys.argv[1] == "--run":
        service.run()
    else:
        print sys.argv[0] + " --run     to start service"
        print sys.argv[0] + " --generate-votecodes 10     to generate 10 votecodes"
        print sys.argv[0] + " --print-votecodes     to print the votecodes"
        print sys.argv[0] + " --evaluate <targetdir>     to evaluate survey results into target"

