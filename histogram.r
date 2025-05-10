age_groups <- c(
  "0-4", "5-9", "10-14", "15-19", "20-24", "25-29",
  "30-34", "35-39", "40-44", "45-49", "50-54",
  "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+"
)

population <- c(
  11087, 11288, 11109, 10499, 10040, 9244,
  8184, 7233, 6539, 5607, 4972,
  4144, 3381, 2402, 1581, 934, 571, 389
)

barplot(
  population,
  names.arg = age_groups,
  col = "skyblue",
  border = "black",
  las = 2,           
  main = "Population by Age Group (2020)",
  xlab = "Age Group",
  ylab = "Population"
)
