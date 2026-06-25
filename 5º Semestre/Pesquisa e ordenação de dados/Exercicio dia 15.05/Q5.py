# Sistema de Recomendação de Playlists

def intersecao_playlists(playlist1, playlist2):
    set2 = set(playlist2)
    resultado = []

    for musica in playlist1:
        if musica in set2 and musica not in resultado:
            resultado.append(musica)

    return resultado

def musicas_unicas(playlist1, playlist2):
    set1 = set(playlist1)
    set2 = set(playlist2)

    resultado = []

    for musica in playlist1:
        if musica not in set2:
            resultado.append(musica)

    for musica in playlist2:
        if musica not in set1:
            resultado.append(musica)

    return resultado

usuario1 = ["Imagine", "Hey Jude", "Bohemian Rhapsody", "Billie Jean"]
usuario2 = ["Billie Jean", "Imagine", "Thriller", "Beat It"]

print(intersecao_playlists(usuario1, usuario2))

print(musicas_unicas(usuario1, usuario2))