

import { resolve } from 'path';

// Specify the filename you want to obtain the path for
const filename = 'List.js';

// Resolve the file path
const filePath = resolve(__dirname, filename);

console.log('File Path:', filePath);






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

    append(value){
        const node = new Node(value)
        if(this.isEmpty()){
            this.head = node;
        } else {
            let curr = this.head
            while(curr.next){
                curr = curr.next
            }
            curr.next = node
        }
        this.size ++;
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

List.append(10)
List.append(20)
List.append(30)

console.log(List.head, List.getSize(), List.isEmpty())
List.print()