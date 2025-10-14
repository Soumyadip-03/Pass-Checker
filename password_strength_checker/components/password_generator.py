import reflex as rx
from ..utils.password_analyzer import PasswordGenerator

class GeneratorState(rx.State):
    """State for password generator"""
    generated_password: str = ""
    length: int = 12
    use_uppercase: bool = True
    use_lowercase: bool = True
    use_digits: bool = True
    use_special: bool = True
    exclude_ambiguous: bool = True
    
    def generate_password(self):
        """Generate new password with current settings"""
        generator = PasswordGenerator()
        self.generated_password = generator.generate(
            length=self.length,
            use_uppercase=self.use_uppercase,
            use_lowercase=self.use_lowercase,
            use_digits=self.use_digits,
            use_special=self.use_special,
            exclude_ambiguous=self.exclude_ambiguous
        )
    
    def copy_to_clipboard(self):
        """Copy generated password to clipboard"""
        return rx.set_clipboard(self.generated_password)

def password_generator() -> rx.Component:
    """Password generator component"""
    return rx.vstack(
        rx.heading("Password Generator", size="6"),
        
        # Length slider
        rx.vstack(
            rx.hstack(
                rx.text("Length:", font_weight="bold"),
                rx.text(GeneratorState.length),
                justify="between",
                width="100%"
            ),
            rx.slider(
                rx.slider_track(
                    rx.slider_filled_track()
                ),
                rx.slider_thumb(),
                value=GeneratorState.length,
                on_change=GeneratorState.set_length,
                min_=4,
                max_=50,
                step=1,
                width="100%"
            ),
            spacing="2",
            width="100%"
        ),
        
        # Character type checkboxes
        rx.vstack(
            rx.text("Character Types:", font_weight="bold"),
            rx.checkbox(
                "Uppercase Letters (A-Z)",
                is_checked=GeneratorState.use_uppercase,
                on_change=GeneratorState.set_use_uppercase
            ),
            rx.checkbox(
                "Lowercase Letters (a-z)",
                is_checked=GeneratorState.use_lowercase,
                on_change=GeneratorState.set_use_lowercase
            ),
            rx.checkbox(
                "Numbers (0-9)",
                is_checked=GeneratorState.use_digits,
                on_change=GeneratorState.set_use_digits
            ),
            rx.checkbox(
                "Special Characters (!@#$%^&*)",
                is_checked=GeneratorState.use_special,
                on_change=GeneratorState.set_use_special
            ),
            rx.checkbox(
                "Exclude Ambiguous Characters (0,O,l,1,I)",
                is_checked=GeneratorState.exclude_ambiguous,
                on_change=GeneratorState.set_exclude_ambiguous
            ),
            spacing="2",
            align="start"
        ),
        
        # Generate button
        rx.button(
            "Generate Password",
            on_click=GeneratorState.generate_password,
            bg="blue.500",
            color="white",
            size="3",
            width="100%"
        ),
        
        # Generated password display
        rx.cond(
            GeneratorState.generated_password != "",
            rx.vstack(
                rx.text("Generated Password:", font_weight="bold"),
                rx.hstack(
                    rx.input(
                        value=GeneratorState.generated_password,
                        is_read_only=True,
                        font_family="monospace",
                        font_size="3",
                        flex="1"
                    ),
                    rx.button(
                        "📋 Copy",
                        on_click=GeneratorState.copy_to_clipboard,
                        size="2"
                    ),
                    width="100%"
                ),
                spacing="2",
                width="100%"
            )
        ),
        
        spacing="6",
        width="100%",
        max_width="500px"
    )