import reflex as rx
from .utils.password_analyzer import PasswordAnalyzer, PasswordGenerator

class State(rx.State):
    """Enhanced application state"""
    password: str = ""
    score: int = 0
    strength: str = "Very Weak"
    feedback: list = []
    generated_password: str = ""
    show_password: bool = False
    dark_mode: bool = True
    
    # Generator settings
    password_length: int = 16
    use_uppercase: bool = True
    use_lowercase: bool = True
    use_numbers: bool = True
    use_symbols: bool = True
    
    # Advanced analysis
    entropy: float = 0.0
    crack_time: str = ""
    patterns_found: list = []
    nist_compliant: bool = False
    
    # History
    password_history: list[dict] = []
    password_count: int = 0
    
    def analyze_password(self, password: str):
        """Enhanced password analysis"""
        self.password = password
        
        if password:
            analyzer = PasswordAnalyzer()
            analysis = analyzer.analyze_comprehensive(password)
            
            self.score = int(analysis.get("score", 0))
            self.strength = analysis.get("strength", "Very Weak")
            self.feedback = analysis.get("feedback", [])            
            self.entropy = analysis.get("entropy", 0.0)
            self.crack_time = analysis.get("zxcvbn", {}).get("crack_time", "Unknown")
            self.patterns_found = analysis.get("patterns", {}).get("issues", [])
            self.nist_compliant = self._check_nist_compliance(password)
            
            # Add to history (last 10 analyses)
            self.password_count += 1
            if len(self.password_history) >= 10:
                self.password_history.pop(0)
            self.password_history.append({
                "score": self.score,
                "strength": self.strength,
                "length": len(password),
                "timestamp": f"Password {self.password_count}"
            })
        else:
            self._reset_analysis()
    
    def generate_password(self):
        """Generate password with custom settings"""
        if not (self.use_uppercase or self.use_lowercase or self.use_numbers or self.use_symbols):
            self.generated_password = "⚠️ Please select at least one character type"
            return
        
        generator = PasswordGenerator()
        self.generated_password = generator.generate(
            length=self.password_length,
            use_uppercase=self.use_uppercase,
            use_lowercase=self.use_lowercase,
            use_digits=self.use_numbers,
            use_special=self.use_symbols
        )
        
        if self.generated_password and "⚠️" not in self.generated_password:
            self.analyze_password(self.generated_password)
    
    def toggle_password_visibility(self):
        self.show_password = not self.show_password
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
    
    def copy_to_clipboard(self, text: str):
        return rx.set_clipboard(text)
    
    def increase_length(self):
        if self.password_length < 50:
            self.password_length += 1
    
    def decrease_length(self):
        if self.password_length > 8:
            self.password_length -= 1
    
    def _check_nist_compliance(self, password: str) -> bool:
        if len(password) < 8:
            return False
        common_passwords = ["password", "123456", "123456789", "qwerty", "abc123", "password123", "admin", "letmein", "welcome", "monkey"]
        if password.lower() in common_passwords:
            return False
        if len(set(password)) < 4:
            return False
        return True
    
    def _reset_analysis(self):
        self.score = 0
        self.strength = "Very Weak"
        self.feedback = []
        self.entropy = 0.0
        self.crack_time = ""
        self.patterns_found = []
        self.nist_compliant = False
    
    def set_use_uppercase(self, value: bool):
        self.use_uppercase = value
    
    def set_use_lowercase(self, value: bool):
        self.use_lowercase = value
    
    def set_use_numbers(self, value: bool):
        self.use_numbers = value
    
    def set_use_symbols(self, value: bool):
        self.use_symbols = value

