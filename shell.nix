let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  shellHook = ''
    exec fish
  '';
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.pandas
      python-pkgs.requests
      python-pkgs.panflute
    ]))
    pkgs.fish
    pkgs.git
    pkgs.nodePackages.mathjax
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
  ];
}
