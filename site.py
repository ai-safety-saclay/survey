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
    fig.savefig(buf, format="svg")
    svg_data = buf.getvalue().decode("utf-8")
    buf.close()
    doc.asis(svg_data)


def render_choices(choices):
    with tag("ul", style="list-style: none"):
        for c in choices:
            with tag("li"):
                with tag("input", type="checkbox", disabled=True):
                    pass
                text(c)

# How can I prevent a html checkbox to be checked ?
def render_question(i):
    q = questions[i]
    with tag("h3"):
        text(q["question"])

    if "subquestions" in q:
        with tag("ul"):
            for s in q["subquestions"]:
                with tag("li"):
                    with tag("h4"):
                        text(s)
                render_choices(q["choices"])

    else:
        render_choices(q["choices"])


def pie_chart(df, title, labels=None):
    fig, _ = plt.subplots()
    count = df.value_counts().sort_index()/N
    if labels==None:
        labels = count.index
    plt.pie(count.values, labels=labels, autopct=lambda x:f"{x:1.1f} %")
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
            text('Survey Results')
    with tag('body'):
        with tag('h1'):
            text('Sondage sûreté IA')

        render_question(0)
        capabilities = ["Minecraft", "Olympiades", "meme", "musique"]
        columns = data[[1,2,3,4]].fillna(0).astype(int)
        values = columns.mean(axis=0)
        bar_chart(capabilities, values, 'Tâches résolues')

        render_question(1)
        pie_chart(data[5], 'Elo chatGPT')

        render_question(2)
        labels = ["Taille / performances", "Refus", "Raisonnement", "Connaissances"]
        columns = data[[6,7,8,9]].fillna(0).astype(int)
        values = columns.mean(axis=0)
        bar_chart(labels, values, 'Compréhension des LLM')

        render_question(3)
        pie_chart(data[10], "RLHF")

        render_question(4)
        fig, ax = plt.subplots()
        count = data[11].astype(float).value_counts().sort_index()/N
        bar_chart(count.index, count.values, 'Timeline openAI')

        render_question(5)
        count = data[12].astype(float).value_counts().sort_index()/N
        bar_chart(count.index, count.values, 'avis des Experts')

        render_question(6)
        count = data[13].value_counts().sort_index()/N
        bar_chart(count.index, count.values, 'Probablitité de catastrophe')

        render_question(7)
        count = data[14].value_counts().sort_index()/N
        bar_chart(count.index, count.values, 'Cyber')
        count = data[15].value_counts().sort_index()/N
        bar_chart(count.index, count.values, 'Crash')
        count = data[16].value_counts().sort_index()/N
        bar_chart(count.index, count.values, 'Perte contrôle')
        count = data[17].value_counts().sort_index()/N
        bar_chart(count.index, count.values, 'Automatisation')

        render_question(8)
        pie_chart(data[18], "ChatGPT", labels=["non", "oui"])

        render_question(9)
        pie_chart(data[19], "API Publique", labels=["non", "oui"])

        render_question(10)
        pie_chart(data[20], "Sûreté IA Juridique", labels=["non", "oui"])

        render_question(11)
        pie_chart(data[21], "Sûreté IA recherche", labels=["non", "oui"])

        render_question(12)
        pie_chart(data[22], "Ralentir création", labels=["non", "oui"])

        render_question(13)
        pie_chart(data[23], "Ralentir déploiement", labels=["non", "oui"])

        render_question(14)
        pie_chart(data[24], "EU AI Act", labels=["non", "oui"])
        pie_chart(data[25], "Séoul", labels=["non", "oui"])
        pie_chart(data[26], "PauseAI", labels=["non", "oui"])
        pie_chart(data[27], "CeSIA", labels=["non", "oui"])

        render_question(15)
        pie_chart(data[28], "Cours", labels=["non", "oui"])

with open("index.html", "w") as file:
    html_content = doc.getvalue()
    file.write(html_content)
