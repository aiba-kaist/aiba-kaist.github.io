#!/usr/bin/env python3
"""
Google Sheets to Jekyll Sync Script

이 스크립트는 Google Sheets에서 데이터를 가져와서 Jekyll 파일로 변환합니다.
- Members 시트 → _pages/team.md
- Publications 시트 → _bibliography/papers.bib
- Teaching 시트 → _pages/teaching.md
- Industry 시트 → _pages/industry.md
- Gallery 시트 → _pages/gallery.md
"""

import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets 인증
def get_sheet_client():
    creds_json = os.environ.get('GOOGLE_CREDENTIALS')
    if not creds_json:
        raise ValueError("GOOGLE_CREDENTIALS environment variable not set")
    
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=[
            'https://www.googleapis.com/auth/spreadsheets.readonly',
            'https://www.googleapis.com/auth/drive.readonly'
        ]
    )
    return gspread.authorize(creds)

def get_sheet_data(client, sheet_id, sheet_name):
    """시트에서 데이터 가져오기"""
    spreadsheet = client.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    return worksheet.get_all_records()

# ============================================
# Members 시트 → team.md
# ============================================
def generate_team_md(members):
    """Members 데이터로 team.md 생성"""
    
    # 역할별 분류
    faculty = [m for m in members if m['role'] == 'Faculty']
    phd = [m for m in members if m['role'] == 'PhD']
    ms = [m for m in members if m['role'] == 'MS']
    undergrad = [m for m in members if m['role'] == 'Undergrad']
    alumni = [m for m in members if m['role'] == 'Alumni']
    
    content = """---
layout: page
permalink: /team/
title: team
description: Members of AIBA Lab
nav: true
nav_order: 2
---

"""
    
    # Faculty
    if faculty:
        content += "## Faculty\n\n"
        for m in faculty:
            content += f"""<div class="row">
  <div class="col-sm-3">
    <img class="img-fluid rounded" src="/assets/img/members/{m['photo']}" alt="{m['name_en']}">
  </div>
  <div class="col-sm-9">
    <h4>{m['name_en']}</h4>
    <p><strong>{m['position']}</strong><br>
    {m['affiliation']}<br>
    <a href="mailto:{m['email']}">{m['email']}</a>"""
            if m.get('website'):
                content += f""" · 
    <a href="{m['website']}">Personal Website</a>"""
            content += f"""</p>
    <p><em>Research Interests:</em> {m['research_area']}</p>
"""
            if m.get('bio'):
                content += f"""    <ul>
"""
                for line in m['bio'].split('\n'):
                    if line.strip():
                        content += f"""      <li>{line.strip()}</li>
"""
                content += """    </ul>
"""
            content += """  </div>
</div>

---

"""
    
    # PhD Students
    if phd:
        content += "## Ph.D. Students\n\n"
        content += '<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">\n'
        for m in phd:
            content += f"""  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{m['photo']}" alt="{m['name_en']}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{m['name_en']}</h5>
    <p>{m['research_area']}</p>
  </div>
"""
        content += "</div>\n\n---\n\n"
    
    # M.S. Students
    if ms:
        content += "## M.S. Students\n\n"
        content += '<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">\n'
        for m in ms:
            content += f"""  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{m['photo']}" alt="{m['name_en']}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{m['name_en']}</h5>
    <p>{m['research_area']}</p>
  </div>
"""
        content += "</div>\n\n---\n\n"
    
    # Undergraduate Researcher
    if undergrad:
        content += "## Undergraduate Researcher\n\n"
        content += '<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">\n'
        for m in undergrad:
            content += f"""  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{m['photo']}" alt="{m['name_en']}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{m['name_en']}</h5>
    <p>{m['research_area']}</p>
  </div>
"""
        content += "</div>\n\n---\n\n"
    
    # Alumni
    if alumni:
        content += "## Alumni\n\n"
        content += '<div class="row row-cols-2 row-cols-md-4 g-4 mt-3">\n'
        for m in alumni:
            content += f"""  <div class="col text-center mb-4">
    <img class="img-fluid rounded mb-2" src="/assets/img/members/{m['photo']}" alt="{m['name_en']}" style="width:150px;height:150px;object-fit:cover;">
    <h5>{m['name_en']}</h5>
    <p>{m['graduation_info']}</p>
  </div>
"""
        content += "</div>\n\n"
    
    return content

