import base64, os

# embed the CyberHawk logo
with open("cyberhawk-logo.png", "rb") as f:
    logo_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode()

W = 800   # total width
H = 530   # total height

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>
  <!-- hex grid bg -->
  <pattern id="hexgrid" width="34" height="30" patternUnits="userSpaceOnUse">
    <polygon points="17,0 34,8.5 34,21.5 17,30 0,21.5 0,8.5"
             fill="none" stroke="#0066cc" stroke-width="0.4" opacity="0.13"/>
  </pattern>

  <!-- scan gradient -->
  <linearGradient id="scanGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#4da6ff" stop-opacity="0"/>
    <stop offset="40%"  stop-color="#4da6ff" stop-opacity="0.5"/>
    <stop offset="60%"  stop-color="#4da6ff" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#4da6ff" stop-opacity="0"/>
  </linearGradient>

  <!-- header fill -->
  <linearGradient id="hdrGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="#0066cc" stop-opacity="0.30"/>
    <stop offset="50%"  stop-color="#0066cc" stop-opacity="0.08"/>
    <stop offset="100%" stop-color="#0066cc" stop-opacity="0.30"/>
  </linearGradient>

  <!-- CTA card -->
  <linearGradient id="ctaGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="#001433"/>
    <stop offset="100%" stop-color="#001020"/>
  </linearGradient>

  <!-- card fill -->
  <linearGradient id="cardGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="#0d1628"/>
    <stop offset="100%" stop-color="#091120"/>
  </linearGradient>

  <clipPath id="logoClip">
    <circle cx="34" cy="31" r="22"/>
  </clipPath>

  <style>
    .mono  {{ font-family: 'Courier New', Courier, monospace; }}
    .sans  {{ font-family: Arial, Helvetica, sans-serif; }}

    @keyframes scan {{
      0%   {{ transform: translateY(-10px); opacity: 0; }}
      4%   {{ opacity: 1; }}
      96%  {{ opacity: 1; }}
      100% {{ transform: translateY({H+10}px); opacity: 0; }}
    }}
    @keyframes breathe {{
      0%,100% {{ stroke-opacity: .40; }}
      50%      {{ stroke-opacity: .90; }}
    }}
    @keyframes ctaPulse {{
      0%,100% {{ opacity: .80; }}
      50%      {{ opacity: 1;  }}
    }}
    @keyframes livePulse {{
      0%,100% {{ opacity: 1;  r: 5;   }}
      50%      {{ opacity: .4; r: 6.5; }}
    }}
    @keyframes cornerFlicker {{
      0%,100% {{ opacity: .65; }}
      50%      {{ opacity: 1;  }}
    }}

    .scan-line    {{ animation: scan          5s linear      infinite; }}
    .outer-border {{ animation: breathe       3s ease-in-out infinite; }}
    .cta-btn      {{ animation: ctaPulse      2.5s ease-in-out infinite; }}
    .live-dot     {{ animation: livePulse     1.3s ease-in-out infinite; }}
    .corner       {{ animation: cornerFlicker 4s ease-in-out infinite; }}
  </style>
</defs>

<!-- ═══ BACKGROUND ═══ -->
<rect width="{W}" height="{H}" fill="#0a1220"/>
<rect width="{W}" height="{H}" fill="url(#hexgrid)"/>

<!-- outer glow border -->
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="9"
      fill="none" stroke="#0066cc" stroke-width="2.2" class="outer-border"/>
<rect x="7" y="7" width="{W-14}" height="{H-14}" rx="7"
      fill="none" stroke="#0066cc" stroke-width="0.5" opacity=".20"/>

<!-- corner accents -->
<path d="M1,38 L1,1 L38,1"              fill="none" stroke="#f5a623" stroke-width="2.8" class="corner"/>
<path d="M{W-38},1 L{W-1},1 L{W-1},38"  fill="none" stroke="#f5a623" stroke-width="2.8" class="corner"/>
<path d="M1,{H-38} L1,{H-1} L38,{H-1}"              fill="none" stroke="#f5a623" stroke-width="2.8" class="corner"/>
<path d="M{W-38},{H-1} L{W-1},{H-1} L{W-1},{H-38}" fill="none" stroke="#f5a623" stroke-width="2.8" class="corner"/>

<!-- scan line -->
<rect x="0" y="0" width="{W}" height="9" fill="url(#scanGrad)" class="scan-line"/>

<!-- ═══ HEADER ═══ -->
<rect x="1.5" y="1.5" width="{W-3}" height="64" rx="8" fill="url(#hdrGrad)"/>
<line x1="1.5" y1="65.5" x2="{W-1.5}" y2="65.5" stroke="#0066cc" stroke-width="0.8" opacity=".55"/>

