{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
    name = "transducer-exercices-shell";
    buildInputs = [ (import ./default.nix { inherit pkgs; }) ];
}
