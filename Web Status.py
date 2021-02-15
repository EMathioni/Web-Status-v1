import requests

print("Bem vindo ao Web Status v1 :)")
print("GitHub: https://github.com/EMathioni")
print("------------")
def request_func(lista_url):
  try:
    request = requests.get(lista_url)
    if request.status_code >= 200 or request.status_code <= 299:
      print(f"{lista_url} --> Site online")
    elif request.status_code == 403:
      print("Sem autorização")
    elif request.status_code == 404:
      print("Pagina nao encontrada")
  except:
    print(f"Erro ao verificar site ({lista_url})")

def start ():
  print("Digite o site a consultar:")
  guarda_urls = input("> ").lower().split(",")
  for site in guarda_urls:
    if "." not in site:
      print(f"'{site}' não é uma URL válida, por favor, insira uma URL válida.")
      break
    elif "https" in site:
      site = site.replace("https://", " ")
    if "http://" not in site:
      site = f"http://{site.strip()}"
      request_func(site)
  repeat()      

def repeat():
  print("Deseja verificar outros sites? s/n")
  continuar = input("> ")
  if continuar == "s":
    start()
  elif continuar == "n":
    print("Programa encerrado!")
    print("Obrigado por usar o Web Status v1")
    print("GitHub: https://github.com/EMathioni")
    return
  else:
    print(f"Opção invalida ({continuar})\n\n")
    repeat()
start()