<!-- CyberHawk logo (circle-clipped) -->
<circle cx="34" cy="33" r="23" fill="#0a1220" stroke="#f5a623" stroke-width="1.5"/>
<image href="{logo_b64}" x="12" y="11" width="44" height="44" clip-path="url(#logoClip)" preserveAspectRatio="xMidYMid meet"/>

<!-- vertical divider -->
<line x1="68" y1="14" x2="68" y2="52" stroke="#0066cc" stroke-width="1" opacity=".40"/>

<!-- name + title -->
<text x="80" y="34" class="sans" font-size="16" font-weight="bold"
      fill="#ffffff" letter-spacing="3">RUDRA VERMA</text>
<text x="80" y="53" class="mono" font-size="9.5"
      fill="#4da6ff" letter-spacing="1.5">SENIOR CYBER SECURITY ARCHITECT · CYBERHAWK CONSULTANCY · NZ</text>

<!-- right: CONNECT label -->
<text x="598" y="32" class="mono" font-size="11" fill="#0066cc"
      letter-spacing="3" font-weight="bold">CONNECT</text>
<text x="598" y="52" class="mono" font-size="9" fill="#7d8590"
      letter-spacing="0.5">cyberhawkthreatintel.com</text>

<!-- LIVE dot -->
<circle cx="776" cy="27" r="5.5" fill="#00ff41" class="live-dot"/>
<text x="776" y="47" class="mono" font-size="8.5" fill="#00ff41"
      text-anchor="middle" letter-spacing="1">LIVE</text>

<!-- ═══ WEBSITE CTA CARD ═══ -->
<rect x="16" y="78" width="768" height="80" rx="6" fill="url(#ctaGrad)"/>
<rect x="16" y="78" width="768" height="80" rx="6"
      fill="none" stroke="#0066cc" stroke-width="1.2"/>
<rect x="16" y="78" width="4.5" height="80" rx="2" fill="#0066cc"/>

<!-- globe icon -->
<g transform="translate(52,118)">
  <circle cx="0" cy="0" r="20" fill="none" stroke="#0066cc" stroke-width="1.8"/>
  <ellipse cx="0" cy="0" rx="8" ry="20" fill="none" stroke="#0066cc" stroke-width="1.1"/>
  <line x1="-20" y1="0"   x2="20" y2="0"   stroke="#0066cc" stroke-width="0.9"/>
  <line x1="-18" y1="-10" x2="18" y2="-10" stroke="#0066cc" stroke-width="0.7"/>
  <line x1="-18" y1="10"  x2="18" y2="10"  stroke="#0066cc" stroke-width="0.7"/>
</g>

<text x="88" y="108" class="sans" font-size="22" font-weight="bold"
      fill="#ffffff" letter-spacing="0.5">cyberhawkthreatintel.com</text>
<text x="88" y="128" class="mono" font-size="10.5"
      fill="#aaaaaa" letter-spacing="0.3">AI-powered threat intelligence platform · 272,000+ IOCs · 79 live feeds</text>
<text x="88" y="147" class="mono" font-size="9.5"
      fill="#4da6ff" letter-spacing="0.5">Free account · real-time threat dashboards · MISP integrated</text>

<!-- CTA button -->
<rect x="594" y="94" width="176" height="48" rx="5" fill="#0066cc" class="cta-btn"/>
<rect x="594" y="94" width="176" height="48" rx="5"
      fill="none" stroke="#4da6ff" stroke-width="1" opacity=".65"/>
<text x="682" y="113" class="mono" font-size="9.5" fill="#cce5ff"
      text-anchor="middle" letter-spacing="2">SIGN UP FREE</text>
<text x="682" y="132" class="sans"  font-size="14" font-weight="bold"
      fill="#ffffff" text-anchor="middle">GET ACCESS</text>

<!-- ═══ SOCIAL DIVIDER ═══ -->
<line x1="16"  y1="173" x2="288" y2="173" stroke="#0066cc" stroke-width="0.6" opacity=".40"/>
<text x="400" y="178" class="mono" font-size="9.5" fill="#4da6ff"
      text-anchor="middle" letter-spacing="3" opacity=".9">SOCIAL CHANNELS</text>
<line x1="512" y1="173" x2="784" y2="173" stroke="#0066cc" stroke-width="0.6" opacity=".40"/>

<!-- ═══ SOCIAL CARDS (stacked, full width) ═══ -->

<!-- Card height + gap -->
<!-- YOUTUBE: y=184, h=72 -->
<rect x="16" y="184" width="768" height="72" rx="6" fill="url(#cardGrad)"/>
<rect x="16" y="184" width="768" height="72" rx="6"
      fill="none" stroke="#cc2200" stroke-width="1.2" opacity=".75"/>
