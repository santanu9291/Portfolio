#!/usr/bin/env python3
"""
CV PDF Generator Script
This script generates a professional PDF of your CV
To use: python3 generate_pdf.py
"""

import os
from datetime import datetime

# Try to import PDF libraries
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False
    print("⚠️  reportlab not installed. Trying alternative method...")

def generate_pdf_with_reportlab():
    """Generate PDF using reportlab"""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib import colors
    
    # Create PDF
    pdf_path = "Santanu_Mondal_CV.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    # Container for PDF elements
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#1f77d2'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#1f77d2'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        borderColor=colors.HexColor('#1f77d2'),
        borderWidth=1,
        borderPadding=10
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#555555'),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        spaceAfter=6
    )
    
    # Add header
    elements.append(Paragraph("Santanu Mondal", title_style))
    elements.append(Paragraph("Game Developer & Drupal Developer", subtitle_style))
    elements.append(Paragraph("Computer Science Engineer | 4+ Years Experience", subtitle_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Profile Section
    elements.append(Paragraph("PROFILE", heading_style))
    profile_text = "Passionate Computer Science Engineer with 4+ years of hands-on experience in game development and Drupal CMS. Specialized in designing and deploying high-performance 2D mobile games and robust backend solutions. Dedicated to writing clean code, delivering innovative designs, and optimizing user experiences."
    elements.append(Paragraph(profile_text, normal_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Technical Skills Section
    elements.append(Paragraph("TECHNICAL SKILLS", heading_style))
    skills = "Unity 2D, C#, Drupal, PHP, JavaScript, SQL, Git & Github, UI/UX Design, Game Physics, REST APIs, Database Design, Performance Optimization"
    elements.append(Paragraph(skills, normal_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Experience Section
    elements.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
    
    elements.append(Paragraph("<b>Senior Game Developer</b> — Game Development (4+ Years)", normal_style))
    exp1 = """
    • Architected and shipped 2 major titles: Differences Finder and Fruitiya with 100K+ downloads<br/>
    • Implemented advanced monetization strategies including targeted ads and in-app purchases<br/>
    • Optimized game performance achieving 60 FPS on low-end devices<br/>
    • Created intuitive UI systems with smooth animations and responsive controls<br/>
    • Collaborated with designers and artists to bring game vision to life
    """
    elements.append(Paragraph(exp1, normal_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("<b>Drupal Developer</b> — Backend Development (Current)", normal_style))
    exp2 = """
    • Designed and developed custom Drupal modules for enterprise clients<br/>
    • Contributed PHPStan static analysis rules to Drupal community<br/>
    • Implemented enhanced CAPTCHA security modules for webform protection<br/>
    • Performed security audits and hardened Drupal installations<br/>
    • Mentored junior developers on Drupal best practices
    """
    elements.append(Paragraph(exp2, normal_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Education Section
    elements.append(Paragraph("EDUCATION", heading_style))
    
    elements.append(Paragraph("<b>Bachelor of Technology in Computer Science Engineering</b>", normal_style))
    elements.append(Paragraph("XYZ University (2014 - 2018) — Graduated with distinction", normal_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("<b>Game Development Certification</b>", normal_style))
    elements.append(Paragraph("Unity Academy (2019) — Advanced certification in game development", normal_style))
    elements.append(Spacer(1, 0.1*inch))
    
    elements.append(Paragraph("<b>Drupal Development Expert</b>", normal_style))
    elements.append(Paragraph("Drupal.org Community (2020 - Present) — Certified Drupal developer", normal_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Achievements Section
    elements.append(Paragraph("ACHIEVEMENTS", heading_style))
    achievements = """
    • Successfully launched 2 mobile games with combined 100,000+ downloads<br/>
    • Contributed open-source Drupal modules adopted by 5,000+ developers<br/>
    • Achieved 4.8/5 average rating across all published games<br/>
    • Improved game performance by 35% through advanced optimization techniques<br/>
    • Mentored 10+ junior developers in game and web development
    """
    elements.append(Paragraph(achievements, normal_style))
    
    # Build PDF
    doc.build(elements)
    print(f"✅ PDF created successfully: {pdf_path}")
    print(f"📁 Location: {os.path.abspath(pdf_path)}")
    return True

def create_simple_pdf():
    """Create a simple text-based PDF using basic Python (fallback method)"""
    try:
        from fpdf import FPDF
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 20)
        pdf.cell(0, 10, "Santanu Mondal", 0, 1, "C")
        
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 5, "Game Developer & Drupal Developer", 0, 1, "C")
        pdf.cell(0, 5, "Computer Science Engineer | 4+ Years Experience", 0, 1, "C")
        
        pdf.ln(5)
        
        # Profile
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 5, "PROFILE", 0, 1)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 4, "Passionate Computer Science Engineer with 4+ years of hands-on experience in game development and Drupal CMS. Specialized in designing and deploying high-performance 2D mobile games and robust backend solutions.")
        
        pdf.ln(3)
        
        # Skills
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 5, "TECHNICAL SKILLS", 0, 1)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 4, "Unity 2D, C#, Drupal, PHP, JavaScript, SQL, Git & Github, UI/UX Design, Game Physics, REST APIs, Database Design, Performance Optimization")
        
        pdf.ln(3)
        
        # Experience
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 5, "PROFESSIONAL EXPERIENCE", 0, 1)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(0, 5, "Senior Game Developer - Game Development (4+ Years)", 0, 1)
        pdf.set_font("Arial", "", 9)
        pdf.multi_cell(0, 4, "- Architected and shipped 2 major titles with 100K+ downloads\n- Implemented monetization strategies including ads and in-app purchases\n- Optimized game performance achieving 60 FPS\n- Created intuitive UI systems")
        
        pdf.ln(2)
        
        pdf.set_font("Arial", "B", 10)
        pdf.cell(0, 5, "Drupal Developer - Backend Development (Current)", 0, 1)
        pdf.set_font("Arial", "", 9)
        pdf.multi_cell(0, 4, "- Designed custom Drupal modules for enterprise clients\n- Contributed to Drupal community\n- Implemented security modules\n- Mentored junior developers")
        
        pdf.ln(3)
        
        # Education
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 5, "EDUCATION", 0, 1)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(0, 5, "Bachelor of Technology - Computer Science Engineering", 0, 1)
        pdf.set_font("Arial", "", 9)
        pdf.cell(0, 4, "XYZ University (2014 - 2018)", 0, 1)
        
        pdf.output("Santanu_Mondal_CV.pdf")
        print("✅ PDF created successfully: Santanu_Mondal_CV.pdf")
        return True
    except:
        return False

if __name__ == "__main__":
    print("🔄 Generating CV PDF...")
    print()
    
    try:
        if HAS_REPORTLAB:
            generate_pdf_with_reportlab()
        else:
            print("Attempting alternative PDF generation method...")
            if not create_simple_pdf():
                print("❌ Could not generate PDF. Please install required library:")
                print("   pip install fpdf2")
                print()
                print("Or install reportlab:")
                print("   pip install reportlab")
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        print()
        print("Installation options:")
        print("1. Using pip: pip install reportlab")
        print("2. Using apt: sudo apt-get install python3-reportlab")
