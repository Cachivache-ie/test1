diff --git a//dev/null b/calculator.py
index 0000000000000000000000000000000000000000..ff383709bc4a37651dc6cd466736b9c31bec431e 100644
--- a//dev/null
+++ b/calculator.py
@@ -0,0 +1,55 @@
+"""Simple calculator module."""
+
+from __future__ import annotations
+
+import argparse
+from typing import Callable
+
+
+def add(a: float, b: float) -> float:
+    """Return the sum of a and b."""
+    return a + b
+
+
+def subtract(a: float, b: float) -> float:
+    """Return the difference of a and b."""
+    return a - b
+
+
+def multiply(a: float, b: float) -> float:
+    """Return the product of a and b."""
+    return a * b
+
+
+def divide(a: float, b: float) -> float:
+    """Return the division of a by b."""
+    if b == 0:
+        raise ZeroDivisionError("Cannot divide by zero")
+    return a / b
+
+
+OPERATIONS: dict[str, Callable[[float, float], float]] = {
+    "add": add,
+    "sub": subtract,
+    "mul": multiply,
+    "div": divide,
+}
+
+
+def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
+    parser = argparse.ArgumentParser(description="Simple calculator")
+    parser.add_argument("operation", choices=OPERATIONS.keys(), help="Operation to perform")
+    parser.add_argument("a", type=float, help="First operand")
+    parser.add_argument("b", type=float, help="Second operand")
+    return parser.parse_args(argv)
+
+
+def main(argv: list[str] | None = None) -> None:
+    args = parse_args(argv)
+    func = OPERATIONS[args.operation]
+    result = func(args.a, args.b)
+    print(result)
+
+
+if __name__ == "__main__":
+    main()
