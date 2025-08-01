"""
CyberVault - A secure encrypted notes vault with cyberpunk-themed GUI

A Python package for securely storing and managing encrypted notes with a beautiful
cyberpunk-themed graphical user interface.
"""

__version__ = "1.0.0"
__author__ = "Layzee"
__description__ = "A secure encrypted notes vault with cyberpunk-themed GUI"

__all__ = ["vault", "gui"]

# Lazy imports to avoid import issues during testing
def _import_vault():
    """Lazy import for vault module"""
    from . import vault
    return vault

def _import_gui():
    """Lazy import for gui module"""
    from . import gui
    return gui 