#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>

int sol(int len) {
  std::stringstream buffer;
  buffer << std::ifstream("input.txt").rdbuf();
  std::string seq = buffer.str();

  for (int i = 0; i < seq.size(); ++i) {
    std::unordered_set<char> set;
    std::string marker = seq.substr(i, len);
    std::for_each(marker.begin(), marker.end(),
                  [&set](char c) -> void { set.insert(c); });
    if (set.size() == len)
      return i + len;
  }

  return 0;
}

int main() {
  std::cout << sol(4) << std::endl;
  std::cout << sol(14) << std::endl;
}
