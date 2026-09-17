"""Check generated HTML using only Python's standard library.

Run after `bundle exec jekyll build`: python scripts/check_site.py
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = set()
        self.links = []
        self.errors = []
        self.h1_count = 0
        self.main_count = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f"Duplicate id: {attrs['id']}")
            self.ids.add(attrs['id'])
        self.h1_count += tag == 'h1'
        self.main_count += tag == 'main'
        if tag == 'img' and 'alt' not in attrs:
            self.errors.append('Image is missing alt text')
        for attr in ('href', 'src'):
            if attrs.get(attr):
                self.links.append(attrs[attr])


def check(root):
    pages = {}
    errors = []
    for path in root.rglob('*.html'):
        page = Page(path)
        page.feed(path.read_text(encoding='utf-8'))
        pages[path.resolve()] = page
        if page.h1_count != 1 or page.main_count != 1:
            page.errors.append('Expected exactly one h1 and one main landmark')
        errors.extend(f'{path}: {error}' for error in page.errors)
    if not pages:
        errors.append(f'No HTML found in {root}; build the site first')
    for path, page in pages.items():
        source_url = '/' + path.relative_to(root).as_posix()
        for link in page.links:
            url = urlsplit(urljoin(source_url, link))
            if url.scheme or url.netloc:
                continue
            target = root / unquote(url.path).lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{path}: missing local target {link}')
            elif url.fragment and target.resolve() in pages:
                if unquote(url.fragment) not in pages[target.resolve()].ids:
                    errors.append(f'{path}: missing anchor {link}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'Checked {len(pages)} pages: local links, anchors, images, IDs, and landmarks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(check(Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()))