def modern_card(*children, **props) -> rx.Component:
    """Ultra-modern rectangular glassmorphism card with theme support"""
    return rx.box(
        *children,
        style={
            "background": rx.cond(
                State.dark_mode,
                "rgba(255, 255, 255, 0.05)",
                "rgba(255, 255, 255, 0.8)"
            ),
            "backdrop_filter": "blur(20px)",
            "border": rx.cond(
                State.dark_mode,
                "1px solid rgba(255, 255, 255, 0.1)",
                "1px solid rgba(0, 0, 0, 0.1)"
            ),
            "border_radius": "16px",
            "padding": "30px",
            "box_shadow": rx.cond(
                State.dark_mode,
                "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
                "0 25px 50px -12px rgba(0, 0, 0, 0.15)"
            ),
            "transition": "all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
            "width": "100%",
            "max_width": "600px",
            "margin": "0 auto",
            "_hover": {
                "transform": "translateY(-8px)",
                "box_shadow": rx.cond(
                    State.dark_mode,
                    "0 35px 70px -12px rgba(0, 0, 0, 0.35)",
                    "0 35px 70px -12px rgba(0, 0, 0, 0.25)"
                ),
                "background": rx.cond(
                    State.dark_mode,
                    "rgba(255, 255, 255, 0.08)",
                    "rgba(255, 255, 255, 0.9)"
                )
            }
        },
        **props
    )

def animated_input(placeholder: str, value: str, on_change, input_type: str = "text") -> rx.Component:
    """Modern rectangular animated input field"""
    return rx.box(
        rx.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            type_=input_type,
            style={
                "width": "100%",
                "height": "56px",  # Slightly more rectangular
                "background": rx.cond(
                    State.dark_mode,
                    "rgba(15, 15, 35, 0.8)",
                    "rgba(255, 255, 255, 0.9)"
                ),
                "border": rx.cond(
                    State.dark_mode,
                    "2px solid rgba(255, 255, 255, 0.1)",
                    "2px solid rgba(0, 0, 0, 0.1)"
                ),
                "border_radius": "12px",
                "padding": "16px 20px",
                "font_size": "16px",
                "color": rx.cond(State.dark_mode, "white", "#1a202c"),
                "font_family": "'SF Pro Display', -apple-system, sans-serif",
                "transition": "all 0.3s ease",
                "_focus": {
                    "border_color": "#667eea",
                    "box_shadow": "0 0 0 4px rgba(102, 126, 234, 0.2)",
                    "background": rx.cond(
                        State.dark_mode,
                        "rgba(15, 15, 35, 0.9)",
                        "rgba(255, 255, 255, 1.0)"
                    )
                },
                "_placeholder": {
                    "color": rx.cond(State.dark_mode, "rgba(255, 255, 255, 0.5)", "rgba(0, 0, 0, 0.5)")
                }
            }
        ),
        style={
            "position": "relative",
            "width": "100%"
        }
    )

def modern_switch(is_checked, on_change, label: str) -> rx.Component:
    """Premium rectangular animated switch"""
    return rx.hstack(
        rx.box(
            rx.box(
                style={
                    "width": "24px",
                    "height": "24px",
                    "background": "white",
                    "border_radius": "6px",  # More rectangular thumb
                    "transform": rx.cond(is_checked, "translateX(28px)", "translateX(4px)"),
                    "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                    "box_shadow": "0 2px 8px rgba(0,0,0,0.15)"
                }
            ),
            on_click=on_change,
            style={
                "width": "56px",
                "height": "32px",
                "background": rx.cond(
                    is_checked, 
                    "linear-gradient(135deg, #10b981, #059669)",
                    "linear-gradient(135deg, #374151, #1f2937)"
                ),
                "border_radius": "8px",  # More rectangular track
                "cursor": "pointer",
                "transition": "all 0.3s ease",
                "position": "relative",
                "display": "flex",
                "align_items": "center"
            }
        ),
        rx.text(
            label,
            style={
                "color": rx.cond(State.dark_mode, "rgba(255,255,255,0.9)", "rgba(0,0,0,0.9)"),
                "font_weight": "600",
                "font_size": "15px"
            }
        ),
        align="center",
        spacing="4"
    )

