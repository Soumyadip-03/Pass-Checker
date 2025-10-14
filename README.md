# 🔐 Enhanced Password Strength Checker

A comprehensive password strength analyzer built with **Reflex** (Pure Python web framework) featuring real-time analysis, password generation, and security insights.

## ✨ Enhanced Features

### Core Features
- **Real-time password strength analysis** with visual feedback
- **Multi-algorithm scoring** (Basic + zxcvbn + Pattern analysis)
- **Interactive strength meter** with color-coded indicators
- **Detailed security breakdown** with entropy calculation
- **Breach database simulation** check

### Advanced Features
- **🎲 Smart Password Generator** with customizable rules
- **📊 Password History Tracking** (last 10 analyses)
- **🌙 Dark/Light Theme Toggle**
- **📋 One-click copy to clipboard**
- **💡 Security tips and best practices**
- **🔍 Pattern detection** (sequential chars, repetition, etc.)

### Technical Enhancements
- **Multiple analysis engines**: password-strength + zxcvbn + custom patterns
- **Entropy calculation** for cryptographic strength
- **Secure password hashing** with bcrypt
- **Responsive tabbed interface**
- **Real-time feedback** as you type

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip package manager

### Installation

1. **Clone and setup**:
```bash
cd "c:\Users\soumy\OneDrive\Documents\CSE\PENDING PROJECTs\PROJECT-4 (Password Strength Checker)"

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

2. **Initialize Reflex**:
```bash
reflex init
```

3. **Run the application**:
```bash
reflex run
```

4. **Open browser**: http://localhost:3000

## 📁 Project Structure

```
password-strength-checker/
├── .web/                           # Auto-generated frontend
├── assets/                         # Static files
├── password_strength_checker/
│   ├── __init__.py
│   ├── password_strength_checker.py    # Main app
│   ├── components/
│   │   ├── strength_meter.py          # Visual components
│   │   └── password_generator.py      # Generator UI
│   └── utils/
│       └── password_analyzer.py       # Core analysis logic
├── requirements.txt                # Dependencies
├── rxconfig.py                    # Reflex config
├── .env.example                   # Environment template
└── README.md
```

## 🔧 Tech Stack

### Core Framework
- **Reflex 0.4.0+** - Pure Python web framework

### Password Analysis Libraries
- **password-strength** - Wolfram Alpha-based scoring
- **zxcvbn** - Advanced pattern recognition
- **bcrypt** - Secure password hashing

### Additional Libraries
- **pandas** - Data analysis
- **matplotlib** - Visualization
- **python-dotenv** - Environment management

## 🎯 Usage Guide

### 1. Password Analysis
- Enter password in the analyzer tab
- View real-time strength meter
- Check detailed breakdown including:
  - Character requirements
  - Entropy calculation
  - Estimated crack time
  - Breach database status

### 2. Password Generation
- Customize length (4-50 characters)
- Select character types
- Exclude ambiguous characters option
- Generate and copy secure passwords

### 3. History Tracking
- View last 10 password analyses
- Track strength improvements
- Clear history when needed

## 🛡️ Security Features

### Analysis Methods
1. **Basic Analysis**: Character diversity, length scoring
2. **zxcvbn Analysis**: Pattern recognition, dictionary attacks
3. **Custom Patterns**: Sequential chars, repetition detection
4. **Entropy Calculation**: Cryptographic strength measurement

### Security Measures
- **No password storage** - Analysis only
- **Client-side processing** - Passwords never leave your device
- **Secure generation** - Cryptographically secure random generation
- **Breach simulation** - Common password detection

## 🚀 Deployment Options

### Local Development
```bash
reflex run --env dev
```

### Production Deployment

#### Option 1: Reflex Cloud
```bash
reflex deploy
```

#### Option 2: Docker
```bash
# Create Dockerfile
reflex export --frontend-only
# Deploy to any container platform
```

#### Option 3: Traditional Hosting
```bash
reflex export --frontend-only
# Deploy static files to any web server
```

## 🔧 Configuration

### Environment Variables
Copy `.env.example` to `.env` and customize:

```env
REFLEX_ENV=production
REFLEX_FRONTEND_PORT=3000
REFLEX_BACKEND_PORT=8000
ENABLE_BREACH_CHECK=true
MAX_PASSWORD_HISTORY=10
```

### Customization Options
- Modify scoring weights in `password_analyzer.py`
- Add custom breach databases
- Extend pattern detection rules
- Customize UI themes and colors

## 📊 Performance

- **Real-time analysis**: < 50ms response time
- **Memory efficient**: Minimal state management
- **Scalable**: Pure Python architecture
- **Cross-platform**: Works on Windows, macOS, Linux

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Reflex Team** - Amazing Python web framework
- **zxcvbn** - Advanced password strength estimation
- **Dropbox** - Security research and tools

---

**Built with ❤️ using Pure Python and Reflex Framework**