# We use the nixos build image as a base
FROM nixos/nix:2.23.0

COPY shell.nix .

# We setup the environment according to what is written 
# in the shell.nix file
RUN nix-env -f shell.nix -i -A buildInputs

# The entrypoint of the container is the shell
ENTRYPOINT ["nix-shell"]

