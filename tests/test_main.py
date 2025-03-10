import pytest
import pathlib
import io
from src.diff_tool.main import main


@pytest.mark.parametrize(
    "lines1, lines2, expected_lcs",
    [
        (
            ["This is a test which contains:", "this is the lcs"],
            ["this is the lcs", "we're testing"],
            ["this is the lcs"]
        ),
        (
            ["one", "two", "three"],
            ["four", "five", "six"],
            []
        ),
        (
            ["one", "two", "three", "four", "five"],
            ["one", "three", "five"],
            ["one", "three", "five"]
        ),
    ]
)
def test_main_lines(tmp_path: pathlib.Path, lines1, lines2, expected_lcs):
    file1 = tmp_path / "original.txt"
    file2 = tmp_path / "new.txt"

    file1.write_text("\n".join(lines1))
    file2.write_text("\n".join(lines2))

    out = io.StringIO()
    main(file1=file1, file2=file2, output=out, diff=True)

    assert out.getvalue().strip() == "\n".join(expected_lcs)

@pytest.mark.parametrize(
    "lines1, lines2, expected_lcs",
    [
        (
            [
                "Coding Challenges helps you become a better software engineer through",
                "that build real applications."
            ],
            [
                "Helping you become a better software engineer through coding challenges",
                "that build real applications."
            ],
            [
                "become a better software engineer through",
                "that build real applications."
            ]
        ),
        (
            [
                "I’ve used or am using these coding challenges as exercises to learn a",
                "new programming language or technology."
            ],
            [
                "These are challenges that I’ve used or am using as exercises to learn",
                "a new programming language or technology."
            ],
            [
                "challenges that I’ve used or am using as exercises to learn",
                "a new programming language or technology."
            ]
        )
    ]
)
def test_main_lcs_lines(tmp_path: pathlib.Path, lines1, lines2, expected_lcs):
    file1 = tmp_path / "original.txt"
    file2 = tmp_path / "new.txt"

    file1.write_text("\n".join(lines1))
    file2.write_text("\n".join(lines2))

    out = io.StringIO()
    main(file1=file1, file2=file2, output=out, diff=True)

    assert out.getvalue().strip() == "\n".join(expected_lcs)


