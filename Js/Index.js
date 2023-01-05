// const map = new Map([['a', 1], ['b', 2]])
// map.set('c', 3)
// map.delete('a')
// map.clear()
// // console.log(map.classification('b'))

// for(const [key, value] of map){
//   console.log(`${key} : ${value}`)
// }


// STACK IMPLEMENTATION


// class Stack {
//   constructor(){
//     this.items = []
//   }

//   push(el){
//     this.items.push(el)
//   }

//   pop(){
//     return this.items.pop()
//   }

//   peek(){
//     return this.items[this.items.length - 1]
//   }

//   isEmpty(){
//     return this.items.length === 0;
//   }

//   size(){
//     return this.items.length
//   }

//   print(){
//     console.log(this.items.toString())
//   }
// }

// const stack = new Stack
// console.log(stack.isEmpty())
// stack.push('a new push');
// console.log(stack.peek())
// stack.push('code maniac!')
// console.log(stack.size());(
// console.log(stack.print())


// QUEUE IMPLEMENTATION

// class Queue {
//   constructor(){
//     this.items = []
//   }

//   enqueue(el){
//     this.items.push(el)
//   }

//   dequeue(){
//     return this.items.shift()
//   }

//   peek(){
//     return this.items[this.items.length - 1]
//   }

//   isEmpty(){
//     return this.items.length === 0;
//   }

//   size(){
//     return this.items.length
//   }

//   print(){
//     console.log(this.items.toString())
//   }
// }

// const queue = new Queue
// console.log(queue.isEmpty())
// queue.enqueue('a new push');
// console.log(queue.peek())
// queue.enqueue('code maniac!')
// console.log(queue.size());
// console.log(queue.print())
// console.log(queue.peek())


//  CIRCULAR QUEUE IMPLEMENTATION


class circularQueue {
    constructor(capacity){
      this.items = new Array(capacity)
      this.capacity = capacity
      this.currentLength = 0
      this.rear = -1
      this.front = -1
    }
  
    isFull(){
     return this.currentLength === this.capacity
    }
  
    isEmpty(){
      return this.currentLength == 0
    }
  enqueue(el){
  if(!this.isFull()) {
    this.currentLength += 1
    this.rear = (this.rear + 1) % this.capacity;
    this.items[this.rear] = el;
    if(this.front === -1){
      this.front = this.rear
    } else {
     return null
    }
  }
   
  }
  
    peek(){
      return this.items[this.front]
    }
    dequeue(){
      if(this.isEmpty()){
        return null
      }
      const item = this.items[this.front]
      this.currentLength -= 1
      this.items[this.front] === null
      this.front = (this.front + 1) % this.capacity
      if(this.isEmpty()){
        this.rear = -1
        this.front = -1
      }
      return item
    }
  
    print(){
      if(this.isEmpty()){
        return null
      }
      else {
       let i
        let string = ''
        for(i = this.front; i !== this.rear; i = (i + 1) % this.capacity ){
          string += this.items[i] +" "
          // console.log(i) 
        }
        string += this.items[i]
        // console.log(i)
      return string
      }
    }
  }
  
  const Circle = new circularQueue(4)
  
  // console.log(Circle.isEmpty())
  Circle.enqueue(10)
  Circle.enqueue(20)
  Circle.enqueue(30)
  Circle.enqueue(40)
  
  console.log(Circle.peek(), Circle.isEmpty())
  console.log('this is ',Circle.print())
  
  
  