function moveZeros(arr) {
      const nonZeros = arr.filter(x => x !== 0);
        const zeros = Array(arr.length - nonZeros.length).fill(0);
          return [...nonZeros, ...zeros];
          }
