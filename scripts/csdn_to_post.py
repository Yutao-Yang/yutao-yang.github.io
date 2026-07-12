import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime
import sys

def fetch_csdn_article(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    title = ""
    date_str = ""
    tags = []
    content = ""
    
    title_tag = soup.find('h1', class_=['title-article', 'article-title'])
    if title_tag:
        title = title_tag.get_text(strip=True)
    
    date_tag = soup.find('span', class_='time')
    if not date_tag:
        date_tag = soup.find('span', class_='post-time')
    if date_tag:
        date_str = date_tag.get_text(strip=True)
    
    tag_list = soup.find_all('a', class_=['tag-link', 'article-tag-link'])
    tags = [tag.get_text(strip=True) for tag in tag_list if tag.get_text(strip=True)]
    
    content_div = soup.find('div', class_=['article_content', 'content_views', 'markdown_views'])
    if content_div:
        content = content_div.prettify()
    
    return {
        'title': title,
        'date_str': date_str,
        'tags': tags,
        'content': content
    }

def html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for script in soup(['script', 'style']):
        script.decompose()
    
    result = []
    for element in soup.descendants:
        if element.name == 'h1':
            result.append(f"# {element.get_text(strip=True)}\n")
        elif element.name == 'h2':
            result.append(f"## {element.get_text(strip=True)}\n")
        elif element.name == 'h3':
            result.append(f"### {element.get_text(strip=True)}\n")
        elif element.name == 'h4':
            result.append(f"#### {element.get_text(strip=True)}\n")
        elif element.name == 'h5':
            result.append(f"##### {element.get_text(strip=True)}\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                result.append(text + "\n")
        elif element.name == 'strong' or element.name == 'b':
            text = element.get_text(strip=True)
            if text:
                result.append(f"**{text}**")
        elif element.name == 'em' or element.name == 'i':
            text = element.get_text(strip=True)
            if text:
                result.append(f"*{text}*")
        elif element.name == 'ul':
            for li in element.find_all('li'):
                text = li.get_text(strip=True)
                if text:
                    result.append(f"- {text}\n")
        elif element.name == 'ol':
            for idx, li in enumerate(element.find_all('li'), 1):
                text = li.get_text(strip=True)
                if text:
                    result.append(f"{idx}. {text}\n")
        elif element.name == 'code':
            parent = element.parent
            if parent and parent.name == 'pre':
                lang = parent.get('class', [])
                lang_str = lang[-1].replace('language-', '') if lang else ''
                code_text = element.get_text()
                result.append(f"``` {lang_str}\n{code_text}\n```\n")
            else:
                text = element.get_text(strip=True)
                if text:
                    result.append(f"`{text}`")
        elif element.name == 'pre':
            code = element.find('code')
            if code:
                lang = code.get('class', [])
                lang_str = lang[-1].replace('language-', '') if lang else ''
                code_text = code.get_text()
                result.append(f"``` {lang_str}\n{code_text}\n```\n")
        elif element.name == 'a':
            href = element.get('href', '')
            text = element.get_text(strip=True)
            if text and href:
                result.append(f"[{text}]({href})")
        elif element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '')
            if src:
                result.append(f"![{alt}]({src})\n")
        elif element.name == 'br':
            result.append("\n")
        elif element.name == 'hr':
            result.append("---\n")
    
    return '\n'.join(result).replace('\n\n\n', '\n\n').strip()

def parse_date(date_str):
    patterns = [
        r'(\d{4})-(\d{2})-(\d{2})',
        r'(\d{4})年(\d{1,2})月(\d{1,2})日',
        r'(\d{4})/(\d{1,2})/(\d{1,2})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str)
        if match:
            year, month, day = match.groups()
            return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    
    return datetime.now().strftime('%Y-%m-%d')

def generate_filename(title, date_str):
    clean_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '-').lower()
    clean_title = re.sub(r'-+', '-', clean_title)[:100]
    return f"{date_str}-{clean_title}.md"

def write_markdown_file(data, output_dir):
    filename = generate_filename(data['title'], data['date'])
    filepath = os.path.join(output_dir, filename)
    
    if os.path.exists(filepath):
        overwrite = input(f"File {filename} already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Skipping...")
            return False
    
    tags_str = '\n  - '.join(data['tags']) if data['tags'] else ''
    if tags_str:
        tags_str = '\n  - ' + tags_str
    
    content = f"""---
title: '{data['title']}'
date: {data['date']}
permalink: /posts/{data['date'].replace('-', '/')}/{data['title'].lower().replace(' ', '-')}/
tags:{tags_str}
---

{data['markdown_content']}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully created: {filepath}")
    return True

def main():
    print("=" * 60)
    print("CSDN Article to Markdown Converter")
    print("=" * 60)
    print("Enter CSDN article URL, or 'quit' to exit")
    print("=" * 60)
    
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_posts')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    while True:
        url = input("\nEnter CSDN URL: ").strip()
        
        if url.lower() == 'quit':
            print("Exiting...")
            break
        
        if not url.startswith('http'):
            print("Invalid URL. Please enter a valid URL.")
            continue
        
        print(f"Fetching article from: {url}")
        html = fetch_csdn_article(url)
        
        if not html:
            continue
        
        print("Parsing article...")
        parsed = parse_html(html)
        
        if not parsed['title']:
            print("Failed to parse article title.")
            continue
        
        print(f"Title: {parsed['title']}")
        print(f"Date: {parsed['date_str']}")
        print(f"Tags: {', '.join(parsed['tags'])}")
        
        date = parse_date(parsed['date_str'])
        print(f"Parsed date: {date}")
        
        print("Converting to Markdown...")
        markdown_content = html_to_markdown(parsed['content'])
        
        data = {
            'title': parsed['title'],
            'date': date,
            'tags': parsed['tags'],
            'markdown_content': markdown_content
        }
        
        write_markdown_file(data, output_dir)

if __name__ == '__main__':
    main()
