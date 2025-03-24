import marimo

__generated_with = "0.11.26"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    mo.md("# python-jsonpath Sandbox")
    return (mo,)


@app.cell
def _():
    import json
    import jsonpath
    return json, jsonpath


@app.cell
def _(json):
    # Load the bookstore data
    with open("data/bookstore.json") as stream:
        store = json.load(stream)
    store
    return store, stream


@app.cell
def _(jsonpath, store):
    # List titles
    print("\n# Books Titles")
    for title in jsonpath.findall('$.inventory..title', store):
        print(f"- {title}")
    return (title,)


@app.cell
def _(jsonpath, store):
    # List low stock books
    print("\n# Low in stock")
    books = jsonpath.findall("$.inventory[?@.count < 10]", store)
    for book in books:
        print(f"- {book['title']}: {book['count']}")
    return book, books


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
