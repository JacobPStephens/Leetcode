public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> numsSet = new HashSet<int>(nums);

        return !(nums.Length == numsSet.Count);
    }
}
