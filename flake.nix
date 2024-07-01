{
  description = "A flake for the pywhis project";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
    in {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          python3
          python3Packages.pip
          python3Packages.setuptools
          python3Packages.wheel
          python3Packages.openai
        ];
      };

      packages.default = pkgs.python3Packages.buildPythonPackage {
        pname = "pywhis";
        version = "0.1.0";

        src = ./.;

        propagatedBuildInputs = with pkgs; [
          python3Packages.pip
          python3Packages.setuptools
          python3Packages.wheel
          python3Packages.openai
        ];
      };
    });
}
