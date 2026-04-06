# -*- coding: utf-8 -*-
"""
SMOKED! ERP - Configurações
"""
import os
from datetime import timedelta

class Config:
    """Configurações base"""
    
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'smoked-erp-secret-key-change-in-production'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 
        'sqlite:///' + os.path.join(BASE_DIR, '../database/smoked.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    PERMANENT_SESSION_LIFETIME = timedelta(hours=8)
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    UPLOAD_FOLDER = os.path.join(BASE_DIR, '../uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    ETIQUETAS_FOLDER = os.path.join(BASE_DIR, '../etiquetas')
    BACKUP_FOLDER = os.path.join(BASE_DIR, '../backups')
    
    EMPRESA_NOME = "Smoked!"
    EMPRESA_SLOGAN = "Defumados Artesanais de Qualidade"
    
    ITEMS_PER_PAGE = 50
    TIMEZONE = 'America/Sao_Paulo'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}