def strength_meter() -> rx.Component:
    """Modern strength meter with security tips"""
    return modern_card(
        rx.vstack(
            rx.hstack(
                rx.text(
                    "Password Strength",
                    style={
                        "background": "linear-gradient(135deg, #667eea, #764ba2)",
                        "background_clip": "text",
                        "color": "transparent",
                        "font_size": "24px",
                        "font_weight": "700"
                    }
                ),
                rx.text(
                    f"{State.score}%",
                    style={
                        "color": "#10b981",
                        "font_size": "32px",
                        "font_weight": "800"
                    }
                ),
                justify="between",
                width="100%"
            ),
            
            # Progress bar
            rx.box(
                rx.box(
                    style={
                        "width": f"{State.score}%",
                        "height": "100%",
                        "background": "linear-gradient(90deg, #10b981, #059669)",
                        "border_radius": "12px",
                        "transition": "all 1s ease"
                    }
                ),
                style={
                    "width": "100%",
                    "height": "16px",
                    "background": "rgba(255,255,255,0.1)",
                    "border_radius": "12px",
                    "overflow": "hidden"
                }
            ),
            
            rx.hstack(
                rx.text(
                    f"Strength: {State.strength}",
                    style={
                        "color": rx.cond(State.dark_mode, "white", "#1a202c"), 
                        "font_weight": "600"
                    }
                ),
                rx.text(
                    f"Entropy: {State.entropy:.1f} bits",
                    style={"color": "#a855f7", "font_size": "14px"}
                ),
                justify="between",
                width="100%"
            ),
            
            # Security Tips
            rx.cond(
                State.score < 80,
                rx.box(
                    rx.text(
                        "Security Tips:",
                        style={
                            "color": rx.cond(State.dark_mode, "white", "#1a202c"),
                            "font_weight": "600",
                            "font_size": "14px",
                            "margin_bottom": "8px"
                        }
                    ),
                    rx.text(
                        rx.cond(
                            State.score < 40,
                            "• Use 12+ characters • Mix uppercase & lowercase • Add numbers & symbols",
                            "• Consider adding more special characters • Avoid common patterns"
                        ),
                        style={
                            "color": rx.cond(State.dark_mode, "rgba(255,255,255,0.8)", "rgba(0,0,0,0.8)"),
                            "font_size": "12px",
                            "line_height": "1.4"
                        }
                    ),
                    style={
                        "background": "rgba(102, 126, 234, 0.1)",
                        "border_radius": "8px",
                        "padding": "12px",
                        "margin_top": "12px"
                    }
                )
            ),
            
            spacing="6",
            width="100%"
        )
    )

def password_history() -> rx.Component:
    """Password history tracking component"""
    return rx.cond(
        State.password_history.length() > 0,
        modern_card(
            rx.vstack(
                rx.text(
                    "Password History",
                    style={
                        "background": "linear-gradient(135deg, #667eea, #764ba2)",
                        "background_clip": "text",
                        "color": "transparent",
                        "font_size": "20px",
                        "font_weight": "700"
                    }
                ),
                
                rx.vstack(
                    rx.foreach(
                        State.password_history,
                        lambda item: rx.hstack(
                            rx.text(
                                item["timestamp"],
                                style={
                                    "color": rx.cond(State.dark_mode, "rgba(255,255,255,0.7)", "rgba(0,0,0,0.7)"),
                                    "font_size": "12px",
                                    "width": "80px"
                                }
                            ),
                            rx.text(
                                f"{item['score']}%",
                                style={
                                    "color": "#60a5fa",
                                    "font_weight": "600",
                                    "font_size": "12px",
                                    "width": "40px"
                                }
                            ),
                            rx.text(
                                item["strength"],
                                style={
                                    "color": rx.cond(State.dark_mode, "rgba(255,255,255,0.8)", "rgba(0,0,0,0.8)"),
                                    "font_size": "12px",
                                    "flex": "1"
                                }
                            ),
                            justify="start",
                            align="center",
                            width="100%",
                            style={"padding": "4px 0"}
                        )
                    ),
                    spacing="1",
                    width="100%"
                ),
                
                spacing="4",
                width="100%"
            )
        )
    )

