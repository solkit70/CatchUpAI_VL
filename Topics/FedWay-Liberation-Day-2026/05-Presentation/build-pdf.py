# -*- coding: utf-8 -*-
"""slides.html -> 16:9 PDF (슬라이드당 1페이지)."""
import os
from playwright.sync_api import sync_playwright

BASE = (r'C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics'
        r'\FedWay-Liberation-Day-2026\05-Presentation')
SRC = os.path.join(BASE, 'slides.html')
OUT = os.path.join(BASE, 'out', '20260815-박창수-발표.pdf')

os.makedirs(os.path.dirname(OUT), exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('file:///' + SRC.replace('\\', '/'))
    page.wait_for_timeout(1500)
    page.pdf(
        path=OUT,
        width='1920px',
        height='1080px',
        print_background=True,
        margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
        prefer_css_page_size=True,
    )
    browser.close()

size = os.path.getsize(OUT) / 1024 / 1024
print(f'PDF 생성: {OUT}')
print(f'크기: {size:.1f} MB')
