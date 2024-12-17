package docker.policy

# Deny usage of root user
deny[msg] {
    input.instruction == "USER"
    input.value == "root"
    msg = "Dockerfile must not use the root user. Use a non-root user instead."
}

# Deny usage of ADD
deny[msg] {
    input.instruction == "ADD"
    input.value == "http ."
    msg = "Dockerfile must use COPY instead of ADD for improved security."
}

# Deny if no non-root USER is set
deny[msg] {
    not any_non_root_user_set
    msg = "Dockerfile must define a non-root USER for better security."
}

any_non_root_user_set {
    input.instruction == "USER"
    input.value != "root"
}