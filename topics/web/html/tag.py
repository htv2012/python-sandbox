#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup


class Style(object):
    @classmethod
    def from_html(cls, html_style):
        style = cls()
        html_style = (
            html_style.replace("color", "font-color").replace("-", "_").replace("'", "")
        )
        for k, v in [kv.split(":") for kv in html_style.split(";") if kv]:
            setattr(style, k, v)
        return style


class Tag(object):
    @classmethod
    def from_html(cls, html_text):
        soup = BeautifulSoup(html_text, "lxml")
        soup = next(soup.body.children)
        tag = cls()
        tag.text = soup.text
        tag.name = soup.name
        tag.style = Style.from_html(soup.get("style", ""))
        return tag


if __name__ == "__main__":
    html_text = """<span style="font-family:'Arial';font-size:27px;line-height:30px;color:#555555;font-style:italic;">Span1</span>"""
    tag = Tag.from_html(html_text)

    print("html: {!r}".format(html_text))
    print()
    print("tag:", tag.name)
    print("text:", tag.text)
    print("style:")
    print("  font-family:", tag.style.font_family)
    print("  font-size:", tag.style.font_size)
    print("  font-style:", tag.style.font_style)
    print("  line-height:", tag.style.line_height)

    t2 = Tag.from_html("<strong>hello world</strong>")
