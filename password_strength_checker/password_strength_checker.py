import reflex as rx
from .utils.password_analyzer import PasswordAnalyzer, PasswordGenerator

class State(rx.State):
    """Main application state"""
    password: str = ""
    score: int = 0
    strength: str = "Very Weak"
    feedback: list = []
    generated_password: str = ""
    
    def analyze_password(self, password: str):
        """Analyze password strength"""
        self.password = password
        if password:
            analyzer = PasswordAnalyzer()
            analysis = analyzer.analyze_comprehensive(password)
            self.score = int(analysis.get("score", 0))
            self.strength = analysis.get("strength", "Very Weak")
            self.feedback = analysis.get("feedback", [])
        else:
            self.score = 0
            self.strength = "Very Weak"
            self.feedback = []
    
    def generate_password(self):
        """Generate new password"""
        generator = PasswordGenerator()
        self.generated_password = generator.generate(length=12)

def strength_meter() -> rx.Component:
    """Visual strength meter"""
    return rx.vstack(
        rx.hstack(
            rx.text(f"Strength: {State.strength}", font_weight="bold"),
            rx.text(f"Score: {State.score}/100", color="gray.600"),
            justify="between",
            width="100%"
        ),
        rx.progress(value=State.score, width="100%"),
        width="100%",
        spacing="2"
    )

def feedback_section() -> rx.Component:
    """Feedback section"""
    return rx.cond(
        State.feedback.length() > 0,
        rx.vstack(
            rx.text("Suggestions:", font_weight="bold", color="orange.600"),
            rx.foreach(
                State.feedback,
                lambda suggestion: rx.text(f"• {suggestion}")
            ),
            spacing="2",
            align="start"
        ),
        rx.text("✅ Password meets requirements!", color="green.600", font_weight="bold")
    )

def index() -> rx.Component:
    """Main page"""
    return rx.container(
        rx.vstack(
            # Header
            rx.heading("🔐 Password Strength Checker", size="8", text_align="center"),
            
            # Password input
            rx.vstack(
                rx.heading("Enter Password", size="6"),
                rx.input(
                    placeholder="Enter your password...",
                    type_="password",
                    value=State.password,
                    on_change=State.analyze_password,
                    width="100%"
                ),
                rx.cond(
                    State.password != "",
                    rx.vstack(
                        strength_meter(),
                        feedback_section(),
                        spacing="4",
                        width="100%"
                    )
                ),
                spacing="4",
                width="100%"
            ),
            
            # Password Generator
            rx.vstack(
                rx.heading("Password Generator", size="6"),
                rx.button(
                    "Generate Secure Password",
                    on_click=State.generate_password,
                    width="100%"
                ),
                rx.cond(
                    State.generated_password != "",
                    rx.vstack(
                        rx.text("Generated Password:", font_weight="bold"),
                        rx.input(
                            value=State.generated_password,
                            is_read_only=True,
                            width="100%"
                        ),
                        spacing="2",
                        width="100%"
                    )
                ),
                spacing="4",
                width="100%"
            ),
            
            # Security Tips
            rx.vstack(
                rx.heading("🛡️ Security Tips", size="6"),
                rx.vstack(
                    rx.text("✅ Use at least 12 characters"),
                    rx.text("✅ Mix uppercase, lowercase, numbers, and symbols"),
                    rx.text("✅ Avoid personal information"),
                    rx.text("✅ Use unique passwords for each account"),
                    spacing="2",
                    align="start"
                ),
                spacing="3",
                width="100%"
            ),
            
            spacing="8",
            width="100%",
            max_width="600px",
            padding="4"
        ),
        center_content=True
    )

# Create the app
app = rx.App()
app.add_page(index, route="/")

if __name__ == "__main__":
    app.compile()