package docker.policy

deny[msg] {
    input.instruction == "USER"
    input.value == "root"
    msg = "Avoid using root user in Dockerfile."
}

deny[msg] {
    input.instruction == "ADD"
    msg = "Use COPY instead of ADD for better security."
}

any_non_root_user_set {
    input.instruction == "USER"
    input.value != "root"
}

deny[msg] {
    input.instruction == "USER"
    input.value == "root"
    not any_non_root_user_set
    msg = "Set a non-root user before using it in the Dockerfile."
}
