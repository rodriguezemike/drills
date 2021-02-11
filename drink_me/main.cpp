#include <iostream>
#include <stdlib.h>

int main(){
	std::string drinks[5] = {"black coffee", 
						"black tea", 
						"flat white", 
						"quad shot",
						"chai tea latte"};

	std::srand(time(nullptr));
	int drink_size = sizeof(drinks)/sizeof(drinks[0]);
	int selector = rand() % drink_size;

	std::cout << drink_size << "\n";
	std::cout << selector	<< "\n";
	std::cout << "Drink Me : " << drinks[selector] << "\n"; 
	
	return 0;
}
