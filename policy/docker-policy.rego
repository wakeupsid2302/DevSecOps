package docker.policy

deny[msg] {
    input.instruction == "USER"
    input.value == "root"
    msg = "Dockerfile must not use the root user"
}

deny[msg] {
    input.instruction == "ADD"
    msg = "Dockerfile must use COPY instead of ADD"
}
