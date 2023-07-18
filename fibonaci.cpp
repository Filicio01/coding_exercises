#include<iostream>

 
 using namespace std;

 int fib(int n)
	 {
 	if(n ==1 || n == 2 ){
 		
		 return 1;
 		
	 	
	 } else {
	 
	  
	  	return fib(n - 2) + fib (n-1);	
	 
	 }
 	}
		 	 
	 
int main(){
	int n;
	int o = 1;


	cout << "Enter with a number: ";
	cin >> n;	
	cout << fib(n);
	
	
	return (0);
}

 	

