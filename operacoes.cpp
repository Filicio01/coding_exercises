#include <iostream>
#include <locale>

using namespace std;

int main() {
    setlocale(LC_ALL, "portuguese");

    float num1, num2, resultado;
    char operador;

    cout << "Digite o primeiro valor: ";
    cin >> num1;
    cout << "Digite o operador (+,-,*,/): ";
    cin >> operador;
    cout << "Digite o segundo valor: ";
    cin >> num2;

    switch (operador) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            resultado = num1 / num2;
            break;
        default:
            cout << "Operador inválido" << endl;
            return 1;
    }

    cout << num1 << " " << operador << " " << num2 << " = " << resultado << endl;

    return 0;
}

