//linked_list.h

template <class T>
class LinkedListNode {
	public:
		Node();	
		Node(Node &n)
		~Node();
		void append(T &value);
		Node* push(T &value);
		Node* insert(T &value, int position);
		void remove(T &value);
		void reverse();
}