# ============================================
# Publications 시트 → papers.bib
# ============================================
def generate_papers_bib(publications):
    """Publications 데이터로 papers.bib 생성"""
    
    content = """---
---

"""
    
    # 저널 논문
    journals = [p for p in publications if p['type'] == 'journal']
    if journals:
        content += "% Journal Papers\n\n"
        for p in journals:
            content += f"@article{{{p['bibtex_key']},\n"
            content += f"  title={{{p['title']}}},\n"
            content += f"  author={{{p['authors']}}},\n"
            content += f"  journal={{{p['venue']}}},\n"
            if p.get('volume'):
                content += f"  volume={{{p['volume']}}},\n"
            if p.get('number'):
                content += f"  number={{{p['number']}}},\n"
            if p.get('pages'):
                content += f"  pages={{{p['pages']}}},\n"
            content += f"  year={{{p['year']}}},\n"
            if p.get('selected') and str(p['selected']).upper() == 'TRUE':
                content += "  selected={true},\n"
            content += f"  abbr={{{p['abbr']}}}\n"
            content += "}\n\n"
    
    # 컨퍼런스 논문
    conferences = [p for p in publications if p['type'] == 'conference']
    if conferences:
        content += "% Conference Papers\n\n"
        for p in conferences:
            content += f"@inproceedings{{{p['bibtex_key']},\n"
            content += f"  title={{{p['title']}}},\n"
            content += f"  author={{{p['authors']}}},\n"
            content += f"  booktitle={{{p['venue']}}},\n"
            content += f"  year={{{p['year']}}},\n"
            if p.get('award'):
                content += f"  award={{{p['award']}}},\n"
            if p.get('selected') and str(p['selected']).upper() == 'TRUE':
                content += "  selected={true},\n"
            content += f"  abbr={{{p['abbr']}}}\n"
            content += "}\n\n"
    
    return content

# ============================================
# Teaching 시트 → teaching.md
# ============================================
def generate_teaching_md(courses):
    """Teaching 데이터로 teaching.md 생성"""
    
    current = [c for c in courses if str(c.get('is_current', '')).upper() == 'TRUE']
    past = [c for c in courses if str(c.get('is_current', '')).upper() != 'TRUE']
    
    content = """---
layout: page
permalink: /teaching/
title: teaching
description: Courses taught by AIBA Lab
nav: true
nav_order: 5
---

## Current Courses

### KAIST Graduate School of Business

"""
    
    for c in current:
        content += f"""**{c['course_code']} - {c['course_name']}**
- {c['description']}
- Topics: {c['topics']}

"""
    
    content += """---

## Past Courses

"""
    
    for c in past:
        content += f"- {c['course_name']} ({c['semester']})\n"
    
    content += "\n"
    
    return content

# ============================================
# Industry 시트 → industry.md
# ============================================
def generate_industry_md(partners):
    """Industry 데이터로 industry.md 생성"""
    
    collaborators = [p for p in partners if p['type'] == 'Collaborator']
    funding = [p for p in partners if p['type'] == 'Funding']
    
    content = """---
layout: page
permalink: /industry/
title: industry
description: Our industry partners and collaborations
nav: true
nav_order: 4
---

## Collaborators

<div class="row row-cols-2 row-cols-md-3 g-4 mt-3">
"""
    
    for p in collaborators:
        content += f"""  <div class="col text-center mb-4">
    <img class="img-fluid" src="/assets/img/partners/{p['logo']}" alt="{p['name']}" style="max-height:80px;object-fit:contain;">
    <p class="mt-2"><strong>{p['name']}</strong></p>
  </div>
"""
    
    content += """</div>

---

## Funding

<div class="row row-cols-2 row-cols-md-3 g-4 mt-3">
"""
    
    for p in funding:
        content += f"""  <div class="col text-center mb-4">
    <img class="img-fluid" src="/assets/img/partners/{p['logo']}" alt="{p['name']}" style="max-height:80px;object-fit:contain;">
    <p class="mt-2"><strong>{p['name']}</strong></p>
  </div>
"""
    
    content += "</div>\n\n"
    
    return content

