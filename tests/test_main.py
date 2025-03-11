import pytest
import pathlib
import io
from src.diff_tool.main import main


@pytest.mark.parametrize(
    "lines1, lines2, expected_lcs",
    [
        (
            [
                "Coding Challenges helps you become",
                "I share a weekly coding challenge",
                "I’ve used or am using these coding challenges",
                "Each challenge will have you writing."
            ],
            [
                "Helping you become a better software engineer",
                "I share a weekly coding challenge",
                "These are challenges that I’ve used",
                "Each challenge will have you writing."
            ],
            [
                "> Helping you become a better software engineer",
                "< Coding Challenges helps you become",
                "> These are challenges that I’ve used",
                "< I’ve used or am using these coding challenges"
            ]
        ),
        (
            [
                "Line one",
                "Line two",
                "Line three",
            ],
            [
                "Line one",
                "Line four",
                "Line three",
            ],
            [
                "> Line four",
                "< Line two"
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


