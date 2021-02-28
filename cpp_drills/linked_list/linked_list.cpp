#include <iostream>
#include <stdlib>

template <class T>
class LinkedListNode{
	public:
		T value;
		Node *next;
}		
LinkedListNode::Node(T& value){
	this.value = value;
	this.next = nullptr;

}
LinkedListNode::~Node(){
	Node *tmp = this;
	while(tmp != nullptr){
		tmp = this->next;
		delete this;
	}
}

//Might need to dereference all of these
void LinkedListNode::append(T &value){
	Node *tmp = this;
	while(tmp->next != nullptr){
		tmp = tmp->next;
	}
	Node *n = new Node(value);
	tmp->next = n;
}

Node* LinkedListNode::push(T &value){
	Node *n = new Node(value);
	n->next = this;
	return n;
}

Node* LinkedListNode::insert(T &value, int position){
	if(position == 0){
		return push(value);
	}
	else{
		Node *tmp = this;
		int index = 0;
		while(index < position){
			if(tmp->next != nullptr){
				tmp = tmp->next;
			}
			index++;
		}
		Node *n = new Node(value);
		tmp->next = n;
		return this;
	}
}

void LinkedListNode::remove(T &value){
	Node *tmp = this;
	while(tmp != nullptr){
		if(tmp->next->value == value){
			Node* toRemove = tmp->next;
			tmp->next = toRemove->next;
			toRemove->next = nullptr;
			delete toRemove;
			break;
		}
		else{
			tmp = tmp->next;
		}
	}
}

void LinkedLisitNode::reverse(){
	Node *tmp = this;
	Node *newNext = nullptr;
	while(tmp.next!= nullptr){
		Node *n = new Node(tmp->value);
		n->next = newNext;
		newNext = n;
		tmp = tmp->next; 	
	}
	this->value = tmp.value;
	this->next = newHead;
}