def password_analyzer() -> rx.Component:
    """Modern password analyzer"""
    return modern_card(
        rx.vstack(
            rx.text(
                "Password Analyzer",
                style={
                    "background": "linear-gradient(135deg, #667eea, #764ba2)",
                    "background_clip": "text",
                    "color": "transparent",
                    "font_size": "28px",
                    "font_weight": "700"
                }
            ),
            
            animated_input(
                "Enter your password...",
                State.password,
                State.analyze_password,
                "password"
            ),
            
            rx.cond(
                State.password != "",
                strength_meter()
            ),
            
            spacing="8",
            width="100%"
        )
    )

def password_generator() -> rx.Component:
    """Modern password generator"""
    return modern_card(
        rx.vstack(
            rx.text(
                "Password Generator",
                style={
                    "background": "linear-gradient(135deg, #667eea, #764ba2)",
                    "background_clip": "text",
                    "color": "transparent",
                    "font_size": "28px",
                    "font_weight": "700"
                }
            ),
            
            # Length control
            rx.vstack(
                rx.hstack(
                    rx.text("Length", style={
                        "color": rx.cond(State.dark_mode, "white", "#1a202c"), 
                        "font_weight": "600", 
                        "font_size": "18px"
                    }),
                    rx.text(
                        State.password_length,
                        style={
                            "color": "#60a5fa",
                            "font_weight": "800",
                            "font_size": "24px"
                        }
                    ),
                    justify="between",
                    width="100%"
                ),
                
                rx.hstack(
                    rx.button(
                        "−",
                        on_click=State.decrease_length,
                        style={
                            "width": "44px",
                            "height": "44px",
                            "background": "linear-gradient(135deg, #ef4444, #dc2626)",
                            "border": "none",
                            "border_radius": "8px",  # More rectangular
                            "color": "white",
                            "font_size": "20px",
                            "cursor": "pointer"
                        }
                    ),
                    
                    rx.text(
                        f"{State.password_length} characters",
                        style={
                            "color": "white", 
                            "font_weight": "500", 
                            "text_align": "center", 
                            "flex": "1"
                        }
                    ),
                    
                    rx.button(
                        "+",
                        on_click=State.increase_length,
                        style={
                            "width": "44px",
                            "height": "44px",
                            "background": "linear-gradient(135deg, #10b981, #059669)",
                            "border": "none",
                            "border_radius": "8px",  # More rectangular
                            "color": "white",
                            "font_size": "20px",
                            "cursor": "pointer"
                        }
                    ),
                    
                    width="100%",
                    align="center"
                ),
                
                spacing="4",
                width="100%"
            ),
            
            # Character type switches
            rx.vstack(
                rx.text(
                    "Character Types",
                    style={
                        "color": rx.cond(State.dark_mode, "white", "#1a202c"),
                        "font_size": "20px",
                        "font_weight": "600"
                    }
                ),
                
                rx.vstack(
                    modern_switch(State.use_uppercase, lambda: State.set_use_uppercase(~State.use_uppercase), "Uppercase Letters"),
                    modern_switch(State.use_lowercase, lambda: State.set_use_lowercase(~State.use_lowercase), "Lowercase Letters"),
                    modern_switch(State.use_numbers, lambda: State.set_use_numbers(~State.use_numbers), "Numbers"),
                    modern_switch(State.use_symbols, lambda: State.set_use_symbols(~State.use_symbols), "Special Symbols"),
                    spacing="5",
                    width="100%"
                ),
                
                spacing="5",
                align="start"
            ),
            
            # Generate button - More rectangular
            rx.button(
                rx.text("Generate Secure Password", style={"font_weight": "700", "font_size": "16px"}),
                on_click=State.generate_password,
                style={
                    "width": "100%",
                    "height": "56px",  # More rectangular height
                    "background": "linear-gradient(135deg, #667eea, #764ba2)",
                    "border": "none",
                    "border_radius": "12px",  # Less rounded
                    "color": "white",
                    "cursor": "pointer",
                    "transition": "all 0.4s ease",
                    "_hover": {
                        "transform": "translateY(-2px)",
                        "box_shadow": "0 12px 32px rgba(102, 126, 234, 0.4)"
                    }
                }
            ),
            
            # Generated password display
            rx.cond(
                State.generated_password != "",
                rx.vstack(
                    rx.text(
                        "Generated Password",
                        style={
                        "color": rx.cond(State.dark_mode, "white", "#1a202c"), 
                        "font_weight": "600", 
                        "font_size": "18px"
                    }
                    ),
                    
                    rx.hstack(
                        rx.input(
                            value=State.generated_password,
                            is_read_only=True,
                            style={
                                "width": "100%",
                                "height": "56px",
                                "background": "rgba(255,255,255,0.05)",
                                "border": "2px solid rgba(255,255,255,0.1)",
                                "border_radius": "12px",
                                "padding": "16px",
                                "color": "white",
                                "font_family": "monospace",
                                "font_size": "16px"
                            }
                        ),
                        
                        rx.button(
                            "Copy",
                            on_click=lambda: State.copy_to_clipboard(State.generated_password),
                            style={
                                "width": "52px",
                                "height": "52px",
                                "background": "linear-gradient(135deg, #10b981, #059669)",
                                "border": "none",
                                "border_radius": "8px",  # More rectangular
                                "font_size": "18px",
                                "cursor": "pointer"
                            }
                        ),
                        
                        spacing="3",
                        width="100%"
                    ),
                    
                    spacing="4",
                    width="100%"
                )
            ),
            
            spacing="8",
            width="100%"
        )
    )

