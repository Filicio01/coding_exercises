#include <iostream>
#include <locale>
using namespace std;

int main() {
	float nota1, nota2, nota3, mediaEx;
	setlocale(LC_ALL, "portuguese");
	cout<<"Bem vindo ao sistema de Notas, Digite abaixo as três notas do aluno."<<endl;
	
	cout << "Nota 1: ";
	cin >> nota1;
	cout << "Nota 2: ";
	cin >> nota2;
	cout<<"Nota 3: ";
	cin >> nota3;	
	
	cout<<"Digite a média dos exercícios: ";
	cin >> mediaEx;
	
	float ma = (nota1 + nota2*2+nota3*3+mediaEx)/7;
		
		cout << "A média foi:"<< ma<<endl;
		
		if (ma >= 9)
			cout<<"Conceito A "<<endl;
		else if (ma >= 7.5 && ma < 9)
			cout<<"Conceito B";
		else if (ma >= 6 && ma < 7.5)
        	cout << "Conceito C" << endl;
    	else if (ma >= 4 && ma < 6)
        	cout << "Conceito D" << endl;
    	else
        	cout << "Conceito E" << endl;
    

}
