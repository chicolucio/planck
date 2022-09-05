import streamlit as st


def load_css(css_file_path):
    """
    Inject CSS
    Returns
    -------
    None
        Inject CSS through Streamlit markdown with HTML flag.
    """

    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def find_me_buttons(site, url_or_user, width=120, margin=3):
    """
    Create social media buttons
    Parameters
    ----------
    site : str
        the name of the social media
    url_or_user : str
        full URL (e.g. personal website) or user ID (e.g. social media)
    width : int
        width of the button
    margin : int
        margin around the button
    Returns
    -------
    Streamlit markdown object
    """

    if site == "linkedin":
        button_code = f"""
        <a href="https://www.linkedin.com/in/{url_or_user}" target="_blank">
        <img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" width="{width}" style="margin:{margin}px" target="_blank"></a>"""  # noqa: E501
    elif site == "portfolio":
        button_code = f"""
        <a href="{url_or_user}" target="_blank">
        <img src="https://img.shields.io/badge/portfolio-00A98F?style=for-the-badge&logo=About.me&logoColor=white" width="{width}" style="margin:{margin}px" target="_blank"></a>"""  # noqa: E501
    elif site == "github":
        button_code = f"""
        <a href="https://github.com/{url_or_user}" target="_blank">
        <img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white" width="{width}" style="margin:{margin}px" target="_blank"></a>"""  # noqa: E501
    elif site == "github_sponsors":
        button_code = f"""
        <a href="https://github.com/sponsors/{url_or_user}" target="_blank">
        <img src="https://img.shields.io/badge/-Sponsor-EA4AAA?style=for-the-badge&logo=GitHubSponsors&logoColor=white" width="{width}" style="margin:{margin}px" target="_blank"></a>"""  # noqa: E501
    else:
        raise ValueError("Invalid site")
    return st.markdown(button_code, unsafe_allow_html=True)


def github_avatar_link(user_id):
    """
    Returns the full GitHub avatar link for a given user ID
    Parameters
    ----------
    user_id : int
    Returns
    -------
    str
        GitHub avatar link
    """
    return f"https://avatars.githubusercontent.com/u/{user_id}?v=4"


def text_from_markdown(markdown_file, image_markdown="!["):
    """
    Extract only text from a markdown (avoiding figures with ![')
    This way, the figures can be placed with Streamlit functions which make
    them responsive,
    Parameters
    ----------
    markdown_file : str
        path to file
    image_markdown : str
        string pattern to avoid
    Returns
    -------
    list
        List of strings. Each string is a part of the text before/after a
        image.
    """

    content_parts = []

    with open(markdown_file) as f:
        content = []
        for num, line in enumerate(f, 1):
            if image_markdown in line:
                content_parts.append(content)
                content = []
            else:
                content.append(line)
        content_parts.append(content)
    return content_parts


def vertical_spacer(lines, sidebar=False):
    """
    On mobile screens the last slider is too close to the bottom.
    This function can be used to insert empty lines and create a vertical
    empty space.

    Parameters
    ----------
    lines : int
    sidebar : bool, default: True
    Returns
    -------
    None
    """
    for _ in range(lines):
        if sidebar:
            st.sidebar.write("\n")
        else:
            st.write("\n")
