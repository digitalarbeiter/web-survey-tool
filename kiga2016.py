# -*- coding: utf8 -*-
#
# Umfrage Kiga 2015
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
    survey["title"] = u"Elternbefragung 2015"
    survey["questions"] = []
    survey["questions"].append({
        "type": "text-only",
        "title": u"Elternbefragung 2015",
        "toc": u"Zur Umfrage",
        "question": u"""
<p>
Liebe Eltern! </p>
<p>
Hier findet Ihr die diesjährige schriftliche Elternbefragung,
die der Elternbeirat zusammen mit dem Erzieherinnenteam erarbeitet hat. </p>
<p>
Ziel des Fragebogens ist es, Eure Zufriedenheit mit unserem Kindergarten
abzufragen und wichtige Impulse zu geben, ihn weiterzuentwickeln. 
Auch dieses Jahr fragen wir wieder nach der Zufriedenheit mit den
Angeboten, Informationsfluss, Organisation und Unternehmungen. </p>
<p>
Die Ergebnisse können die Zustände im Kindergarten positiv bestätigen oder 
aber auch dazu führen, Veränderungen zu erarbeiten und umzusetzen. Indem 
Ihr also die vorliegenden Fragen beantwortet, tragt Ihr dazu bei, dass wir 
die Rahmenbedingungen im Kindergarten zu unser aller Zufriedenheit 
gestalten können. Das kommt den Eltern, den Erzieherinnen und natürlich 
ganz besonders unseren Kindern zugute. </p>
<p>
Bitte nehmt Euch Zeit für die Anmerkungen, da diese uns nochmal ein
genaueres Bild geben. </p>
<p>
Jede Familie bekommt nur einen Vote-Code, wir bitten deshalb jeden Elternteil
 bzw. alle Erziehungsberechtigten einen Fragebogen <b>gemeinsam</b> auszufüllen.
 Nehmt den Fragebogen als Anlass euch gemeinsam hinzusetzen und über den 
 Kindergarten ins Gespräch zu kommen und nutzt die Eingabefelder für eigene Bemerkungen. 
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
Bitte füllt Eure Fragebogen bis spätestens Sonntag, den 12. Juni
aus. </p>
<p>
Ein großes Dankeschön schon mal für Eure Unterstützung </p>
<p>
vom Elternbeirat: Lisa Enkler und Isabelle Kretzschmar  </p>
<p>
und vom Team: Petra Welte </p>
            """,
        "subquestions": [],
        "comment": None,
        "answer": None,
    })
    survey["questions"].append({
        "type": "text-only",
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
  Falls es noch Fragen gibt, bitte per Mail an Boas@Enkler.OnMicrosoft.com
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
            u"... den Eingangsbereich",
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
            u"Informationsfluss des aktuellen Elternbeirates",
            u"Ansprechbarkeit des aktuellen Elternbeirates",
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
        "question": u"Um ein Gefühl für Eure Vorstellungen zu bekommen, würden wir gerne wissen, welche Themen Ihr für die Kinder als wichtig anseht. Sagt uns dabei bitte auch, aus welchem Grund, z. B. \"großes Interesse\" oder \"Stärke\". Nutzt dazu das Kommentarfeld.",
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
        "comment": u"Gründe, Ergänzungen, Anmerkungen:",
        "answer": None,
    })
  survey["questions"].append({
        "type": "text-only",
        "title": u"Aktueller Teil",
        "toc": u"Zum aktuellen Teil",
        "question": u"""
<p>Im Aktuellen Teil der Umfrage geht es dieses Jahr um das "Elterncafe"</p></br>

<p>In der Adventszeit 2015 hat uns das Kiga-Team mit dem "Adventsstübchen" eine tolle Möglichkeit
gegeben, uns zum Austausch und Zusammensein zu treffen. Dies fand so grossen Anklang das die
Frage war: Wie können wir das fortsetzen/weiterführen? So entstand die Idee mit dem Elterncafe.
Da unsere Kinder das Projektzimmer benötigen, können wir es nicht mehr für das Elterncafe nutzen. Deshalb haben wir Alternativen gesucht.</p>

            """,
        "subquestions": [],
        "comment": None,
        "answer": None,
    })
	    survey["questions"].append({
        "type": "yes-no",
        "title": u"Elterncafe",
        "toc": u"Teilname",
        "question": u"Habt ihr schon mal am Elterncafe teilgenommen.",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"Habt ihr schon mal am Elterncafe teilgenommen.?"
        ],
        "comment": u"Was waren für euch Gründen teilzunehmen?",
        "answer": None,
    })
	        survey["questions"].append({
        "type": "yes-no",
        "title": u"Elterncafe",
        "toc": u"Nichtteilnahme",
        "question": u"Was waren die Gründe,wenn Ihr nicht teilgenommen habt",
        "answer_type": "radio",
        "choices": JA_NEIN,
        "subquestions": [
            u"Kein Interesse",
            u"Keine Zeit",
            u"Tag und Uhrzeit ungünstig?"
        ],
        "comment": u"Sonstiges",
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
        title = "Kindergarten St. Michael Elternumfrage 2015"
        url = "http://digitalarbeiter.de:8080/"
        service.print_votecodes(title, url)
    elif len(sys.argv) == 2 and sys.argv[1] == "--run":
        service.run()
    else:
        print sys.argv[0] + " --run     to start service"
        print sys.argv[0] + " --generate-votecodes 10     to generate 10 votecodes"
        print sys.argv[0] + " --print-votecodes     to print the votecodes"
        print sys.argv[0] + " --evaluate <targetdir>     to evaluate survey results into target"

