import pytest
import re

def strip_all_comments(text):
    comment_re = re.compile(r"""
        /\* # Match start of block comment
        (?:.|\n)*?   # Match any character or newline (non-greedy)
        \*/          # Match end of block comment
        |            # OR
        //.* # Match C-style line comment
        |            # OR
        \#.* # Match shell-style line comment
    """, re.VERBOSE)
    return comment_re.sub('', text)

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        pytest.param(
            "int x = 5; // line comment", 
            "int x = 5; ", 
            id="c_style_line_comment"
        ),
        pytest.param(
            "var y = 10; # shell comment", 
            "var y = 10; ", 
            id="shell_style_comment"
        ),
        pytest.param(
            "/* multi-line\n comment */code", 
            "code", 
            id="multi_line_block_comment"
        ),
        pytest.param(
            "code /* block */ and // line\n# shell", 
            "code  and \n", 
            id="mixed_comment_types"
        ),
        pytest.param(
            "no comments here", 
            "no comments here", 
            id="no_comments_present"
        ),
        pytest.param(
            "", 
            "", 
            id="empty_string"
        ),
    ]
)
def test_strip_comments(input_text, expected_output):
    assert strip_all_comments(input_text) == expected_output
