from pathlib import Path
import sys
import io

def longest_common_subsequence_lines(lines1, lines2):
    m = len(lines1)
    n = len(lines2)

    dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if lines1[i - 1] == lines2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + [lines1[i - 1]]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
    return dp[m][n]

def main(
    *,
    file1: Path,
    file2: Path,
    diff: bool = False,
    output: io.StringIO = sys.stdout,
) -> None:
    string1 = file1.read_text().split("\n")
    string2 = file2.read_text().split("\n")

    lcs = longest_common_subsequence_lines(string1, string2)

    if diff:
        i, j, k = 0, 0, 0
        while i < len(string1) or j < len(string2):
            if k < len(lcs) and i < len(string1) and string1[i] == lcs[k]:
                i += 1
                j += 1
                k += 1
            elif j < len(string2) and (k >= len(lcs) or string2[j] != lcs[k]):
                output.write(f"> {string2[j]}\n")
                j += 1
            elif i < len(string1) and (k >= len(lcs) or string1[i] != lcs[k]):
                output.write(f"< {string1[i]}\n")
                i += 1
    else:
        output.write("\n".join(lcs) + "\n")

def _cli() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("file1", type=Path, help="Path to first file")
    parser.add_argument("file2", type=Path, help="Path to second file")
    parser.add_argument("-d", "--diff", action="store_true")
    args = parser.parse_args()

    main(file1=args.file1, file2=args.file2, diff=args.diff)

if __name__ == "__main__":
    _cli()