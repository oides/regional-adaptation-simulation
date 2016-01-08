library(fBasics)

sink("analysis.out")

before = c(18,22,21,17,20,17,23,20,22,21)
after = c(16,20,14,21,20,18,13,15,17,21)

cat("\n##########################################\n")
cat("\n### START ANDERSON-DARLING BEFORE\n")
cat("\n##########################################\n")
adBeforeReturn = adTest(before)
adBeforeReturn

cat("\n##########################################\n")
cat("\n### START T-TEST\n")
cat("\n##########################################\n")
t.test(before, after)

sink()
