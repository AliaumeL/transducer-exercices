{ pkgs ? import <nixpkgs> {} }:
pkgs.buildEnv {
  name = "transducer-exercices";
  paths = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas
      python-pkgs.requests
      python-pkgs.panflute
      python-pkgs.icalendar
      python-pkgs.dateparser
    ]))
    pkgs.fish
    pkgs.git
    pkgs.pandoc
    pkgs.gnumake
    pkgs.texliveFull
    pkgs.inkscape
    pkgs.git
    pkgs.bash
    pkgs.entr
    pkgs.websocat
    pkgs.gnutar
    pkgs.zip
    pkgs.dosis
    pkgs.stork
    pkgs.nodejs
    pkgs.coreutils
  ];
}
