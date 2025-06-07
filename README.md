# test1diff --git a/README.md b/README.md
index e6f6b35146143114e85ef7f9e40463aab19de5ca..44e8911b90ec9bf2f350a331ddf437ae9b3d17e2 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,28 @@
-# test1
+# test1
+
+This repository provides a simple calculator module with basic arithmetic
+operations. A small command line interface is included.
+
+## Usage
+
+Run the calculator from the command line by specifying an operation and two
+numbers:
+
+```bash
+python calculator.py add 1 2
+```
+
+Available operations are:
+
+- `add` - addition
+- `sub` - subtraction
+- `mul` - multiplication
+- `div` - division
+
+## Running tests
+
+The project uses `unittest`. Run the tests with:
+
+```bash
+python -m unittest discover -s tests
+```
