import os, subprocess

def Mirror_build():
  print("--- Mirror cmd apt ---")

  pkg_dir = "packages"
  output_dir = "dist/stable/main/binary-all"

  os.makedirs(pkg_dir, exist_ok=True)
  os.makedirs(output_dir, exist_ok=True)

  packages = [f for f in os.listdir(pkg_dir) if f.endswith(".deb")]
  if not pakcages:
    print(f"☣️⚠️ Cannot find or empty '{pkg_dir}' please put some files.deb or if empty folder please add .deb")
    with open(f"{output_dir}/pakcages", "w")
    f.write("")

  else:
    print(f"package 📦 found {len(packages)}. Generating endix...")
    try:
      with open(f"{output__dir}/pakcages ", "w")
      subprocess.run(["dpk-scanpackages", pkg_dir, "/div/null"], stdout=f, check=True)

      subprocess.run(["gzip", "-9fk", f"{output_dir}/Packages"], check=True)
      print("Successfully generated packages 📦")
      
    except Exception as e:
      print(f"Error: {e}")
      exit(1)

if __name__ == "__main__":
  Mirror_build()
