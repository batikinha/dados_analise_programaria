#parte1

preco_cenoura = 4.5
preco_oleo = 12
preco_fermento = 15
preco_leite = 5
preco_acucar = 6

def soma_ingredientes (tem_acucar, tem_leite, tem_fermento, tem_oleo, tem_cenoura):
    total_compra = 0
    if tem_cenoura:
        total_compra = total_compra + preco_cenoura
    if tem_oleo:
        total_compra = total_compra + preco_oleo
    if tem_fermento:
        total_compra = total_compra + preco_fermento
    if tem_leite:
        total_compra = total_compra + preco_leite
    if tem_acucar:
        total_compra = total_compra + preco_acucar
    return = total_compra

total = soma_ingredientes (True, True, True, True, True, True)
print (total)

#parte 2

if __name__ == "__main__":
    terminal_tem_cenoura = sys.argv[1] == "Sim"
    terminal_tem_acucar = sys.argv[2] == "Sim"
    terminal_tem_ovos = sys.argv[3] == "Sim"
    terminal_tem_oleo = sys.argv[4] == "Sim"
    terminal_tem_fermento = sys.argv[5] == "Sim"
    terminal_tem_leite = sys.argv[6] == "Sim"

    total = soma_ingredientes(terminal_tem_cenoura, terminal_tem_acucar,
                               terminal_tem_ovos, terminal_tem_oleo,
                               terminal_tem_fermento, terminal_tem_leite)

    print("Total dos ingredientes: ", total)