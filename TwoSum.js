// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

let nums = [2, 7, 11, 15],
  target = 9;

const TwoSum = (nums = [], target = 9) => {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];

    if (map.has(complement)) {
      return [i, map.get(complement)];
    }

    map.set(nums[i], i);
  }
};

console.log(TwoSum(nums, target));