def index() -> rx.Component:
    """Ultra-modern main page"""
    return rx.box(
        # Dynamic background based on theme
        rx.box(
            style={
                "position": "fixed",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "background": rx.cond(
                    State.dark_mode,
                    "linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%)",
                    "linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%)"
                ),
                "z_index": "-1"
            }
        ),
        
        rx.box(
            rx.vstack(
                # Header - Centered
                rx.box(
                    rx.vstack(
                        rx.text(
                            "SecurePass",
                            style={
                                "background": "linear-gradient(135deg, #667eea, #764ba2)",
                                "background_clip": "text",
                                "color": "transparent",
                                "font_size": "36px",
                                "font_weight": "900"
                            }
                        ),
                        rx.text(
                            "Ultra-Modern Password Strength Checker",
                            style={
                                "color": rx.cond(State.dark_mode, "rgba(255,255,255,0.7)", "rgba(0,0,0,0.7)"), 
                                "font_size": "16px"
                            }
                        ),
                        spacing="0",
                        align="center",
                        width="100%"
                    ),
                    style={
                        "width": "100%",
                        "max_width": "600px",
                        "margin": "0 auto",
                        "padding": "20px",
                        "margin_bottom": "20px"
                    }
                ),
                
                # Main content - Centered rectangular cards
                rx.vstack(
                    password_analyzer(),
                    password_generator(),
                    password_history(),
                    spacing="8",
                    width="100%",
                    align="center"
                ),
                
                # Footer - Centered
                rx.box(
                    rx.text(
                        "Built with Reflex • Ultra-Modern Security",
                        style={
                            "text_align": "center",
                            "color": rx.cond(State.dark_mode, "rgba(255,255,255,0.5)", "rgba(0,0,0,0.5)"),
                            "font_size": "14px"
                        }
                    ),
                    style={
                        "width": "100%",
                        "max_width": "600px",
                        "margin": "20px auto 0 auto",
                        "padding": "16px"
                    }
                ),
                
                spacing="0",
                width="100%",
                align="center"
            ),
            style={
                "display": "flex",
                "justify_content": "center",
                "align_items": "flex-start",
                "min_height": "100vh",
                "padding": "20px",
                "width": "100%"
            }
        ),
        
        style={
            "min_height": "100vh",
            "font_family": "'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif"
        }
    )

# Create the app
app = rx.App(
    stylesheets=[
        "animations.css",
        "https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;600;700;800;900&display=swap"
    ]
)
app.add_page(index, route="/", title="SecurePass - Ultra-Modern Password Checker")

if __name__ == "__main__":
    app.compile()