#include <iostream>
#include <stdlib>


bool test_parens(char paren_string[]){
	int balance = 0;
	int array_size = sizeof(paren_string)/sizeof(paren_string[0])
	for(int i = 0; i < array_size; ++i){
		if (paren_string[i] == "("){
			balance += 1;
		}
		else if (parent_string[i] == ")"){
			balance -= 1;
		}
		else{
			continue;
		}
	}
	return (balance == 0);
}


bool test_unique(char test_string[]){
	int array_size = sizeof(test_string)/sizeof(test_string[0]);
	for(int i = 0; i < array_size; ++i){
		for (int j = i+1; j < array_size; ++i){
			if (test_string[j] == *test_string[i]){
				return false;
			}
		}
	}
	return true;
}

int create_count_dict(char test_string[]){
	std::map <char, int> count_me;
	for(int i = 0; i < std::strlen(test_string); ++i){
		if(count_me.count(test_string[i]) == 0){
			count_me[test_string[i]] = 1;
		}
		else{
			count_me[test_string[i]] = 0;
		}
	}
	return count_me;
}

char[] get_new_char_array(int size){
	char *p;
	p = new char[size*2];
	return p;
}

char[] copy_array(char *new_array, char *old_array){
	for(int i = 0; std::strlen(old_array); ++i){
		new_array[i] = old_array[i];
	}
	delete *old_array;
	return new_array;
}

char[] urlify(char test_string[]){
	char *new_string;
	char[] replacement = "%20";
	int new_string_index = 0;
	new_string = get_new_char_array(std::strlen(test_string));
	for(int i = 0; std::strlen(test_string); ++i){
		if(test_string[i] == " "){
			for(int j = 0; j < std::strlen(replacement); ++i){
				if j == std::strlen(new_string){
					char* tmp_array = get_new_char_array(std::strlen(new_string));
					new_string = copy_array(tmp_array, new_string);	
				}
				new_string[i+j] = replacement[j];
				new_string_index += 1;
			}
		}
		else{
			new_string[new_string_index] = test_string[i];
			new_string_index += 1;
		}
	}
	return new_string; 
}
	
int main(){
	char test_parent[] = "()(())))(())";
	test_parens(test_paraent)
	return 0
}
