import re
import string
import secrets
from typing import Dict, List, Tuple
from password_strength import PasswordStats
from zxcvbn import zxcvbn
import bcrypt

class PasswordAnalyzer:
    def __init__(self):
        self.common_passwords = [
            "password", "123456", "password123", "admin", "qwerty",
            "letmein", "welcome", "monkey", "1234567890", "abc123"
        ]
        
    def analyze_comprehensive(self, password: str) -> Dict:
        """Comprehensive password analysis using multiple methods"""
        if not password:
            return self._empty_result()
            
        # Multiple analysis methods
        basic_analysis = self._basic_analysis(password)
        zxcvbn_analysis = self._zxcvbn_analysis(password)
        pattern_analysis = self._pattern_analysis(password)
        
        # Combined score (weighted average)
        combined_score = (
            basic_analysis["score"] * 0.4 +
            zxcvbn_analysis["score"] * 0.4 +
            pattern_analysis["score"] * 0.2
        )
        
        return {
            "password": password,
            "score": round(combined_score, 1),
            "strength": self._get_strength_label(combined_score),
            "length": len(password),
            "basic": basic_analysis,
            "zxcvbn": zxcvbn_analysis,
            "patterns": pattern_analysis,
            "feedback": self._generate_feedback(password, combined_score),
            "is_breached": self._check_breach_simulation(password),
            "entropy": self._calculate_entropy(password)
        }
    
    def _basic_analysis(self, password: str) -> Dict:
        """Enhanced basic password strength analysis"""
        score = 0
        
        # Length scoring (more generous for longer passwords)
        if len(password) >= 12:
            score += 40
        elif len(password) >= 8:
            score += 25
        else:
            score += len(password) * 3
        
        # Character diversity scoring
        if re.search(r'[a-z]', password):
            score += 15
        if re.search(r'[A-Z]', password):
            score += 15
        if re.search(r'\d', password):
            score += 15
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 15
        
        return {
            "score": min(score, 100),
            "has_uppercase": bool(re.search(r'[A-Z]', password)),
            "has_lowercase": bool(re.search(r'[a-z]', password)),
            "has_digits": bool(re.search(r'\d', password)),
            "has_special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
            "length_score": min(len(password) * 8, 100)
        }
    
    def _zxcvbn_analysis(self, password: str) -> Dict:
        """Advanced pattern-based analysis using zxcvbn"""
        result = zxcvbn(password)
        return {
            "score": result["score"] * 25,
            "crack_time": result["crack_times_display"]["offline_slow_hashing_1e4_per_second"],
            "warning": result.get("feedback", {}).get("warning", ""),
            "suggestions": result.get("feedback", {}).get("suggestions", [])
        }
    
    def _pattern_analysis(self, password: str) -> Dict:
        """Custom pattern analysis"""
        score = 100
        issues = []
        
        # Check for common patterns
        if re.search(r'(.)\1{2,}', password):
            score -= 20
            issues.append("Repeated characters")
            
        if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
            score -= 15
            issues.append("Sequential numbers")
            
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            score -= 15
            issues.append("Sequential letters")
            
        if password.lower() in self.common_passwords:
            score -= 50
            issues.append("Common password")
            
        return {
            "score": max(score, 0),
            "issues": issues
        }
    
    def _calculate_entropy(self, password: str) -> float:
        """Calculate password entropy"""
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'\d', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            charset_size += 32
            
        if charset_size == 0:
            return 0
            
        import math
        return len(password) * math.log2(charset_size)
    
    def _check_breach_simulation(self, password: str) -> bool:
        """Simulate breach database check"""
        return password.lower() in [p.lower() for p in self.common_passwords]
    
    def _generate_feedback(self, password: str, score: float) -> List[str]:
        """Generate improvement feedback"""
        feedback = []
        
        if len(password) < 8:
            feedback.append("Use at least 8 characters")
        if len(password) < 12:
            feedback.append("Consider using 12+ characters for better security")
        if not re.search(r'[A-Z]', password):
            feedback.append("Add uppercase letters")
        if not re.search(r'[a-z]', password):
            feedback.append("Add lowercase letters")
        if not re.search(r'\d', password):
            feedback.append("Add numbers")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            feedback.append("Add special characters")
        if score < 60:
            feedback.append("Avoid common words and patterns")
            
        return feedback
    
    def _get_strength_label(self, score: float) -> str:
        """Convert score to strength label"""
        if score >= 80:
            return "Very Strong"
        elif score >= 60:
            return "Strong"
        elif score >= 40:
            return "Medium"
        elif score >= 20:
            return "Weak"
        else:
            return "Very Weak"
    
    def _empty_result(self) -> Dict:
        """Return empty analysis result"""
        return {
            "password": "",
            "score": 0,
            "strength": "Very Weak",
            "length": 0,
            "basic": {"score": 0},
            "zxcvbn": {"score": 0},
            "patterns": {"score": 0},
            "feedback": [],
            "is_breached": False,
            "entropy": 0
        }

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = "!@#$%^&*(),.?\":{}|<>"
    
    def generate(self, length: int = 16, use_uppercase: bool = True, 
                use_lowercase: bool = True, use_digits: bool = True, 
                use_special: bool = True, exclude_ambiguous: bool = True) -> str:
        """Generate secure password optimized for 80%+ strength"""
        
        # Ensure minimum length for strong passwords
        if length < 12:
            length = 12
        
        charset = ""
        required_chars = []
        
        if use_lowercase:
            chars = self.lowercase
            if exclude_ambiguous:
                chars = chars.replace('l', '').replace('o', '')
            charset += chars
            # Add multiple lowercase chars for stronger passwords
            required_chars.extend([secrets.choice(chars) for _ in range(2)])
            
        if use_uppercase:
            chars = self.uppercase
            if exclude_ambiguous:
                chars = chars.replace('I', '').replace('O', '')
            charset += chars
            # Add multiple uppercase chars
            required_chars.extend([secrets.choice(chars) for _ in range(2)])
            
        if use_digits:
            chars = self.digits
            if exclude_ambiguous:
                chars = chars.replace('0', '').replace('1', '')
            charset += chars
            # Add multiple digits
            required_chars.extend([secrets.choice(chars) for _ in range(2)])
            
        if use_special:
            charset += self.special
            # Add multiple special chars for stronger passwords
            required_chars.extend([secrets.choice(self.special) for _ in range(2)])
        
        if not charset:
            return "Please choose your preferable character type to generate a strong password..."
        
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        if remaining_length > 0:
            password_chars = required_chars + [secrets.choice(charset) for _ in range(remaining_length)]
        else:
            password_chars = required_chars[:length]
        
        # Shuffle multiple times for better randomness
        for _ in range(3):
            secrets.SystemRandom().shuffle(password_chars)
        
        return ''.join(password_chars)

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))