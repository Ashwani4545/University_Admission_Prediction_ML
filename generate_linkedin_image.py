#!/usr/bin/env python3
"""
Generate a professional LinkedIn post image for E-commerce Delivery Prediction project
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Image dimensions optimized for LinkedIn (1200x627 is recommended)
WIDTH = 1200
HEIGHT = 627
BACKGROUND_COLOR = (255, 255, 255)  # White
PRIMARY_COLOR = (0, 119, 181)  # LinkedIn Blue
ACCENT_COLOR = (40, 103, 178)  # Darker Blue
TEXT_COLOR = (0, 0, 0)  # Black
SECONDARY_TEXT = (100, 100, 100)  # Gray
SUCCESS_COLOR = (87, 166, 74)  # Green
RATING_COLOR = (255, 193, 7)  # Gold

def create_linkedin_post_image():
    """Create a professional LinkedIn post image"""
    
    # Create image
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Try to use system fonts, fall back to default if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        heading_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        subheading_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        heading_font = ImageFont.load_default()
        subheading_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Header bar (LinkedIn blue)
    draw.rectangle([0, 0, WIDTH, 100], fill=PRIMARY_COLOR)
    
    # Title
    title = "E-Commerce Delivery Delay Prediction"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((WIDTH - title_width) / 2, 25), title, fill=BACKGROUND_COLOR, font=title_font)
    
    # Subtitle
    subtitle = "Production-Ready ML System with Full MLOps"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=small_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(((WIDTH - subtitle_width) / 2, 75), subtitle, fill=BACKGROUND_COLOR, font=small_font)
    
    # Content area
    y_position = 130
    x_left = 50
    x_right = WIDTH // 2 + 50
    
    # Left column - Tech Stack
    draw.text((x_left, y_position), "🔧 Tech Stack", fill=ACCENT_COLOR, font=heading_font)
    y_position += 50
    
    tech_items = [
        "• FastAPI REST API",
        "• Streamlit UI",
        "• Docker + Compose",
        "• MLflow Tracking",
        "• Scikit-learn & XGBoost",
        "• Python 3.10+"
    ]
    
    for item in tech_items:
        draw.text((x_left, y_position), item, fill=TEXT_COLOR, font=text_font)
        y_position += 35
    
    # Right column - Key Features
    y_position = 130
    draw.text((x_right, y_position), "✨ Key Features", fill=ACCENT_COLOR, font=heading_font)
    y_position += 50
    
    features = [
        "✅ Binary Classification",
        "✅ Behavioral Features",
        "✅ Real-time Predictions",
        "✅ Customer Risk Scoring",
        "✅ Production Deployment",
        "✅ Health Monitoring"
    ]
    
    for feature in features:
        draw.text((x_right, y_position), feature, fill=SUCCESS_COLOR, font=text_font)
        y_position += 35
    
    # Bottom section - Rating and Stats
    y_bottom = HEIGHT - 150
    
    # Rating box
    rating_x = 50
    draw.rectangle([rating_x, y_bottom, rating_x + 350, y_bottom + 100], 
                   outline=RATING_COLOR, width=3, fill=(255, 252, 240))
    
    draw.text((rating_x + 20, y_bottom + 15), "⭐ Overall Rating", fill=TEXT_COLOR, font=subheading_font)
    draw.text((rating_x + 20, y_bottom + 50), "4.0 / 5.0", fill=RATING_COLOR, font=heading_font)
    
    # Impact box
    impact_x = rating_x + 380
    draw.rectangle([impact_x, y_bottom, impact_x + 350, y_bottom + 100], 
                   outline=SUCCESS_COLOR, width=3, fill=(240, 255, 240))
    
    draw.text((impact_x + 20, y_bottom + 15), "💼 Business Impact", fill=TEXT_COLOR, font=subheading_font)
    draw.text((impact_x + 20, y_bottom + 50), "Reduces SLA Breaches", fill=SUCCESS_COLOR, font=text_font)
    
    # Footer
    footer_y = HEIGHT - 35
    footer_text = "GitHub: Ashwani4545/E-commerce-product-delivery-prediction"
    draw.text((50, footer_y), footer_text, fill=SECONDARY_TEXT, font=small_font)
    
    # Save image
    output_path = "LINKEDIN_POST_IMAGE.png"
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ LinkedIn post image created: {output_path}")
    print(f"   Dimensions: {WIDTH}x{HEIGHT}px")
    print(f"   Optimized for LinkedIn feed")
    
    return output_path

if __name__ == "__main__":
    create_linkedin_post_image()
