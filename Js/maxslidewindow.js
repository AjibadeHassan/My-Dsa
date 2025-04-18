function maxSlidingWindow(nums, k) {
      const deque = [], result = [];

        for (let i = 0; i < nums.length; i++) {
            while (deque.length && deque[0] <= i - k) deque.shift();
                while (deque.length && nums[deque[deque.length - 1]] < nums[i]) deque.pop();
                    deque.push(i);
                        if (i >= k - 1) result.push(nums[deque[0]]);
                          }

                            return result;
                            }