<rect x="16" y="184" width="5" height="72" rx="2" fill="#ff0000"/>
<!-- YT icon -->
<rect x="32" y="203" width="36" height="24" rx="4" fill="#ff0000"/>
<polygon points="44,208.5 44,221.5 56,215" fill="#ffffff"/>
<!-- labels -->
<text x="80" y="204" class="mono" font-size="10" fill="#ff5555" letter-spacing="2.5">YOUTUBE</text>
<text x="80" y="222" class="sans"  font-size="14" font-weight="bold" fill="#ffffff">@cyberhawkconsultancy</text>
<text x="80" y="242" class="mono" font-size="11" fill="#ffbbbb">@cyberhawkk</text>
<text x="590" y="222" class="mono" font-size="10" fill="#777" text-anchor="end">hacking · security · threat intel</text>

<!-- X / TWITTER: y=264, h=60 -->
<rect x="16" y="264" width="768" height="60" rx="6" fill="url(#cardGrad)"/>
<rect x="16" y="264" width="768" height="60" rx="6"
      fill="none" stroke="#888888" stroke-width="1.2" opacity=".75"/>
<rect x="16" y="264" width="5" height="60" rx="2" fill="#888888"/>
<!-- X icon -->
<line x1="35" y1="278" x2="57" y2="308" stroke="#ffffff" stroke-width="3"/>
<line x1="57" y1="278" x2="35" y2="308" stroke="#ffffff" stroke-width="3"/>
<text x="80" y="284" class="mono" font-size="10" fill="#bbbbbb" letter-spacing="2.5">X  ·  TWITTER</text>
<text x="80" y="304" class="sans"  font-size="14" font-weight="bold" fill="#ffffff">@cyberhawkintel</text>
<text x="590" y="304" class="mono" font-size="10" fill="#777" text-anchor="end">threat intel · analysis · advisories</text>

<!-- TIKTOK: y=332, h=60 -->
<rect x="16" y="332" width="768" height="60" rx="6" fill="url(#cardGrad)"/>
<rect x="16" y="332" width="768" height="60" rx="6"
      fill="none" stroke="#69c9d0" stroke-width="1.2" opacity=".75"/>
<rect x="16" y="332" width="5" height="60" rx="2" fill="#69c9d0"/>
<!-- TikTok note icon -->
<text x="28" y="378" class="mono" font-size="36" fill="#69c9d0" opacity=".9">♪</text>
<text x="80" y="352" class="mono" font-size="10" fill="#69c9d0" letter-spacing="2.5">TIKTOK</text>
<text x="80" y="372" class="sans"  font-size="14" font-weight="bold" fill="#ffffff">@cyberhawkthreatintel</text>
<text x="590" y="372" class="mono" font-size="10" fill="#777" text-anchor="end">hacking shorts · news · tips</text>

<!-- TELEGRAM: y=400, h=60 -->
<rect x="16" y="400" width="768" height="60" rx="6" fill="url(#cardGrad)"/>
<rect x="16" y="400" width="768" height="60" rx="6"
      fill="none" stroke="#26A5E4" stroke-width="1.2" opacity=".75"/>
<rect x="16" y="400" width="5" height="60" rx="2" fill="#26A5E4"/>
<!-- Telegram paper plane -->
<polygon points="28,432 56,418 48,442" fill="#26A5E4" opacity=".95"/>
<polygon points="40,436 48,442 52,426" fill="#1a7bbf"/>
<text x="80" y="420" class="mono" font-size="10" fill="#26A5E4" letter-spacing="2.5">TELEGRAM</text>
<text x="80" y="440" class="sans"  font-size="14" font-weight="bold" fill="#ffffff">@cyberhawkthreatintel</text>
<text x="590" y="440" class="mono" font-size="10" fill="#777" text-anchor="end">intel channel · alerts · updates</text>

<!-- ═══ FOOTER ═══ -->
<line x1="1.5" y1="470" x2="{W-1.5}" y2="470" stroke="#0066cc" stroke-width="0.5" opacity=".30"/>
<rect x="1.5" y="470" width="{W-3}" height="58" rx="0" fill="#0066cc" opacity=".05"/>

<text x="400" y="492" class="sans"  font-size="10.5" fill="#4da6ff"
      text-anchor="middle" letter-spacing="1.5">RUDRA VERMA · SENIOR SECURITY ARCHITECT · CYBERHAWK CONSULTANCY</text>
<text x="400" y="510" class="mono"  font-size="9"   fill="#666"
      text-anchor="middle">cyberhawkthreatintel.com · New Zealand · Building the tools that did not exist.</text>
<text x="400" y="524" class="mono"  font-size="8"   fill="#444"
      text-anchor="middle">Authorized security research and penetration testing only. Unauthorized use is illegal.</text>
</svg>"""

out_path = "connect.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Done — {os.path.getsize(out_path):,} bytes")
