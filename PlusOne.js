// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

const plusOne = (array = []) => {
  for (let i = array.length - 1; i >= 0; i--) {
    if (array[i] < 9) {
      array[i]++;
      return array;
    }
    array[i] = 0;
  }

  return [1, ...array];
};

let digits = [9, 9, 9];

console.log(plusOne(digits));
