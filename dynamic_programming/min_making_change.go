package main

// You are given coins of different denominations and a total amount of
// money amount. Write a function to compute the fewest number of coins
// that you need to make up that amount. If that amount of money cannot
// be made up by any combination of the coins, return -1.
// https://leetcode.com/articles/coin-change/
func coinChange(coins []int, amount int) int {

	max := 100000
	dp := make([]int, amount+1)

	for i := 1; i <= amount; i++ {

		var coin_change_list []int
		for _, coin := range coins {
			remainder := i - coin
			if remainder >= 0 {
				coin_change_list = append(coin_change_list, dp[remainder])
			}
		}

		min := 100000
		for _, change := range coin_change_list {
			if change < min {
				min = change
			}
		}

		// +1 because coin_change_list only tracks how many coins
		// aside from current coin are needed
		dp[i] = 1 + min

	}

	if dp[len(dp)-1] < max {
		return dp[len(dp)-1]
	} else {
		return -1
	}

}
