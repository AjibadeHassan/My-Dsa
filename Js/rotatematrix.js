function rotate(matrix) {
      const n = matrix.length;

        // Transpose
          for (let i = 0; i < n; i++) {
              for (let j = i; j < n; j++) {
                    [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
                        }
                          }

                            // Reverse each row
                              for (let row of matrix) {
                                  row.reverse();
                                    }
                                    }
