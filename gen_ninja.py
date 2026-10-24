#!/usr/bin/env python3
"""leopard-base 数据包：目录骨架 + initrc/paths/profile（无二进制）。"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT  = ROOT / "out"

# 纯数据包：只有 data 文件，无 install 二进制
PKG = {
    "pkgname": "leopard-base",
    "pkgver":  "1.0_1",
    "arch":    "x86_64",
    "desc":    "Leopard base system",
    "deps":    "",
    "data": [
        ("data/initrc",  "system/etc/leopard/initrc"),
        ("data/paths",   "system/etc/leopard/paths"),
        ("data/profile", "system/etc/leopard/profile"),
        ("data/fstab",   "system/etc/leopard/fstab"),
    ],
}


def esc(p):
    return str(p).replace("$", "$$").replace(":", "$:").replace(" ", "$ ")


def main():
    out  = OUT / f"{PKG['pkgname']}-{PKG['pkgver']}.{PKG['arch']}.xbps"
    args = f"-A {PKG['arch']} -n {PKG['pkgname']}-{PKG['pkgver']} -s \"{PKG['desc']}\""
    if PKG.get("deps"):
        args += f" -D \"{PKG['deps']}\""

    files = [(s, d) for s, d in PKG["data"]]

    cmd = "rm -rf .pkg"
    for src, dst in files:
        cmd += f" && mkdir -p .pkg/$$(dirname {dst}) && cp {src} .pkg/{dst}"
    cmd += f" && cd out && xbps-create {args} ../.pkg"

    L = ["# leopard-base 数据包（无二进制，只有配置文件）", "ninja_required_version = 1.10"]
    L += ["rule package", f"  command = {cmd}", ""]
    L += [f"build {esc(out)}: package {' '.join(esc(s) for s, _ in files)}"]
    L += [f"build pack: phony {esc(out)}"]
    L += ["default pack"]
    L += ["rule clean", "  command = rm -rf out .pkg", "build clean: clean"]

    (ROOT / "build.ninja").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("已生成 build.ninja（leopard-base）。用法：ninja pack")


if __name__ == "__main__":
    main()
