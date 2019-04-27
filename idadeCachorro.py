print("Em que ano vc naceu?")
nascimento=input()
nascimento=int(nascimento)

print("Em que ano vc quer saber a idade")
anoFuturo=input()
anoFuturo=int(anoFuturo)

idadeHumano=anoFuturo-nascimento
idadeCachorro=idadeHumano*7

print("No ano",anoFuturo,"vc terá",idadeHumano,"anos como humano")
print("No ano",anoFuturo,"vc terá",idadeCachorro,"anos como cachorro")
