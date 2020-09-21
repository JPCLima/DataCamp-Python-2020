# Sorting rows
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(
    ['region', 'family_members'], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Subsetting columns
# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals', 'state']]

# Print the head of the result
print(ind_state.head())

# Subsetting rows
# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (
    homelessness['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)

# Subsetting rows by categorical variables
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)
