var decompressRLElist = function(nums) {
  let newArray = []
    for (let index = 0; index < nums.length; index+= 2) {
      for (let index2 = 0; index2 < nums[index]; index2++) {
        newArray.push(nums[index+1]);
      }
    }
    return newArray;
};

console.log(decompressRLElist([1, 1, 2 ,2]));
