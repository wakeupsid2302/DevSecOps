package docker.policy

# Deny usage of root user in Dockerfile
deny[msg] {
    input.instruction == "USER"
    input.value == "root"
    msg = "Avoid using root user in Dockerfile."
}

# Deny usage of ADD instruction
deny[msg] {
    input.instruction == "ADD"
    msg = "Use COPY instead of ADD for better security."
}

# Allow only non-root users
any_non_root_user_set {
    input.instruction == "USER"
    input.value != "root"
}

# Rule to ensure there is a non-root user defined before using it
deny[msg] {
    input.instruction == "USER"
    input.value == "root"
    not any_non_root_user_set
    msg = "Set a non-root user before using it in the Dockerfile."
}
