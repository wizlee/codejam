#include <iostream> // includes cin to read from stdin and cout to write to stdout
using namespace std; // since cin and cout are both in namespace std, this saves some text

int main() {
    return 0;
}

/// <summary>
/// Boilerplate code for non-interactive problem
/// </summary>
int _template_non_interactive() {
    int t, n, m; // t is num_test_cases
    cin >> t; // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> n >> m; // read n and then m.
        cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
    return 0;
}

#include <string>

/// <summary>
/// Boilerplate code for interactive problem.
/// The sample problem is a classic problem of guessing a number from a given range.
/// https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/0000000000000523#problem
/// </summary>
int _template_interactive() {
    int num_test_cases;
    std::cin >> num_test_cases;
    for (int i = 0; i < num_test_cases; ++i) {
        int lo, hi;
        std::cin >> lo >> hi;
        int num_tries;
        std::cin >> num_tries;
        int head = lo + 1, tail = hi;
        while (true) {
            int m = (head + tail) / 2;
            std::cout << m << std::endl;
            std::string s;
            std::cin >> s;
            if (s == "CORRECT") break;
            if (s == "TOO_SMALL")
                head = m + 1;
            else
                tail = m - 1;
        }
    }
    return 0;
}
