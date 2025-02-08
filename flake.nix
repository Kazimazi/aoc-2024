{
  description = "stuff";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    flake-parts.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" ];
      perSystem = { pkgs, ... }: {
        devShells = with pkgs; let
          haskell = [ ghc haskell-language-server ];
          python = [ python3 ];
        in
        {
          default = mkShell {
            nativeBuildInputs = haskell ++ python;
          };

          haskell = mkShell {
            nativeBuildInputs = haskell;
          };

          python = mkShell {
            nativeBuildInputs = python;
          };
        };
      };
    };
}