# ============================================
# Gallery 시트 → gallery.md
# ============================================
def generate_gallery_md(photos):
    """Gallery 데이터로 gallery.md 생성"""
    
    conferences = [p for p in photos if p['category'] == 'Conferences']
    lab_life = [p for p in photos if p['category'] == 'Lab Life']
    
    content = """---
layout: page
permalink: /gallery/
title: gallery
description: Photos and memories from AIBA Lab
nav: true
nav_order: 6
---

## Conferences & Events

<div class="row mt-3">
"""
    
    for p in conferences:
        content += f"""  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/{p['image']}" alt="{p['caption']}">
    <p class="text-center mt-2">{p['caption']}</p>
  </div>
"""
    
    content += """</div>

---

## Lab Life

<div class="row mt-3">
"""
    
    for p in lab_life:
        content += f"""  <div class="col-sm-6 col-md-4 mb-4">
    <img class="img-fluid rounded" src="/assets/img/gallery/{p['image']}" alt="{p['caption']}">
    <p class="text-center mt-2">{p['caption']}</p>
  </div>
"""
    
    content += "</div>\n\n"
    
    return content

# ============================================
# 메인 실행
# ============================================
def main():
    sheet_id = os.environ.get('SHEET_ID')
    if not sheet_id:
        raise ValueError("SHEET_ID environment variable not set")
    
    print("🔐 Authenticating with Google Sheets...")
    client = get_sheet_client()
    
    print("📊 Fetching data from Google Sheets...")
    
    # Members
    try:
        members = get_sheet_data(client, sheet_id, 'Members')
        team_md = generate_team_md(members)
        with open('_pages/team.md', 'w', encoding='utf-8') as f:
            f.write(team_md)
        print("✅ Generated _pages/team.md")
    except Exception as e:
        print(f"⚠️ Members sheet error: {e}")
    
    # Publications
    try:
        publications = get_sheet_data(client, sheet_id, 'Publications')
        papers_bib = generate_papers_bib(publications)
        with open('_bibliography/papers.bib', 'w', encoding='utf-8') as f:
            f.write(papers_bib)
        print("✅ Generated _bibliography/papers.bib")
    except Exception as e:
        print(f"⚠️ Publications sheet error: {e}")
    
    # Teaching
    try:
        courses = get_sheet_data(client, sheet_id, 'Teaching')
        teaching_md = generate_teaching_md(courses)
        with open('_pages/teaching.md', 'w', encoding='utf-8') as f:
            f.write(teaching_md)
        print("✅ Generated _pages/teaching.md")
    except Exception as e:
        print(f"⚠️ Teaching sheet error: {e}")
    
    # Industry
    try:
        partners = get_sheet_data(client, sheet_id, 'Industry')
        industry_md = generate_industry_md(partners)
        with open('_pages/industry.md', 'w', encoding='utf-8') as f:
            f.write(industry_md)
        print("✅ Generated _pages/industry.md")
    except Exception as e:
        print(f"⚠️ Industry sheet error: {e}")
    
    # Gallery
    try:
        photos = get_sheet_data(client, sheet_id, 'Gallery')
        gallery_md = generate_gallery_md(photos)
        with open('_pages/gallery.md', 'w', encoding='utf-8') as f:
            f.write(gallery_md)
        print("✅ Generated _pages/gallery.md")
    except Exception as e:
        print(f"⚠️ Gallery sheet error: {e}")
    
    print("🎉 Sync complete!")

if __name__ == '__main__':
    main()
