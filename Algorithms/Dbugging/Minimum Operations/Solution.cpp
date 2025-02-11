#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <algorithm> 
#include <vector> 
#include <cmath> 
#include <iostream> 
#include <map> 
using namespace std; 

// DP table to store the minimum operations for each subset of colors
int dp[110][1<<3];

// Function to find the minimum operations to ensure all colors are represented
int min_operations(vector<int> red, vector<int> green, vector<int> blue) {
    int n = (int)red.size(), i, j;

    // Initialize DP table with a large value
    for (i = 0; i <= n; i++) {
        for (j = 0; j <= 7; j++) {
            dp[i][j] = 1<<30;
        }
    }

    // Base case: No operations needed for an empty set
    dp[0][0] = 0;

    // Iterate over each index in the given color vectors
    for (i = 0; i < n; i++){
        for (j = 0; j <= 7; j++){
            // Transition by picking the color set at index i
            dp[i + 1][j | 1] = min(dp[i + 1][j | 1], dp[i][j] + green[i] + blue[i]); // Pick red
            dp[i + 1][j | 2] = min(dp[i + 1][j | 2], dp[i][j] + red[i] + blue[i]);   // Pick green
            dp[i + 1][j | 4] = min(dp[i + 1][j | 4], dp[i][j] + red[i] + green[i]);  // Pick blue
        }
    }

    // Determine which colors are present in the input
    j = 0;
    for (i = 0; i < n; i++){
        if (green[i]) j |= 1;
        if (red[i]) j |= 2;
        if (blue[i]) j |= 4;
    }

    // If no valid solution is found, return -1
    if (dp[n][j] >= (1<<30))
        dp[n][j] = -1;

    return dp[n][j];
}

int main() {
    int n, r, g, b;
    cin >> n;
    vector<int> red, blue, green;

    // Read input values for red, green, and blue arrays
    for(int i = 0; i < n; i++){
        cin >> r >> g >> b;
        red.push_back(r);
        green.push_back(g);
        blue.push_back(b);
    }

    // Output the minimum operations required
    cout << min_operations(red, green, blue) << "\n";
    return 0;
}