#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
  public:
    int lengthOfLongestSubstring(string s)
    {
        if (s.size() <= 1)
            return s.size();

        int max_ = 0;
        int i = 0, j = 1;
        for (j = 1; j < s.size(); j++)
        {
            string sub = s.substr(i, j-i);
            int pos = sub.find(s[j]);
            if (pos != sub.npos)
                i += pos + 1;
            else if (1 + j - i > max_)
                max_ = 1 + j - i;
        }
        return max_;
    }
};

int main()
{
    Solution solution;
    cout << solution.lengthOfLongestSubstring("abcabcbb") << endl;
    system("pause");
    return 0;
}