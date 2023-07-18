#include <iostream>
#include <locale>
using namespace std;

int main() {
	float vM;
	setlocale(LC_ALL, "portuguese");
	cout << "Digite a Metragem: ";
	cin >> vM;
	
	float vD = vM * 10;
	cout<< "Este é o valor em Decimentros: "<<vD<< endl;
	
	float vC = vM * 100;
	cout<< "Este é o valor em Centímentros: "<<vC<< endl;
	
	float vP = vM * 39.37;
	cout<< "Este é o valor em Polegadas: "<<vP<< endl;
	
	float vMM = vM * 1000;
	cout<< "Este é o valor em Milímentros: "<<vMM<< endl;	
}
