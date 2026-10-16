"""Require real lifecycle evidence; keep official and ARCenal grades distinct."""
import argparse
import json
from pathlib import Path


def qualify(reports, linter, upgrade_from):
    if not reports:
        raise ValueError("Aucun rapport package_check produit.")
    required = {"TEST_PACKAGE_LINTER", "TEST_INSTALL", "TEST_BACKUP_RESTORE", "TEST_UPGRADE", "TEST_CHANGE_URL"}
    for report in reports:
        tests = report.get("tests", [])
        if not required <= {item.get("test_type") for item in tests}:
            raise ValueError("Scénarios de qualification manquants.")
        if any(item.get("main_result") != "success" for item in tests):
            raise ValueError("Un scénario package_check est en échec ou non qualifié.")
        if not any(item.get("test_type") == "TEST_UPGRADE" and item.get("test_arg") == upgrade_from for item in tests):
            raise ValueError("Mise à jour depuis la version publiée non prouvée.")
        if not all(report.get(key) for key in ("commit", "app_version", "architecture", "yunohost_version")):
            raise ValueError("Identité de la version qualifiée incomplète.")
    if not {"error", "critical"} <= linter.keys():
        raise ValueError("Rapport du linter invalide.")
    permitted = {"error": {"AppCatalog.state_is_working"}, "critical": {"AppCatalog.is_in_catalog"}}
    for severity, allowed in permitted.items():
        if set(linter[severity]) - allowed:
            raise ValueError("Défaut applicatif ou de packaging signalé par le linter.")
    return {
        "schema": "arcenal-technical-qualification/v1",
        "arcenal_technical_level": 5,
        "scope": "Catalogue ARCenal uniquement ; aucune note communautaire officielle attribuée.",
        "upgrade_from": upgrade_from,
        "official_catalog_only_findings": {key: linter[key] for key in permitted},
        "linter_warnings": linter.get("warning", []),
        "evidence": [{key: report[key] for key in ("commit", "app_version", "architecture", "yunohost_version", "level", "tests")} for report in reports],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--linter-report", type=Path, required=True)
    parser.add_argument("--upgrade-from", required=True)
    parser.add_argument("--qualification-output", type=Path, required=True)
    args = parser.parse_args()
    try:
        reports = [json.loads(path.read_text()) for path in sorted(args.directory.glob("results_*.json"))]
        result = qualify(reports, json.loads(args.linter_report.read_text()), args.upgrade_from)
        args.qualification_output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error)) from error
    print("Cycle de vie complet, mise à jour depuis la version publiée et absence de défaut applicatif du linter prouvés.")
    print("Qualification technique ARCenal : niveau 5 ; le résultat officiel original est conservé séparément.")


if __name__ == "__main__":
    main()
