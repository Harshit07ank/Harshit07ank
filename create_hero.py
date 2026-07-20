import os

ascii_path = 'assets/ascii-art (1).svg'
out_path = 'assets/hero.svg'

with open(ascii_path, 'r', encoding='utf-8') as f:
    ascii_content = f.read()

# Extract inner content of ascii-art
start_idx = ascii_content.find('<rect')
end_idx = ascii_content.find('</svg>')
inner_svg = ascii_content[start_idx:end_idx]

# Remove the solid background rect from the ascii art so it blends
inner_svg = inner_svg.replace('<rect width="100%" height="100%" fill="#0a0a0b"/>', '')

hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400" width="100%" height="400">
    <defs>
        <!-- Gradients -->
        <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#050510" />
            <stop offset="50%" stop-color="#0a0a1a" />
            <stop offset="100%" stop-color="#050510" />
        </linearGradient>
        
        <linearGradient id="accent-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#8b5cf6" />
            <stop offset="100%" stop-color="#06b6d4" />
        </linearGradient>

        <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.6"/>
            <stop offset="50%" stop-color="#222244" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#06b6d4" stop-opacity="0.6"/>
        </linearGradient>

        <!-- Glow Filters -->
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="15" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
        
        <filter id="glow-small" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>

        <!-- Decorative Patterns -->
        <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1" fill="#ffffff" opacity="0.05" />
        </pattern>
    </defs>

    <!-- Background -->
    <rect width="1000" height="400" fill="url(#bg-grad)" rx="20" />
    
    <!-- Grid Pattern -->
    <rect width="1000" height="400" fill="url(#dots)" rx="20" />

    <!-- Glowing Orbs -->
    <circle cx="150" cy="100" r="100" fill="#8b5cf6" opacity="0.12" filter="url(#glow)" />
    <circle cx="800" cy="300" r="120" fill="#06b6d4" opacity="0.08" filter="url(#glow)" />
    <circle cx="500" cy="200" r="150" fill="#ff007f" opacity="0.05" filter="url(#glow)" />

    <!-- Glowing Border -->
    <rect x="2" y="2" width="996" height="396" fill="none" stroke="url(#border-grad)" stroke-width="2" rx="18" />

    <!-- Decorative Top Left UI Elements -->
    <g transform="translate(30, 30)">
        <circle cx="0" cy="0" r="6" fill="#ff5f56" />
        <circle cx="20" cy="0" r="6" fill="#ffbd2e" />
        <circle cx="40" cy="0" r="6" fill="#27c93f" />
    </g>

    <!-- Typography Section -->
    <g transform="translate(80, 140)">
        <text x="0" y="0" font-family="'Segoe UI', system-ui, sans-serif" font-size="52" font-weight="900" fill="#ffffff" letter-spacing="3">
            HARSHIT TYAGI
        </text>
        
        <text x="0" y="45" font-family="'Segoe UI', system-ui, sans-serif" font-size="20" font-weight="600" fill="url(#accent-grad)" letter-spacing="1.5">
            SOFTWARE ENGINEER &amp; AI DEVELOPER
        </text>

        <!-- Decorative Line -->
        <rect x="0" y="70" width="60" height="4" fill="url(#accent-grad)" rx="2" />

        <text x="0" y="115" font-family="'Segoe UI', system-ui, sans-serif" font-size="16" font-weight="400" fill="#8a9a9a">
            <tspan x="0" dy="0">Building intelligent software and immersive 3D</tspan>
            <tspan x="0" dy="26">experiences through creative technology.</tspan>
        </text>
        
        <!-- Tech Stack Pills -->
        <g transform="translate(0, 175)">
            <rect x="0" y="0" width="90" height="28" fill="#1c1c2e" rx="14" stroke="#8b5cf6" stroke-opacity="0.5"/>
            <text x="45" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#d1d5db" text-anchor="middle">Full Stack</text>
            
            <rect x="100" y="0" width="130" height="28" fill="#1c1c2e" rx="14" stroke="#06b6d4" stroke-opacity="0.5"/>
            <text x="165" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#d1d5db" text-anchor="middle">WebGL &amp; Graphics</text>
            
            <rect x="240" y="0" width="90" height="28" fill="#1c1c2e" rx="14" stroke="#ff007f" stroke-opacity="0.5"/>
            <text x="285" y="18" font-family="sans-serif" font-size="12" font-weight="600" fill="#d1d5db" text-anchor="middle">AI / RAG</text>
        </g>
    </g>

    <!-- Embedded ASCII Art on the Right -->
    <g transform="translate(560, -80) scale(0.8)">
        <!-- Glow behind portrait -->
        <circle cx="303" cy="317" r="180" fill="#8b5cf6" opacity="0.15" filter="url(#glow)"/>
        {inner_svg}
    </g>
</svg>'''

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(hero_svg)

print('Hero SVG generated successfully!')
