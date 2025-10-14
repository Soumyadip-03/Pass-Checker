import reflex as rx
from typing import Dict

def strength_meter(analysis: Dict) -> rx.Component:
    """Visual strength meter component"""
    score = analysis.get("score", 0)
    strength = analysis.get("strength", "Very Weak")
    
    # Color mapping
    color_map = {
        "Very Weak": "#ff4444",
        "Weak": "#ff8800", 
        "Medium": "#ffaa00",
        "Strong": "#88cc00",
        "Very Strong": "#00cc44"
    }
    
    color = color_map.get(strength, "#ff4444")
    width_percentage = min(score, 100)
    
    return rx.vstack(
        rx.hstack(
            rx.text(f"Strength: {strength}", font_weight="bold"),
            rx.text(f"Score: {score}/100", color="gray.600"),
            justify="between",
            width="100%"
        ),
        rx.box(
            rx.box(
                width=f"{width_percentage}%",
                height="100%",
                bg=color,
                border_radius="4px",
                transition="all 0.3s ease"
            ),
            width="100%",
            height="20px",
            bg="gray.200",
            border_radius="4px",
            overflow="hidden"
        ),
        width="100%",
        spacing="2"
    )

def detailed_analysis(analysis: Dict) -> rx.Component:
    """Detailed analysis breakdown"""
    basic = analysis.get("basic", {})
    zxcvbn = analysis.get("zxcvbn", {})
    patterns = analysis.get("patterns", {})
    
    return rx.vstack(
        rx.heading("Analysis Breakdown", size="5"),
        
        # Basic checks
        rx.vstack(
            rx.text("Character Requirements:", font_weight="bold"),
            rx.hstack(
                _check_item("Uppercase", basic.get("has_uppercase", False)),
                _check_item("Lowercase", basic.get("has_lowercase", False)),
                spacing="4"
            ),
            rx.hstack(
                _check_item("Numbers", basic.get("has_digits", False)),
                _check_item("Special Chars", basic.get("has_special", False)),
                spacing="4"
            ),
            spacing="2",
            align="start"
        ),
        
        # Length info
        rx.hstack(
            rx.text("Length:", font_weight="bold"),
            rx.text(f"{analysis.get('length', 0)} characters"),
            rx.text(f"Entropy: {analysis.get('entropy', 0):.1f} bits", color="gray.600"),
            spacing="2"
        ),
        
        # Crack time
        rx.hstack(
            rx.text("Estimated crack time:", font_weight="bold"),
            rx.text(zxcvbn.get("crack_time", "Unknown"), color="blue.600"),
            spacing="2"
        ) if zxcvbn.get("crack_time") else rx.box(),
        
        # Breach check
        rx.hstack(
            rx.text("Breach Status:", font_weight="bold"),
            rx.text(
                "⚠️ Found in breach database" if analysis.get("is_breached") else "✅ Not found in common breaches",
                color="red.500" if analysis.get("is_breached") else "green.500"
            ),
            spacing="2"
        ),
        
        spacing="4",
        align="start",
        width="100%"
    )

def _check_item(label: str, passed: bool) -> rx.Component:
    """Individual check item"""
    return rx.hstack(
        rx.text("✅" if passed else "❌"),
        rx.text(label, color="green.600" if passed else "red.500"),
        spacing="1"
    )

def feedback_section(feedback: list) -> rx.Component:
    """Feedback and suggestions section"""
    if not feedback:
        return rx.text("✅ Password meets all requirements!", color="green.600", font_weight="bold")
    
    return rx.vstack(
        rx.text("Suggestions for improvement:", font_weight="bold", color="orange.600"),
        rx.unordered_list(
            *[rx.list_item(suggestion) for suggestion in feedback],
            spacing="1"
        ),
        spacing="2",
        align="start"
    )