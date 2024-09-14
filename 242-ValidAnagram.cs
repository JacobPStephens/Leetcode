// Jacob Stephens - September 12, 2024
// https://leetcode.com/problems/valid-anagram/
public class Solution {
    public bool IsAnagram(string s, string t) {
        
        if (s.Length != t.Length) {
            return false;
        }

        Dictionary<char, int> s_dict = new Dictionary<char, int>();
        Dictionary<char, int> t_dict = new Dictionary<char, int>();

        // Add (ch: count) to dictionaries
        for (int i = 0; i < s.Length; i++) {
            // Add key to dictionary if doesn't exist yet
            if (!s_dict.ContainsKey(s[i])) {
                s_dict[s[i]] = 0;
            }
            if (!t_dict.ContainsKey(t[i])) {
                t_dict[t[i]] = 0;
            }
            // Increment counts by 1
            s_dict[s[i]] += 1;
            t_dict[t[i]] += 1;
            
        } 

        // Next, compare the two dictionaries
        foreach (KeyValuePair<char, int> entry in s_dict) {
            
            // If t_dict doesn't have key or the counts don't match, return false
            if (!t_dict.ContainsKey(entry.Key) || (entry.Value != t_dict[entry.Key])) {
                return false;
            }
        }
        
        // If there is no difference found, return true
        return true;

    }
}
