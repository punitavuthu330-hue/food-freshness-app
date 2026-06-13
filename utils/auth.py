"""Authentication utilities"""
from datetime import datetime, timedelta
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    """Hash a password"""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Verify a password against hash"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data, expires_delta=None):
    """Create JWT access token"""
    from jose import jwt
    import os
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)
    
    to_encode.update({"exp": expire})
    secret_key = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")
    return encoded_jwt
