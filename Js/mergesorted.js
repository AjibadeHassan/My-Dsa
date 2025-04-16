function mergeSortedArrays(arr1, arr2) {
      let i = 0, j = 0, result = [];

        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) result.push(arr1[i++]);
                else result.push(arr2[j++]);
                  }

                    return [...result, ...arr1.slice(i), ...arr2.slice(j)];
                    }
