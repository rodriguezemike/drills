#include <iostream>
#include <stdlib>

template <class T>
class LinkedListNode{
	public:
		T value;
		Node *next;
		Node(T& value){
			this.value = value
			this.next = nullptr
		}
		~Node(){
			Node *tmp = this
			while(tmp != nullptr){
				tmp = this.next
				delete this
			}
		}
		
		//Might need to dereference all of these
		void append(T &value){

		}

		void add(T &value){

		}
		
		void insert(T &value){

		}

		void remove(T &value){

		}

		void reverse(){

		}

}
