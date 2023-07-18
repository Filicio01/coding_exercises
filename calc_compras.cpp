#include <iostream>
#include <locale>

using namespace std;

int main() {
    setlocale(LC_ALL, "portuguese");

    float tot, valP;
    cout << "Digite o total gasto pelo cliente: R$";
    cin >> tot;

    cout << "\nOpções de pagamento: \n";
    cout << "1 - À vista com 10% de desconto\n";
    cout << "2 - Em duas vezes (preço da etiqueta)\n";
    cout << "3 - De 3 até 10 vezes com 3% de juros (somente para compras acima de R$ 100,00)\n";
    cout << "Digite a opção desejada: ";
    int opcao;
    cin >> opcao;

    switch(opcao) {
        case 1:
            valP = tot - (tot * 0.1);
            cout << "\nValor total com desconto: R$" << valP << endl;
            break;
        case 2:
            valP = tot / 2;
            cout << "\nValor das duas parcelas: R$" << valP << endl;
            break;
        case 3:
            if (tot > 100) {
                cout << "\nDigite a quantidade de parcelas (entre 3 e 10): ";
                int parcelas;
                cin >> parcelas;
                if (parcelas >= 3 && parcelas <= 10) {
                    valP = (tot * 1.03) / parcelas;
                    cout << "\nValor das parcelas: R$" << valP << endl;
                } else {
                    cout << "\nOpção inválida." << endl;
                }
            } else {
                cout << "\nEsta opção está disponível apenas para compras acima de R$ 100,00." << endl;
            }
            break;
        default:
            cout << "\nOpção inválida." << endl;
            break;
    }

    return 0;
}

