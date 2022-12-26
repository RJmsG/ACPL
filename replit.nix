{ pkgs }: {
	deps = [
		pkgs.run
  pkgs.clang_12
		pkgs.ccls
		pkgs.gdb
		pkgs.gnumake
	];
}