print("Bienvenido al Diccionario")

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado"
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
  print(meme_dict[word])    
  i = input("Preciona enter para salir...")
else:
  print("Esa palabra no esta en el diccionario")   
  i = input("Preciona enter para salir...")
  
