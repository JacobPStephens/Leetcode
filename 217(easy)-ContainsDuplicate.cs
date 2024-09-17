// Jacob Stephens - September 12, 2024
// https://leetcode.com/problems/contains-duplicate/description/
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> numsSet = new HashSet<int>(nums);

        return !(nums.Length == numsSet.Count);
    }
}
