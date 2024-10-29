public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> dict = new Dictionary<int,int>();
        int diff=0;
        for(int i=0; i<nums.Length; i++)
        {
            diff = target- nums[i];
            if(dict.ContainsKey(diff))
            {
               return new int[]{i,dict[diff]};
            }
            else if(!dict.ContainsKey(nums[i]))
            {
              dict.Add(nums[i],i);
            }
        }
        return null;
    } 
}
    
# Time Complexity: O(n)
# Space Complexity: O(1)
