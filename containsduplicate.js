 var containsDuplicate = function(nums) {
    for (let index = 0; index < nums.length; index++) {
      counter = 0;
      for (let index2 = 0; index2 < nums.length; index2++) {
        if (nums[index] === nums[index2]) {
          counter = counter +1
        }
      }
      if (counter > 1) {
        return true
      }
    }
    return false
};

console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2]));

// public boolean containsDuplicate3(int[] nums){
//   Arrays.sort(nums);
//   for (int i = 0; i < nums.length-1; i++) {
//       if(nums[i] == nums[i+1]){
//           return true;
//       }
//   }
//   return false;
// } faz um sort, ve se o proximo numero é igual ao ultimo