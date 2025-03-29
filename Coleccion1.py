# gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista

texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
texto_lst = texto.split("&")
texto_lst[0] = texto_lst[0].capitalize() + "..."
texto_lst[1] = "- " + texto_lst[1].split("-")[0].capitalize() + "-" + texto_lst[1].split("-")[1] + "."
texto_lst[2] = "- " + texto_lst[2].split("-")[0].capitalize() + "-" + texto_lst[2].split("-")[1] + "."
texto_lst[3] = "- " + texto_lst[3].capitalize() + "."
print("\n".join(texto_lst))