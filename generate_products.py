#!/usr/bin/env python3
"""Generate 50 individual product detail HTML pages."""

products = [
    ("PurGas 4.5L N2O Whip Cream Charger", "purgas-4-5l-n2o-whip-cream-charger-box-of-1-tank", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2026/04/PURGAS4.5L-D.png", "Accessories"),
    ("PurGas 1100g N2O Whip Cream Charger", "purgas-1100g-n2o-whip-cream-charger-box-of-6-tank", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2026/04/PURGAS1.1L-D.png", "Accessories"),
    ("10\" Waterpipe - WYQ039", "10-waterpipe-wyq039", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/03/WYQ039_Default_.png", "Waterpipe"),
    ("Glass Straws", "glass-straws", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/03/WPX040_Default.png", "Accessories"),
    ("Rock Glass Regular Banger Set Display 18ct - RG1003", "rock-glass-regular-banger-set-display-18ct-rg1003", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/03/RG1003-14-90_Default_.png", "Dabbing"),
    ("Glass Sherlock Pipe - GP333", "glass-sherlock-pipe-gp333", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/03/GB333_Default_.png", "Handpipe"),
    ("Limitless 7-Hydroxy Pre-Priced $49.99 Tablets 50mg 10 Jar", "limitless-7-hydroxy-pre-priced-49-99-tablets-50mg-10-jar", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2026/04/Limitless-49.99.jpg-1.png", "Wellness"),
    ("8\" Waterpipe - WG066", "8-waterpipe-wg066", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2026/04/WCG066_Default_.png", "Waterpipe"),
    ("Waterpipe 5\" Clear - GWP5", "waterpipe-5-clear-gwp5", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2024/12/5CLEAR-WP_default.jpg", "Waterpipe"),
    ("Waterpipe 5\" - GWP244", "waterpipe-5-gwp244", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2024/03/GWP244.jpg", "Waterpipe"),
    ("Silicone Handpipe Honey Design - DZ002A", "silicone-handpipe-honey-design-dz002a", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2025/03/DZ002A-default-scaled.jpeg", "Handpipe"),
    ("Waterpipe 8\" - GWP480", "waterpipe-8-gwp480", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2024/03/Product-Edits-9.jpg", "Waterpipe"),
    ("Waterpipe 8\" Mix Color - RS240", "waterpipe-8-mix-color-rs240", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/RS240-DEFAULT-PIC.jpg", "Waterpipe"),
    ("Waterpipe 8\" - GWP479", "waterpipe-8-gwp479", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2024/03/GWP479-DEFAUT-PIC.jpg", "Waterpipe"),
    ("Waterpipe Recycler 5\" - FGP4000", "waterpipe-recycler-5-fgp4000", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2024/03/Fgp4000-default-1.jpg", "Recycler"),
    ("Waterpipe 6\" - GWP322", "waterpipe-6-gwp322", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2024/10/Gwp322-default.jpg", "Waterpipe"),
    ("Labubu Silicone Waterpipe - SRS1406", "labubu-silicone-waterpipe-srs1406", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2025/07/SRS1406-Default-1.png", "Silicone Waterpipe"),
    ("Silicone Waterpipes 4\" - SP1102P", "silicone-waterpipes-4-sp1102p", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/03/Silicone-waterpipe-4-SP1102P-8.jpg", "Silicone Waterpipe"),
    ("Silicone Waterpipes 7\" - SP1035QP", "silicone-waterpipes-7-sp1035qp", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/03/SP1035QP-8.jpg", "Silicone Waterpipe"),
    ("Waterpipe 5\" Moon on Cloud Glow in Dark - S330G", "waterpipe-5-moon-on-cloud-glow-in-dark-s330g", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2025/01/S330G_D.jpg", "Glow in Dark"),
    ("Waterpipe 5\" Batman - S342", "waterpipe-5-batman-s342", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2025/01/S342_D.jpg", "Character"),
    ("Waterpipe 5\" Mewtwo - S343", "waterpipe-5-mewtwo-s343", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2025/01/S343_D.jpg", "Character"),
    ("6\" Labubu Silicone Waterpipe - SRS1539", "6-labubu-silicone-waterpipe-srs1539", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2025/09/SRS1539-SILICONE-WP.jpg", "Silicone Waterpipe"),
    ("Silicone Waterpipe PVC Moose 7\" - H467", "silicone-waterpipe-pvc-moose-7-h467", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2025/05/H467-default-scaled.jpeg", "Silicone Waterpipe"),
    ("10\" Soft Glass Skull Glow in Dark - SG-10KU", "10-soft-glass-skull-glow-in-dark-sg-10ku", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG10KU-2.jpg", "Soft Glass"),
    ("9\" Soft Glass Eagle Glow in Dark - SG-9EA", "9-soft-glass-eagle-glow-in-dark-sg-9ea", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG9EA.jpg", "Soft Glass"),
    ("12\" Inch Soft Glass Groot Glow in Dark - SG-12T", "12-inch-soft-glass-groot-glow-in-dark-sg-12t", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG12T.jpg", "Soft Glass"),
    ("14\" Soft Glass Skull - SG-14SK", "14-soft-glass-skull-sg-14sk", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG14SK-2.jpg", "Soft Glass"),
    ("11\" Soft Glass EagleGlow in Dark - SG-11D", "11-soft-glass-eagleglow-in-dark-sg-11d", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG11D.jpg", "Soft Glass"),
    ("12\" Soft Glass Iron Man Glow in Dark - SG-12R", "12-soft-glass-iron-man-glow-in-dark-sg-12r", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG12R-2.jpg", "Soft Glass"),
    ("11\" Soft Glass FaceGlow in Dark - SG-411A", "11-soft-glass-faceglow-in-dark-sg-411a", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG11A.jpg", "Soft Glass"),
    ("16\" Soft Glass Eagle Glow in Dark - SG-16EA", "16-soft-glass-eagle-glow-in-dark-sg-16ea", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/06/SG16EA-2.jpg", "Soft Glass"),
    ("Waterpipe Soft Glass 12\" Hammer - SG12H", "waterpipe-soft-glass-12-hammer-sg12h", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/07/SG12H.jpg", "Soft Glass"),
    ("Waterpipe Soft Glass 16\" - SG15BL", "waterpipe-soft-glass-16-sg15bl", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/07/SG15BL-2.jpg", "Soft Glass"),
    ("Sherlock Colortube - A15", "sherlock-colortube-a15", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/11/A15.jpg", "Handpipe"),
    ("Wood Pipe - PI01", "wood-pipe-pi01", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/01/PI-01-Wood-Pipe-default.jpg", "Handpipe"),
    ("Sherlock Colortube - A16", "sherlock-colortube-a16", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/11/A16.jpg", "Handpipe"),
    ("Sherlock Pipe Rock Glass 6\" - R293", "sherlock-pipe-rock-glass-6-r293", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/04/Sherlock-Pipe-Rock-Glass-6_-R293.jpg", "Handpipe"),
    ("Sherlock Colortube - A10", "sherlock-colortube-a10", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/11/A10-default.jpg", "Handpipe"),
    ("Sherlock Colortube - A17", "sherlock-colortube-a17", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/11/A17-default-1.jpg", "Handpipe"),
    ("Stem Roller Rock Glass 4\" - P226", "stem-roller-rock-glass-4-p226", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/03/Steam-Roller-Rock-Glass-6-R226.jpg", "Handpipe"),
    ("Sherlock Pipe - A80", "sherlock-pipe-a80", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/03/A80-default.jpg", "Handpipe"),
    ("Regular Bowl Mix 14 mm - BWL-06", "regular-bowl-mix-14-mm-bwl-06", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/05/BwL06-14m-default.jpg", "Bowl"),
    ("Fancy Bowl Mix 14mm - BWL-01", "fancy-bowl-mix-14mm-bwl-01", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/05/Fancy-Bwl01-14m-default.jpg", "Bowl"),
    ("Heavy Bowl Mix 14mm - BWL-03", "heavy-bowl-mix-14mm-bwl-03", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/05/Hv-bowl-bwl03-14m-default.jpg", "Bowl"),
    ("Regular Bowl Mix 18 mm - BWL-07", "regular-bowl-mix-18-mm-bwl-07", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/05/Bwl07-18m-default.jpg", "Bowl"),
    ("Character Bowl Mix 14mm - BWL09", "character-bowl-mix-14mm-bwl09", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/01/Bwl09-default-.jpg", "Bowl"),
    ("Heavy Bowl Mix 18mm - BWL-04", "heavy-bowl-mix-18mm-bwl-04", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/05/Hv-bowl-bwl04-18m-default.jpg", "Bowl"),
    ("Regular Bowls 10mm - BWL08", "regular-bowls-10mm-bwl08", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2022/08/Regular-Bowl-10MM-BWL08.jpg", "Bowl"),
    ("Screen Bowl - BWL10", "screen-bowl-bwl10", "https://eadn-wc01-9311305.nxedge.io/wp-content/uploads/2023/07/BWL10-default.jpg", "Bowl"),
]

# Get related products by category
def get_related(prod_idx, category, count=4):
    related = []
    for i, (_, _, _, cat) in enumerate(products):
        if cat == category and i != prod_idx:
            related.append(i)
            if len(related) >= count:
                break
    # If not enough, fill with any products
    while len(related) < count:
        for i in range(len(products)):
            if i not in related and i != prod_idx:
                related.append(i)
                if len(related) >= count:
                    break
    return related[:count]

def generate_product_page(name, slug, image_url, category, prod_idx):
    related = get_related(prod_idx, category)

    page_content = f'''<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>{name} | Glass House Distro</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <script>
      tailwind.config = {{
        darkMode: "class",
        theme: {{
          extend: {{
            "colors": {{
                "on-surface-variant": "#a0b4c4",
                "surface-variant": "#1a2438",
                "secondary": "#88b4cc",
                "background": "#0a0e1a",
                "secondary-container": "#1a3a4e",
                "primary-fixed": "#c8eaff",
                "on-primary": "#001f2e",
                "on-surface": "#e0e8f0",
                "surface-tint": "#7dd3fc",
                "tertiary": "#c8a0f0",
                "on-primary-fixed": "#001f2e",
                "inverse-on-surface": "#0a0e1a",
                "tertiary-container": "#3d2060",
                "surface-container-high": "#1a2438",
                "on-secondary": "#001f2e",
                "on-primary-fixed-variant": "#004d73",
                "surface": "#0f1524",
                "surface-dim": "#0f1524",
                "tertiary-fixed-dim": "#c8a0f0",
                "surface-container": "#141c2e",
                "on-tertiary": "#1a002e",
                "surface-container-highest": "#202c42",
                "on-tertiary-fixed-variant": "#4d2a73",
                "secondary-fixed-dim": "#88b4cc",
                "inverse-surface": "#e0e8f0",
                "error": "#ff6b6b",
                "on-error": "#1a0000",
                "primary-container": "#0e4d6e",
                "surface-container-lowest": "#0a0e1a",
                "error-container": "#3d1414",
                "secondary-fixed": "#c0d8e8",
                "on-background": "#e0e8f0",
                "surface-bright": "#1a2438",
                "surface-container-low": "#111828",
                "primary-fixed-dim": "#7dd3fc",
                "on-tertiary-container": "#e8d0ff",
                "on-secondary-fixed-variant": "#2a4a5e",
                "inverse-primary": "#0a4c6e",
                "on-error-container": "#ffb3b3",
                "outline-variant": "#2a3a48",
                "outline": "#4a6070",
                "on-primary-container": "#c8eaff",
                "on-secondary-fixed": "#0d1f2b",
                "on-secondary-container": "#c0d8e8",
                "tertiary-fixed": "#e8d0ff",
                "primary": "#7dd3fc",
                "on-tertiary-fixed": "#1a002e"
            }},
            "fontFamily": {{
                "headline": ["Inter"],
                "body": ["Inter"],
                "label": ["Inter"]
            }}
          }},
        }},
      }}
    </script>
    <style>
        .glass-panel {{
            background: rgba(15, 21, 36, 0.6);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(125, 211, 252, 0.1);
        }}
        .glass-panel-elevated {{
            background: rgba(15, 21, 36, 0.75);
            backdrop-filter: blur(24px);
            border: 1px solid rgba(125, 211, 252, 0.15);
        }}
        .material-symbols-outlined {{
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }}
    </style>
</head>
<body class="bg-background text-on-surface font-body selection:bg-primary/30">
    <!-- TopNavBar -->
    <nav class="fixed top-0 w-full bg-slate-950/60 backdrop-blur-xl border-b border-sky-400/10 shadow-[0_0_30px_rgba(125,211,252,0.05)] z-50">
        <div class="flex justify-between items-center w-full px-8 py-4 max-w-screen-2xl mx-auto">
            <a href="../index.html" class="text-2xl font-semibold tracking-tighter text-sky-300 font-headline">Glass House Distro</a>
            <div class="hidden md:flex items-center space-x-8 font-inter tracking-tight">
                <a class="text-slate-400 hover:text-sky-200 transition-colors duration-300 cursor-pointer active:scale-95" href="../index.html">Wholesale</a>
                <a class="text-slate-400 hover:text-sky-200 transition-colors duration-300 cursor-pointer active:scale-95" href="../products.html">Catalog</a>
                <a class="text-slate-400 hover:text-sky-200 transition-colors duration-300 cursor-pointer active:scale-95" href="../contact.html">Contact</a>
            </div>
            <div class="flex items-center space-x-4">
                <button class="text-slate-400 hover:text-sky-200 font-medium px-4 py-2 transition-all">Sign In</button>
                <button class="bg-primary/10 border border-primary/20 text-primary px-6 py-2 rounded-lg font-semibold hover:bg-primary/20 transition-all active:scale-95">Open Account</button>
            </div>
        </div>
    </nav>

    <main class="pt-28 pb-20 px-8 max-w-screen-2xl mx-auto">
        <!-- Breadcrumb -->
        <div class="mb-6 text-sm">
            <a href="../products.html" class="text-on-surface-variant hover:text-primary transition-colors">Catalog</a>
            <span class="text-on-surface-variant mx-2">/</span>
            <a href="../products.html" class="text-on-surface-variant hover:text-primary transition-colors">{category}</a>
            <span class="text-on-surface-variant mx-2">/</span>
            <span class="text-primary">{name}</span>
        </div>

        <!-- Hero Section -->
        <div class="glass-panel-elevated rounded-3xl p-8 mb-12">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <!-- Product Image -->
                <div class="relative rounded-2xl overflow-hidden bg-surface-container">
                    <img src="{image_url}" alt="{name}" class="w-full h-auto object-cover" loading="eager"/>
                </div>

                <!-- Product Info -->
                <div class="space-y-6">
                    <div>
                        <span class="inline-block bg-primary/20 backdrop-blur-md text-primary px-4 py-1.5 rounded-full text-xs font-bold tracking-widest uppercase border border-primary/30 mb-4">{category}</span>
                        <h1 class="text-4xl font-bold tracking-tight text-on-surface leading-tight">{name}</h1>
                    </div>

                    <div class="flex flex-wrap gap-4 text-sm text-on-surface-variant">
                        <div class="flex items-center gap-2">
                            <span class="material-symbols-outlined text-primary text-lg">verified</span>
                            <span>In Stock</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="material-symbols-outlined text-primary text-lg">local_shipping</span>
                            <span>Ships Nationwide</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="material-symbols-outlined text-primary text-lg">inventory_2</span>
                            <span>Wholesale Only</span>
                        </div>
                    </div>

                    <p class="text-on-surface-variant leading-relaxed">
                        Premium quality {name.lower()} from Glass House Distro. This professional-grade product is designed for wholesale distribution and retail ready. Contact us for bulk pricing and availability.
                    </p>

                    <div class="glass-panel rounded-xl p-4">
                        <p class="text-sm text-on-surface-variant mb-1">Wholesale Pricing</p>
                        <p class="text-2xl font-bold text-primary italic">Login to see wholesale pricing</p>
                        <p class="text-xs text-on-surface-variant mt-1">Create an account or sign in to view tiered wholesale pricing</p>
                    </div>

                    <div class="flex flex-wrap gap-4 pt-4">
                        <button class="flex-1 bg-primary text-on-primary px-8 py-4 rounded-xl font-bold hover:bg-primary/90 transition-all active:scale-95 flex items-center justify-center gap-2">
                            <span class="material-symbols-outlined">add_shopping_cart</span>
                            Add to Quote
                        </button>
                        <a href="../products.html" class="flex items-center justify-center gap-2 bg-surface-container border border-outline-variant text-on-surface px-8 py-4 rounded-xl font-semibold hover:bg-surface-variant transition-all active:scale-95">
                            <span class="material-symbols-outlined">visibility</span>
                            View Full Catalog
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Product Details -->
        <div class="grid md:grid-cols-3 gap-6 mb-12">
            <div class="glass-panel rounded-xl p-6 text-center">
                <span class="material-symbols-outlined text-primary text-3xl mb-3">workspace_premium</span>
                <h3 class="font-semibold text-on-surface mb-1">Verified Quality</h3>
                <p class="text-sm text-on-surface-variant">Every product inspected for quality assurance before shipping</p>
            </div>
            <div class="glass-panel rounded-xl p-6 text-center">
                <span class="material-symbols-outlined text-primary text-3xl mb-3">local_shipping</span>
                <h3 class="font-semibold text-on-surface mb-1">Secure Logistics</h3>
                <p class="text-sm text-on-surface-variant">Discreet, secure shipping with tracking on all orders</p>
            </div>
            <div class="glass-panel rounded-xl p-6 text-center">
                <span class="material-symbols-outlined text-primary text-3xl mb-3">handshake</span>
                <h3 class="font-semibold text-on-surface mb-1">B2B Scalability</h3>
                <p class="text-sm text-on-surface-variant">Grow your business with tiered wholesale pricing</p>
            </div>
        </div>

        <!-- Related Products -->
        <div class="mb-12">
            <h2 class="text-2xl font-bold text-on-surface mb-6">Related Products</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
'''

    for ridx in related:
        rname, rslug, rimage, rcat = products[ridx]
        related_card = f'''                <a href="{rslug}.html" class="glass-panel rounded-xl overflow-hidden group cursor-pointer">
                    <div class="h-48 overflow-hidden relative">
                        <img src="{rimage}" alt="{rname}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"/>
                    </div>
                    <div class="p-4">
                        <span class="text-[10px] text-secondary font-medium tracking-wide uppercase">{rcat}</span>
                        <h3 class="text-sm font-semibold text-on-surface leading-snug mt-1">{rname}</h3>
                    </div>
                </a>
'''
        page_content += related_card

    page_content += '''            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 border-t border-slate-900 w-full py-12">
        <div class="flex flex-col md:flex-row justify-between items-center px-12 w-full max-w-screen-2xl mx-auto font-inter text-xs text-slate-500">
            <div class="mb-8 md:mb-0">
                <a href="../index.html" class="text-lg font-bold text-slate-300 mb-2 block">Glass House Distro</a>
                <p>© 2025 Glass House Distro. Wholesale Only.</p>
            </div>
            <div class="flex flex-wrap justify-center gap-8">
                <a class="hover:text-sky-300 transition-colors" href="../terms.html">Terms of Service</a>
                <a class="hover:text-sky-300 transition-colors" href="../shipping.html">Shipping Policy</a>
                <a class="hover:text-sky-300 transition-colors" href="../compliance.html">Compliance</a>
                <a class="hover:text-sky-300 transition-colors" href="../contact.html">Contact Us</a>
            </div>
            <div class="mt-8 md:mt-0 flex items-center gap-4">
                <a href="https://glasshousedistro.com/" target="_blank" class="w-8 h-8 rounded-full glass-panel flex items-center justify-center text-on-surface-variant hover:text-primary transition-all">
                    <span class="material-symbols-outlined text-sm">language</span>
                </a>
                <a href="mailto:glasshousedistributors@gmail.com" class="w-8 h-8 rounded-full glass-panel flex items-center justify-center text-on-surface-variant hover:text-primary transition-all">
                    <span class="material-symbols-outlined text-sm">mail</span>
                </a>
            </div>
        </div>
    </footer>

    <!-- FAB Chat Button -->
    <div class="fixed bottom-8 right-8 z-40">
        <button class="flex items-center gap-3 bg-primary text-on-primary px-6 py-4 rounded-2xl font-bold shadow-2xl hover:scale-105 active:scale-95 transition-all">
            <span class="material-symbols-outlined">chat</span>
            <span>Get Quote</span>
        </button>
    </div>
</body>
</html>'''

    return page_content

# Generate all 50 pages
output_dir = "/home/divanshu/Project/glasshouse/products"

for idx, (name, slug, image_url, category) in enumerate(products):
    content = generate_product_page(name, slug, image_url, category, idx)
    filepath = f"{output_dir}/{slug}.html"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Generated {idx+1}/50: {slug}.html")

print("\nAll 50 product pages generated successfully!")

# Also regenerate data/products.js from the same product list
import os
import json

new_products_list = []
for i, (name, slug, image_url, category) in enumerate(products):
    new_products_list.append({
        "name": name,
        "slug": slug,
        "image": image_url,
        "category": category,
        "isNew": i < 2
    })

js_content = "window.PRODUCTS = " + json.dumps(new_products_list, indent=2, ensure_ascii=False) + ";\n"

data_dir = os.path.join(os.path.dirname(output_dir), "data")
os.makedirs(data_dir, exist_ok=True)
js_path = os.path.join(data_dir, "products.js")
with open(js_path, "w") as f:
    f.write(js_content)

print(f"Regenerated data/products.js with {len(new_products_list)} products.")
