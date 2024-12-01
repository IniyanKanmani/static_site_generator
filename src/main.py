# from textnode import TextNode
from inline_markdown import extract_markdown_images, extract_markdown_links


def main():
    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)
    print(
        extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
    )
    print(
        extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
    )


if __name__ == "__main__":
    main()
