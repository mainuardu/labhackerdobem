print("Em que ano vc naceu?")
nascimento=input()
nascimento=int(nascimento)

print("Em que ano vc quer saber a idade")
anoFuturo=input()
anoFuturo=int(anoFuturo)

idade=anoFuturo-nascimento

if idade < 120:
    print("No ano",anoFuturo,"vc terá",idade,"anos")
else:
    print("Acho que vc não vai viver até os",idade,"anos :(")
