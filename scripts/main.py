# from document_control.doc_class import Document_Header, Document_Version
# import sqlite3

storage_root_path: str = "/storage"

document_types: dict[str, str] = {
    "Quality Manual": "QM",
    "Policy": "POL",
    "Quality Objective": "OBJ",
    "Standard Operating Procedure": "SOP",
    "Work Instruction": "WI",
    "Form / Template": "FORM",
    "Specification": "SPEC",
    "Drawing": "DWG",
    "Bill of Materials": "BOM",
    "Software Documentation": "SW",
    "Risk Management": "RISK",
    "Instructions for Use": "IFU",
    "Labeling": "LBL",
    "Plan": "PLAN",
    "Protocol": "PROT",
    "Report": "REP",
    "External Standard": "EXT",
    "Controlled Template": "TMP",
}

status_types: list = [
    "DRAFT",
    "IN_REVIEW",
    "APPROVED_PENDING",
    "RELEASED",
    "SUPERSEDED",
    "OBSOLETE",
]

template_map: dict[str, str] = {
    "QM": "Template_QM.txt",  # Quality Manual
    "POL": "Template_POL.txt",  # Policy
    "OBJ": "Template_OBJ.txt",  # Objectives
    "SOP": "Template_SOP.txt",  # Standard Operating Procedure
    "WI": "Template_WI.txt",  # Work Instruction
    "FORM": "Template_FORM.txt",  # Forms
    "SPEC": "Template_SPEC.txt",  # Specifications
    "BOM": "Template_BOM.txt",  # Bill of Materials
    "SW": "Template_SW.txt",  # Software Docs
    "RISK": "Template_RISK.txt",  # Risk Management
    "IFU": "Template_IFU.txt",  # Instructions for Use
    "PLAN": "Template_PLAN.txt",  # Plans
    "PROT": "Template_PROT.txt",  # Protocols
    "REP": "Template_REP.txt",  # Reports
    "TMP": "Template_Meta.txt",  # Template para crear nuevas plantillas
}

mock_external_files: dict[str, str] = {
    "DWG": "Mock_Drawing.pdf",  # Planos
    "LBL": "Mock_Label.jpg",  # Etiquetas
    "EXT": "Mock_Standard.pdf",  # Normas Externas
}
