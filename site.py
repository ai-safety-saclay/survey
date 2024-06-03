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


def pie(values, labels):
    plt.pie(values, labels=labels, autopct=lambda x:f"{x:1.1f} %")


doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('title'):
            text('Survey Results')
    with tag('body'):
        with tag('h1'):
            text('Sondage sûreté IA')

        render_question(0)
        fig, ax = plt.subplots()
        capabilities = ["Minecraft", "Olympiades", "meme", "musique"]
        columns = data[[1,2,3,4]].fillna(0).astype(int)
        values = columns.mean(axis=0)
        plt.bar(capabilities, values)
        plt.title('Tâches résolues')
        plt.close(fig)
        plot_to_img(fig)

        render_question(1)
        fig, ax = plt.subplots()
        count = data[5].astype(float).value_counts().sort_index()/N
        pie(count.values, labels=count.index)
        plt.title('Elo de chatGPT')
        plt.close(fig)
        plot_to_img(fig)

        render_question(2)
        fig, ax = plt.subplots()
        labels = ["Taille / performances", "Refus", "Raisonnement", "Connaissances"]
        columns = data[[6,7,8,9]].fillna(0).astype(int)
        values = columns.mean(axis=0)
        plt.bar(labels, values)
        plt.title('Compréhension des LLM')
        plt.close(fig)
        plot_to_img(fig)

        render_question(3)
        fig, ax = plt.subplots()
        count = data[10].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('RLHF')
        plt.close(fig)
        plot_to_img(fig)


        render_question(4)
        fig, ax = plt.subplots()
        count = data[11].astype(float).value_counts().sort_index()/N
        plt.bar(count.index, count.values)
        plt.title('Timeline openAI')
        plt.close(fig)
        plot_to_img(fig)

        render_question(5)
        fig, ax = plt.subplots()
        count = data[12].astype(float).value_counts().sort_index()/N
        plt.bar(count.index, count.values)
        plt.title('avis des Experts')
        plt.close(fig)
        plot_to_img(fig)

        render_question(6)
        fig, ax = plt.subplots()
        count = data[13].value_counts().sort_index()/N
        plt.bar(count.index, count.values)
        plt.title('Risques')
        plt.close(fig)
        plot_to_img(fig)


        render_question(7)
        fig, ax = plt.subplots()
        count = data[14].value_counts().sort_index()/N
        plt.bar(count.index, count.values)
        plt.title('Cyber')
        plt.close(fig)
        plot_to_img(fig)

        fig, ax = plt.subplots()
        count = data[15].value_counts().sort_index()/N
        plt.bar(count.index, count.values)
        plt.title('Crash')
        plt.close(fig)
        plot_to_img(fig)

        fig, ax = plt.subplots()
        count = data[16].value_counts().sort_index()/N
        plt.bar(count.index, count.values)
        plt.title('Perte contrôle')
        plt.close(fig)
        plot_to_img(fig)

        fig, ax = plt.subplots()
        count = data[17].value_counts().sort_index()/N
        plt.bar(count.index, count.values)
        plt.title('Automatisation')
        plt.close(fig)
        plot_to_img(fig)

        render_question(8)
        fig, ax = plt.subplots()
        count = data[18].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('ChatGPT')
        plt.close(fig)
        plot_to_img(fig)

        render_question(9)
        fig, ax = plt.subplots()
        count = data[19].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('API GPT4')
        plt.close(fig)
        plot_to_img(fig)

        render_question(10)
        fig, ax = plt.subplots()
        count = data[20].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('Sûreté IA juridique')
        plt.close(fig)
        plot_to_img(fig)

        render_question(11)
        fig, ax = plt.subplots()
        count = data[21].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('Sûreté IA recherche')
        plt.close(fig)
        plot_to_img(fig)

        render_question(12)
        fig, ax = plt.subplots()
        count = data[22].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('ralentir création')
        plt.close(fig)
        plot_to_img(fig)

        render_question(13)
        fig, ax = plt.subplots()
        count = data[23].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('ralentir déploiement')
        plt.close(fig)
        plot_to_img(fig)


        render_question(14)
        fig, ax = plt.subplots()
        count = data[24].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('EU AI Act')
        plt.close(fig)
        plot_to_img(fig)

        fig, ax = plt.subplots()
        count = data[25].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('Séoul')
        plt.close(fig)
        plot_to_img(fig)
        
        fig, ax = plt.subplots()
        count = data[26].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('PauseAI')
        plt.close(fig)
        plot_to_img(fig)

        fig, ax = plt.subplots()
        count = data[27].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('CeSIA')
        plt.close(fig)
        plot_to_img(fig)

        render_question(15)
        fig, ax = plt.subplots()
        count = data[28].value_counts().sort_index()/N
        pie(count.values, labels=["non", "oui"])
        plt.title('Cours')
        plt.close(fig)
        plot_to_img(fig)

with open("index.html", "w") as file:
    html_content = doc.getvalue()
    file.write(html_content)

