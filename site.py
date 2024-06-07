from yattag import Doc
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import yaml

with open("questions/v1.yml") as file:
    questions = yaml.safe_load(file)


data : pd.DataFrame = pd.read_csv("results/telecom_paris.csv", header=None)
data = data.drop(index=[0,1,2])
N = len(data)

doc, tag, text = Doc().tagtext()

def plot_to_img(fig):
    buf = BytesIO()
    fig.savefig(buf, format="svg", transparent=True)
    svg_data = buf.getvalue().decode("utf-8")
    buf.close()
    doc.asis(svg_data)

def render_spacing():
    with tag("hr"):
        pass

def render_choices(choices, expected_answers=None):
    with tag("ul", style="list-style: none"):
        for i, c in enumerate(choices):
            with tag("li"):
                if expected_answers and expected_answers[i]:
                    with tag("input", type="checkbox", checked=True, disabled=True):
                        pass
                else:
                    with tag("input", type="checkbox", disabled=True):
                        pass
                text(c)


def render_question(i):
    q = questions[i]
    with tag("h2"):
        text(q["question"])

    if "subquestions" in q:
        with tag("ul"):
            for s in q["subquestions"]:
                with tag("li"):
                    with tag("h4"):
                        text(s)

    else:
        render_choices(q["choices"], q.get("expected"))


def buckets(series: pd.Series | pd.DataFrame, count_na=True):
    if count_na:
        stats = series.value_counts(normalize=True, dropna=False).sort_index()
        index = [x if pd.notna(x) else "sans réponse" for x in stats.index]
        return index, stats.values
    else:
        stats = series.value_counts(normalize=True).sort_index()
        return stats.index, stats.values


# How do I rename a Nan in the index of a pandas series ?
def pie_chart(series: pd.DataFrame| pd.Series, title, labels=None):
    fig, _ = plt.subplots()
    auto_labels, values = buckets(series)
    if labels==None:
        labels = auto_labels
    else:
        labels.append("sans réponse")
    plt.pie(values, labels=labels, autopct=lambda x:f"{x:1.1f} %")
    plt.title(title)
    plt.close(fig)
    plot_to_img(fig)


def bar_chart(labels, values, title):
    fig, _ = plt.subplots()
    plt.bar(labels, values)
    plt.title(title)
    plt.close(fig)
    plot_to_img(fig)


doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Sondage sûreté IA')
        with tag("link", href="./style.css", type="text/css", rel="stylesheet"):
            pass


    with tag('body'):
        with tag('h1'):
            text('Sondage sûreté IA')
        with tag("div", klass="intro"):
            with tag("p"):
                text("En mai 2024, nous avons fait passé aux étudiants de Télécom Paris un sondage sur la sûreté de l'IA, et en voici les résultats.")
            with tag("p"):
                text("Pour les questions de connaissance où une bonne réponse était attendue, la (ou les) bonnes réponses sont indiquées en gris.")
        with tag("a", href="https://github.com/ai-safety-saclay/survey"):
            text("plus d'information")

        render_question(0)
        capabilities = ["Minecraft", "Olympiades", "meme", "musique"]
        columns = data[[1,2,3,4]].fillna(0).astype(float)
        values = columns.mean(axis=0)
        bar_chart(capabilities, values, 'Tâches résolues')
        render_spacing()

        render_question(1)
        pie_chart(data[5], 'Elo chatGPT')
        render_spacing()

        render_question(2)
        labels = ["Taille / performances", "Refus", "Raisonnement", "Connaissances"]
        columns = data[[6,7,8,9]].fillna(0).astype(float)
        values = columns.mean(axis=0)
        bar_chart(labels, values, 'Compréhension des LLM')
        render_spacing()

        render_question(3)
        pie_chart(data[10], "RLHF", labels=["non", "oui"])
        render_spacing()

        render_question(4)
        fig, ax = plt.subplots()
        index, values = buckets(data[11].astype(float), count_na=False)
        bar_chart(index, values, 'Timeline openAI')
        render_spacing()

        render_question(5)
        index, values = buckets(data[12].astype(float), count_na=False)
        bar_chart(index, values, 'avis des Experts')
        render_spacing()

        render_question(6)
        index, values = buckets(data[13], count_na=False)
        bar_chart(index, values, 'Probablitité de catastrophe')
        render_spacing()

        render_question(7)
        index, values = buckets(data[14].astype(float), count_na=False)
        bar_chart(index, values, 'Cyber')
        index, values = buckets(data[15].astype(float), count_na=False)
        bar_chart(index, values, 'Crash')
        index, values = buckets(data[16].astype(float), count_na=False)
        bar_chart(index, values, 'Perte contrôle')
        index, values = buckets(data[17].astype(float), count_na=False)
        bar_chart(index, values, 'Automatisation')
        render_spacing()

        render_question(8)
        pie_chart(data[18], "ChatGPT", labels=["non", "oui"])
        render_spacing()

        render_question(9)
        pie_chart(data[19], "API Publique", labels=["non", "oui"])
        render_spacing()

        render_question(10)
        render_question(11)
        pie_chart(data[20], "Sûreté IA Juridique", labels=["non", "oui"])
        pie_chart(data[21], "Sûreté IA recherche", labels=["non", "oui"])
        render_spacing()

        render_question(12)
        render_question(13)
        pie_chart(data[22], "Ralentir création", labels=["non", "oui"])
        pie_chart(data[23], "Ralentir déploiement", labels=["non", "oui"])
        render_spacing()

        render_question(14)
        pie_chart(data[24], "EU AI Act", labels=["non", "oui"])
        pie_chart(data[25], "Séoul", labels=["non", "oui"])
        pie_chart(data[26], "PauseAI", labels=["non", "oui"])
        pie_chart(data[27], "CeSIA", labels=["non", "oui"])
        render_spacing()

        render_question(15)
        pie_chart(data[28], "Cours", labels=["non", "oui"])
        render_spacing()

with open("index.html", "w") as file:
    html_content = doc.getvalue()
    file.write(html_content)
