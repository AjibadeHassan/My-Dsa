class Stack {
      constructor() {
          this.stack = [];
            }

              push(val) {
                  this.stack.push(val);
                    }

                      pop() {
                          return this.stack.pop();
                            }

                              peek() {
                                  return this.stack[this.stack.length - 1];
                                    }

                                      isEmpty() {
                                          return this.stack.length === 0;
                                            }
                                            }
