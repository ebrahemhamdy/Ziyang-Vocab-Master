import re
import os

files = [
    "GRE 24套解析器 v5.html",
    "单词工厂 V14Gem.html",
    "背单词_V49_mac字典右键_fixed.html"
]

out_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Ziyang Vocab Master (公益开源版)</title>
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    
    <!-- Shared Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dexie/3.2.4/dexie.min.js"></script>

    <style>
        /* Global Tab Styles */
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background: #f3f4f6; }
        .tab-bar { display: flex; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); padding: 0 20px; overflow-x: auto; white-space: nowrap; }
        .tab-btn { padding: 16px 24px; cursor: pointer; border: none; background: none; font-size: 16px; font-weight: 600; color: #6b7280; border-bottom: 3px solid transparent; flex-shrink: 0; }
        .tab-btn:hover { color: #2563eb; }
        .tab-btn.active { color: #2563eb; border-bottom-color: #2563eb; }
        .tab-content { display: none; padding: 10px; max-width: 1200px; margin: 0 auto; }
        .tab-content.active { display: block; }
        .footer { text-align: center; padding: 20px; color: #6b7280; font-size: 13px; margin-top: 20px; }
        
        /* CSS Reset for Scoped containers */
        .scoped-container { position: relative; }
    </style>
"""

apps_css = []
apps_html = []
apps_js = []

for idx, fname in enumerate(files):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
        
        # Extract style
        style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
        if style_match:
            css = style_match.group(1)
            # Scope CSS by prepending #tabX to rules
            scoped_css = []
            # Very basic parsing, not perfect but good enough for these files
            for rule in re.split(r'\}', css):
                rule = rule.strip()
                if not rule:
                    continue
                if '{' in rule:
                    selectors, declarations = rule.split('{', 1)
                    
                    # Handle @media queries
                    if selectors.strip().startswith('@media'):
                        scoped_css.append(f"{selectors} {{")
                        sub_rules = declarations.split('}')
                        for sub_rule in sub_rules:
                            sub_rule = sub_rule.strip()
                            if not sub_rule: continue
                            if '{' in sub_rule:
                                sub_sel, sub_dec = sub_rule.split('{', 1)
                                new_sub_sels = ", ".join([f"#tab{idx} {s.strip()}" for s in sub_sel.split(',') if s.strip()])
                                scoped_css.append(f"  {new_sub_sels} {{ {sub_dec} }}")
                        scoped_css.append("}")
                        continue
                        
                    # Handle normal rules
                    if selectors.strip().startswith(':root'):
                        scoped_css.append(f"#tab{idx} {{ {declarations} }}")
                    elif selectors.strip() == 'body':
                        scoped_css.append(f"#tab{idx} {{ {declarations} }}")
                    else:
                        new_selectors = ", ".join([f"#tab{idx} {s.strip()}" for s in selectors.split(',') if s.strip()])
                        scoped_css.append(f"{new_selectors} {{ {declarations} }}")
            apps_css.append("\n".join(scoped_css))
            
        # Extract body
        body_match = re.search(r'<body>(.*?)<script', content, re.DOTALL)
        if body_match:
            apps_html.append(body_match.group(1).strip())
        else:
            # Maybe there are no scripts before body end
            body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
            if body_match:
                html_part = re.sub(r'<script.*?</script>', '', body_match.group(1), flags=re.DOTALL)
                apps_html.append(html_part.strip())
            else:
                apps_html.append("<!-- No Body -->")
                
        # Extract JS
        js_matches = re.findall(r'<script(?!\s+src)[^>]*>(.*?)</script>', content, re.DOTALL)
        combined_js = "\n".join(js_matches)
        apps_js.append(combined_js)

out_html += "<style>\n"
for idx, css in enumerate(apps_css):
    out_html += f"/* ====== APP {idx} CSS ====== */\n{css}\n"
out_html += "</style>\n</head>\n<body>\n"

out_html += """
    <div class="tab-bar">
        <button class="tab-btn active" onclick="switchTab(0)">1. PDF 词库提取器</button>
        <button class="tab-btn" onclick="switchTab(1)">2. AI 单词加工厂</button>
        <button class="tab-btn" onclick="switchTab(2)">3. 沉浸背单词测验</button>
    </div>
"""

for idx, html in enumerate(apps_html):
    active_cls = "active" if idx == 0 else ""
    out_html += f'    <div id="tab{idx}" class="tab-content {active_cls} scoped-container">\n'
    out_html += html + "\n"
    out_html += "    </div>\n"

out_html += """
    <div class="footer">
        🚀 Developed by <strong>Ziyang Xu</strong> (10th Grade, High School Affiliated to BNU) <br>
        Open Source & Free software designed for students to study customized textbook vocabularies.
    </div>

    <script>
        function switchTab(index) {
            document.querySelectorAll('.tab-content').forEach((el, i) => {
                el.classList.toggle('active', i === index);
            });
            document.querySelectorAll('.tab-btn').forEach((el, i) => {
                el.classList.toggle('active', i === index);
            });
        }
    </script>
"""

for idx, js in enumerate(apps_js):
    out_html += f"<!-- ====== APP {idx} JS ====== -->\n"
    out_html += f"<script>\n(function() {{\n{js}\n}})();\n</script>\n"

out_html += "</body>\n</html>\n"

with open("Ziyang_Vocab_Master.html", "w", encoding="utf-8") as f:
    f.write(out_html)

print("Merged successfully to Ziyang_Vocab_Master.html")
