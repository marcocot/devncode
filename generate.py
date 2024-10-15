from openai import OpenAI
from dotenv import load_dotenv
import os
import argparse
from slugify import slugify
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_hugo_post(prompt: str, title: str):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": "Sei uno sviluppatore che ha un blog di articoli tecnici su vari argomenti. Scrivi articoli per un pubblico medio-avanzato utilizando un linguaggio informale. Ogni articolo deve avere una introduzione e degli esempi pratici. Ogni articolo deve essere in formato Markdown. Ogni articolo deve contenere anche le tue considerazioni riguardo il topic. Ogni articolo deve essere almeno 3 pagine. Ottimizza l'articolo per il SEO. Quando possibile, aggiungi sempre i link alla documentazione ufficiale. Quando serve, crea dei diagrammi in Mermaid o PlantUML per chiarire meglio.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=4096,
        n=1,
        stop=None,
        temperature=0.6,
    )

    content = response.choices[0].message.content.strip()

    title_slugified = slugify(title)
    date_time = datetime.now().strftime("%Y-%m-%d")

    # Prepara il front matter per Hugo in formato markdown
    front_matter = f"""---
title: "{title}"
date: {date_time}
draft: false
tags: []
path: '/posts/test/{title_slugified}'
---
"""

    # Combina front matter e contenuto generato
    post_content = front_matter + "\n" + content

    # Salva il contenuto come file markdown
    folder_name = os.path.join("content/post/", date_time + "-" + title_slugified)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(f"{folder_name}/index.md", "w") as f:
        f.write(post_content)


if __name__ == "__main__":
    # Configurazione di argparse per gestire gli argomenti
    parser = argparse.ArgumentParser(
        description="Genera un post per Hugo utilizzando OpenAI"
    )
    parser.add_argument("prompt", type=str, help="Le linee guida dell'articolo")
    parser.add_argument("title", type=str, help="Il titolo dell'articolo")

    args = parser.parse_args()

    # Chiama la funzione per generare il post
    generate_hugo_post(args.prompt, args.title)
