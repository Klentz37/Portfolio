# Prompting user to enter their full name
full_name <- readline(prompt = "Enter your full name: ")

# Splitting the full name into first name and last name
name_parts <- strsplit(full_name, " ")[[1]]

# Reversing the order of the name parts
reversed_name <- paste(rev(name_parts), collapse = " ")

# Displaying the result
cat("Swapped name:", reversed_name, "\n")

