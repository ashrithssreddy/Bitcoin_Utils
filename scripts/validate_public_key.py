# Note: THis code is not fully tested yet.

from ecdsa import VerifyingKey, SECP256k1, BadSignatureError

def is_valid_public_key(public_key_hex):
    """
    Function to check if a given Bitcoin public key is valid.
    
    Args:
        public_key_hex (str): Bitcoin public key in hexadecimal format.
        
    Returns:
        bool: True if valid, False if invalid.
    """
    try:
        # Convert hex to bytes
        public_key_bytes = bytes.fromhex(public_key_hex)
        
        # Try to create a VerifyingKey object using the SECP256k1 curve
        vk = VerifyingKey.from_string(public_key_bytes, curve=SECP256k1)
        
        # If no error is thrown, the public key is valid
        return True
    except (ValueError, BadSignatureError):
        # Invalid public key format
        return False
