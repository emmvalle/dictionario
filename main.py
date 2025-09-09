meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "IRL":"algo que pasa en la vida real",
            "UFO":"un objetoto indefinido o disco volador"}
    

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
If word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("esta palabra no existe")
