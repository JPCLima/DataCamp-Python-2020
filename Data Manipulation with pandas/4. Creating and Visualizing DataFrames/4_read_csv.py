# CSV to DataFrame
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby(
    "airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / \
    airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)


# DataFrame to CSV
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values(
    "bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")
