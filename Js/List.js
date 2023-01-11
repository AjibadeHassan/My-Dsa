class Node {
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class linkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    isEmpty(){
        return this.size === 0;
    }

    getSize(){
        return this.size
    }

    prepend(value){
        const node = new Node(value)
        if(this.isEmpty()){
            this.head = node;
        } else {
            node.next = this.head;
            this.head = node
        }
        this.size++
    }

    print(){
        if(this.isEmpty()){
            console.log('this is an empty list')
        } else {
            let curr = this.head;
            let listValues = '';
            while(curr) {
                listValues += `${curr.value} `
                curr = curr.next
            }
            console.log(listValues)
        }
    }
}


const List = new linkedList()

List.prepend(10)
List.prepend(20)
List.prepend(30)

console.log(List.head, List.getSize(), List.isEmpty())
List.print()