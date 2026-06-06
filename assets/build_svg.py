import base64

with open("cyberhawk-logo.png", "rb") as f:
    b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode()

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">
  <defs>
    <radialGradient id="bgGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#1a2a4a"/>
      <stop offset="100%" stop-color="#0a1220"/>
    </radialGradient>
    <clipPath id="logoClip">
      <circle cx="120" cy="120" r="68"/>
    </clipPath>
    <style>
      .r1 {{ animation: spin  18s linear infinite; transform-origin: 120px 120px; }}
      .r2 {{ animation: rspin 12s linear infinite; transform-origin: 120px 120px; }}
      .r3 {{ animation: spin  28s linear infinite; transform-origin: 120px 120px; }}
      .r4 {{ animation: rspin 20s linear infinite; transform-origin: 120px 120px; }}
      .pulse {{ animation: pulse 3s ease-in-out infinite; transform-origin: 120px 120px; }}
      .scan  {{ animation: scan  4s ease-in-out infinite; }}
      @keyframes spin  {{ to {{ transform: rotate( 360deg); }} }}
      @keyframes rspin {{ to {{ transform: rotate(-360deg); }} }}
      @keyframes pulse {{ 0%,100% {{ opacity:0.55; }} 50% {{ opacity:0.90; }} }}
      @keyframes scan  {{ 0%,100% {{ opacity:0.3; }} 50% {{ opacity:0.8; }} }}
    </style>
  </defs>

  <circle cx="120" cy="120" r="120" fill="url(#bgGlow)"/>

  <!-- Ring 1: outermost fine dashes -->
  <g class="r1">
    <circle cx="120" cy="120" r="112" fill="none" stroke="#8b5e0a" stroke-width="1" stroke-dasharray="2 6"/>
  </g>

  <!-- Ring 2: bold gold dashes + tick marks -->
  <g class="r2">
    <circle cx="120" cy="120" r="106" fill="none" stroke="#c47b00" stroke-width="2.5" stroke-dasharray="14 5"/>
    <line x1="120" y1="14"  x2="120" y2="4"   stroke="#f5a623" stroke-width="2"/>
    <line x1="120" y1="226" x2="120" y2="236" stroke="#f5a623" stroke-width="2"/>
    <line x1="14"  y1="120" x2="4"   y2="120" stroke="#f5a623" stroke-width="2"/>
    <line x1="226" y1="120" x2="236" y2="120" stroke="#f5a623" stroke-width="2"/>
    <circle cx="47"  cy="47"  r="2.5" fill="#d4890a"/>
    <circle cx="193" cy="47"  r="2.5" fill="#d4890a"/>
    <circle cx="47"  cy="193" r="2.5" fill="#d4890a"/>
    <circle cx="193" cy="193" r="2.5" fill="#d4890a"/>
  </g>

  <!-- Ring 3: mid dotted amber -->
  <g class="r3">
    <circle cx="120" cy="120" r="96" fill="none" stroke="#a06810" stroke-width="1.5" stroke-dasharray="3 7"/>
  </g>

  <!-- Ring 4: inner segmented + dots -->
  <g class="r4">
    <circle cx="120" cy="120" r="87" fill="none" stroke="#d4890a" stroke-width="2" stroke-dasharray="10 4"/>
    <circle cx="120" cy="33"  r="3" fill="#f5a623"/>
    <circle cx="120" cy="207" r="3" fill="#f5a623"/>
    <circle cx="33"  cy="120" r="3" fill="#f5a623"/>
    <circle cx="207" cy="120" r="3" fill="#f5a623"/>
  </g>

  <!-- Ring 5: innermost pulse -->
  <g class="pulse">
    <circle cx="120" cy="120" r="77" fill="none" stroke="#f5a623" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.7"/>
  </g>

  <!-- Logo background -->
  <circle cx="120" cy="120" r="72" fill="#0a1220"/>
  <circle cx="120" cy="120" r="70" fill="#0d1628"/>

  <!-- Logo — base64 embedded -->
  <image href="{b64}"
         x="52" y="52" width="136" height="136"
         clip-path="url(#logoClip)"
         preserveAspectRatio="xMidYMid meet"/>

  <!-- Inner glow rim -->
  <circle cx="120" cy="120" r="70" fill="none" stroke="#c47b00" stroke-width="1.5" opacity="0.5" class="scan"/>
</svg>"""

with open("logo-ring.svg", "w", encoding="utf-8") as f:
    f.write(svg)

import os
print(f"Done — {os.path.getsize('logo-ring.svg'):,} bytes")
