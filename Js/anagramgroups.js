function groupAnagrams(strs) {
      const map = new Map();

        for (let word of strs) {
            const sorted = word.split('').sort().join('');
                if (!map.has(sorted)) map.set(sorted, []);
                    map.get(sorted).push(word);
                      }

                        return Array.from(map.values());
                        }
