# Step 1: Generate a random number between 1 to 10 and store it in var1
var1 <- sample(1:10, 1)
cat("Generated number:", var1, "\n")

# Step 2: Generate a second number, display it, and add it to var1
repeat {
  var2 <- sample(1:10, 1)
  cat("Generated number:", var2, "\n")
  var1 <- var1 + var2
  
  # Step 3: Check conditions using IF statements
  if (var1 < 16) {
    cat("Var1 is below 16. Continuing...\n")
    next
  } else if (var1 >= 16 && var1 <= 21) {
    cat("Hold. The total is:", var1, "\n")
    break
  } else {
    cat("Busted. The total is:", var1, "\n")
    break
  }
}
