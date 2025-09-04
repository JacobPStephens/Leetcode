#include <map>
#include <string>
#include <iostream>

class Solution {
public:
    bool isAnagram(string s, string t) {
        
        std::map<char, int> sMap;
        std::map<char, int> tMap;

        std::cout<< "Size of s: " << s.size() << std::endl;

        if (s.size() != t.size()) {
            std::cout << "Sizes differ" << std::endl;
            return false;
        }

        for (int i = 0; i < s.size(); i++) {
            sMap[s[i]] += 1;
            tMap[t[i]] += 1;
            std::cout << s[i] << std::endl;
        }

        // std::cout<< "Size of sMap: " << sMap.size() << std::endl;
        // std::cout<< "Size of tMap: " << tMap.size() << std::endl;

        for (const auto& pair : sMap) {
            if (tMap.find(pair.first) == tMap.end()) {
                std::cout << pair.first << " not in second word";
                return false;
            }
            if (sMap[pair.first] != tMap[pair.first]) {
                std::cout << "count of " << pair.first << "differs in each word";
                return false;
            }
        }
        return true;
    }
};
