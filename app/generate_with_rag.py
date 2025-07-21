import os
from dotenv import load_dotenv
from app.retriever import get_relevant_chunks
from app.generator import generate_text

# Cargar variables de entorno si se requieren
load_dotenv()

def generate_text_with_context(base_prompt, tone, company, language, model):
    """
    Genera contenido adaptado al contexto si la empresa es RuizTech.
    """
    company_clean = company.strip().lower()
    is_ruiztech = company_clean == "ruiztech"

    # Instrucción de idioma
    language_instruction = get_language_instruction(language)

    # Si la empresa es RuizTech, añadimos contexto
    if is_ruiztech:
        context = get_relevant_chunks(base_prompt)
        full_prompt = f"""{language_instruction}

Contexto relevante de la empresa RuizTech:
{context}

Escribe un contenido para la plataforma sobre: "{base_prompt}".
Usa un tono {tone.lower()} y adapta el mensaje como si fuera publicado por RuizTech.
Debe ser directo, atractivo y adecuado para esa red social."""
    else:
        # Prompt sin contexto
        full_prompt = f"""{language_instruction}
Escribe un contenido para la plataforma sobre: "{base_prompt}".
Usa un tono {tone.lower()} y adapta el mensaje como si fuera publicado por {company if company else "una empresa"}.
Debe ser directo, atractivo y adecuado para esa red social."""

    return generate_text(full_prompt, model)

def get_language_instruction(language):
    """
    Devuelve la instrucción de idioma apropiada para el LLM.
    """
    return {
        "Español": "Responde en español.",
        "Inglés": "Respond in English.",
        "Francés": "Réponds en français.",
        "Italiano": "Rispondi in italiano."
    }.get(language, "Responde en español.")
