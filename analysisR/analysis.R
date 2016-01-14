library(fBasics)
library(lawstat)
library(MASS)

sink("analysis.out")

LEVELS = 2
LEVELS_SIZE = 10

# Exemplo dieta
#controlOff = c(635, 704, 662, 560, 603, 745, 698, 575, 633, 669)
#controlOn = c(640, 712, 681, 558, 610, 740, 707, 585, 635, 682)

# Exemplo maconha
#controlOff = c(16,20,14,21,20,18,13,15,17,21)
#controlOn = c(18,22,21,17,20,17,23,20,22,21)

# Exemplo load CSV
controlOff = scan('reports/outputControlOff.csv')
controlOn = scan('reports/outputControlOn.csv')

cat("\n##########################################\n")
cat("\n### START ANDERSON-DARLING CONTROL OFF\n")
cat("\n##########################################\n")
adControlOffReturn = adTest(controlOff)
adControlOffReturn

cat("\n##########################################\n")
cat("\n### START ANDERSON-DARLING CONTROL ON\n")
cat("\n##########################################\n")
adControlOnReturn = adTest(controlOn)
adControlOnReturn

cat("\n##########################################\n")
cat("\n### START LEVENE\n")
cat("\n##########################################\n")
controlOnOffCombined = c(controlOff, controlOn)
gender=gl(LEVELS, LEVELS_SIZE)
factor=factor(gender)
levene.test(controlOnOffCombined, factor, location="median")

cat("\n##########################################\n")
cat("\n### START T-TEST\n")
cat("\n##########################################\n")
t.test(controlOff, controlOn, alternative = "less")

cat("\n##########################################\n")
cat("\n### START WILCOXON\n")
cat("\n##########################################\n")
wilcox.test(controlOff, controlOn, paired=TRUE, alternative = "less")

sink()
