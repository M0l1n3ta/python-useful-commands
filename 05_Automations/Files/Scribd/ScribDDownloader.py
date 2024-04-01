import scribd_dl

#https://es.scribd.com/doc/20154009/Tecnologias-ASP-NET-4-0-saltando-desde-la-version-2-0
#https://es.scribd.com/embeds/20154009/content
with scribd_dl.ScribdDL() as session:
    session.download('https://es.scribd.com/doc/20154009/Tecnologias-ASP-NET-4-0-saltando-desde-la-version-2-0', pages='1-3')
    for title in session.doc_titles:
        print(title)