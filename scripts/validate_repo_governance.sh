#!/usr/bin/env bash
set -euo pipefail

DEPLOY_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_REPO="${1:-$PWD}"
RULES_FILE="${RULES_FILE:-$DEPLOY_ROOT/governance/no-python-business-logic.rules.tsv}"
TS_RULES_FILE="${TS_RULES_FILE:-$DEPLOY_ROOT/governance/no-server-typescript.rules.tsv}"
HIDDEN_RULES_FILE="${HIDDEN_RULES_FILE:-$DEPLOY_ROOT/governance/no-hidden-runtime-logic.rules.tsv}"

if ! command -v rg >/dev/null 2>&1; then
  echo "ripgrep is required for governance checks."
  exit 2
fi

if [[ ! -d "$TARGET_REPO" ]]; then
  echo "Target repo does not exist: $TARGET_REPO"
  exit 2
fi

if [[ ! -f "$RULES_FILE" ]]; then
  echo "Governance rules file not found: $RULES_FILE"
  exit 2
fi

if [[ ! -f "$TS_RULES_FILE" ]]; then
  echo "TypeScript governance rules file not found: $TS_RULES_FILE"
  exit 2
fi

if [[ ! -f "$HIDDEN_RULES_FILE" ]]; then
  echo "Hidden runtime logic rules file not found: $HIDDEN_RULES_FILE"
  exit 2
fi

cd "$TARGET_REPO"

PY_FILES="$(rg --files --hidden -g '*.py' \
  -g '!**/.venv/**' \
  -g '!**/venv/**' \
  -g '!**/__pycache__/**' \
  -g '!**/.git/**' \
  -g '!**/node_modules/**' || true)"

FAIL=0

echo "Agent-deploy governance validation"
echo "Target: $TARGET_REPO"
echo "Rules:  $RULES_FILE"
echo "TS:     $TS_RULES_FILE"
echo "Hidden: $HIDDEN_RULES_FILE"
echo ""

check_content_pattern() {
  local label="$1"
  local pattern="$2"
  local matches

  if [[ -z "$PY_FILES" ]]; then
    return
  fi
  matches="$(printf '%s\n' "$PY_FILES" | xargs rg -n "$pattern" 2>/dev/null || true)"
  if [[ -n "$matches" ]]; then
    echo "[FAIL] $label"
    echo "$matches"
    echo ""
    FAIL=1
  fi
}

check_path_pattern() {
  local label="$1"
  local pattern="$2"
  local matches

  if [[ -z "$PY_FILES" ]]; then
    return
  fi
  matches="$(printf '%s\n' "$PY_FILES" | rg "$pattern" || true)"
  if [[ -n "$matches" ]]; then
    echo "[FAIL] $label"
    echo "$matches"
    echo ""
    FAIL=1
  fi
}

while IFS=$'\t' read -r scope label pattern; do
  [[ -z "${scope:-}" || "$scope" == \#* ]] && continue

  case "$scope" in
    content)
      check_content_pattern "$label" "$pattern"
      ;;
    path)
      check_path_pattern "$label" "$pattern"
      ;;
    *)
      echo "[FAIL] Unknown governance rule scope '$scope' in $RULES_FILE"
      FAIL=1
      ;;
  esac
done < "$RULES_FILE"

ALL_FILES="$(rg --files --hidden \
  -g '!**/.git/**' \
  -g '!**/node_modules/**' \
  -g '!**/.venv/**' \
  -g '!**/venv/**' || true)"

YAML_FILES="$(printf '%s\n' "$ALL_FILES" | rg '\.(ya?ml)$' || true)"

check_validator_file_inventory() {
  if [[ -d ".github" ]] && ! printf '%s\n' "$ALL_FILES" | rg '^\.github/' >/dev/null 2>&1; then
    echo "[FAIL] Validator file inventory must include hidden CI/CD paths such as .github/."
    echo ".github exists but was not included in the scanned file list."
    echo ""
    FAIL=1
  fi
}

check_validator_file_inventory

check_central_governance_workflow() {
  local workflow_files
  local matches

  workflow_files="$(printf '%s\n' "$YAML_FILES" | rg '^\.github/workflows/' || true)"
  if [[ -z "$workflow_files" ]]; then
    echo "[FAIL] Repository must include a CI/CD workflow that runs Agent-deploy centralized governance validation."
    echo "Missing .github/workflows/*.yml or .github/workflows/*.yaml."
    echo ""
    FAIL=1
    return
  fi

  matches="$(printf '%s\n' "$workflow_files" | xargs rg -n 'validate_repo_governance\.sh' 2>/dev/null || true)"
  if [[ -z "$matches" ]]; then
    echo "[FAIL] CI/CD must enforce Agent-deploy centralized governance validation."
    echo "No .github/workflows file runs validate_repo_governance.sh."
    echo ""
    FAIL=1
  fi
}

check_central_governance_workflow

DOC_FILES="$(printf '%s\n' "$ALL_FILES" | rg '(^|/)(README|AGENTS)\.md$' || true)"

check_agentql_doc_sources() {
  local missing=""
  local doc_file
  local source_file

  if [[ -z "$DOC_FILES" ]]; then
    return
  fi

  while IFS= read -r doc_file; do
    [[ -z "$doc_file" ]] && continue
    source_file="${doc_file%.md}.agentql"
    if [[ ! -f "$source_file" ]]; then
      missing+="$doc_file -> missing $source_file"$'\n'
    fi
  done <<< "$DOC_FILES"

  if [[ -n "$missing" ]]; then
    echo "[FAIL] README.md and AGENTS.md must be authored in AgentQL first."
    printf '%s' "$missing"
    echo ""
    FAIL=1
  fi
}

check_agentql_doc_sources

while IFS=$'\t' read -r scope label pattern allowed_pattern; do
  [[ -z "${scope:-}" || "$scope" == \#* ]] && continue

  case "$scope" in
    path)
      matches="$(printf '%s\n' "$ALL_FILES" | rg "$pattern" || true)"
      if [[ -n "$matches" ]]; then
        echo "[FAIL] $label"
        echo "$matches"
        echo ""
        FAIL=1
      fi
      ;;
    path_outside_allowed)
      matches="$(printf '%s\n' "$ALL_FILES" | rg "$pattern" | rg -v "${allowed_pattern:-^$}" || true)"
      if [[ -n "$matches" ]]; then
        echo "[FAIL] $label"
        echo "$matches"
        echo ""
        FAIL=1
      fi
      ;;
    *)
      echo "[FAIL] Unknown TypeScript governance rule scope '$scope' in $TS_RULES_FILE"
      FAIL=1
      ;;
  esac
done < "$TS_RULES_FILE"

while IFS=$'\t' read -r scope label pattern; do
  [[ -z "${scope:-}" || "$scope" == \#* ]] && continue

  case "$scope" in
    content)
      matches="$(printf '%s\n' "$ALL_FILES" | xargs rg -n "$pattern" 2>/dev/null || true)"
      if [[ -n "$matches" ]]; then
        echo "[FAIL] $label"
        echo "$matches"
        echo ""
        FAIL=1
      fi
      ;;
    content_yaml)
      if [[ -n "$YAML_FILES" ]]; then
        matches="$(printf '%s\n' "$YAML_FILES" | xargs rg -n "$pattern" 2>/dev/null || true)"
      else
        matches=""
      fi
      if [[ -n "$matches" ]]; then
        echo "[FAIL] $label"
        echo "$matches"
        echo ""
        FAIL=1
      fi
      ;;
    path)
      matches="$(printf '%s\n' "$ALL_FILES" | rg "$pattern" || true)"
      if [[ -n "$matches" ]]; then
        echo "[FAIL] $label"
        echo "$matches"
        echo ""
        FAIL=1
      fi
      ;;
    path_requires_agentql_manifest)
      matches="$(printf '%s\n' "$ALL_FILES" | rg "$pattern" || true)"
      missing_manifest=""
      if [[ -n "$matches" ]]; then
        while IFS= read -r artifact_file; do
          [[ -z "$artifact_file" ]] && continue
          manifest_file="${artifact_file%.*}.agentql"
          if [[ ! -f "$manifest_file" ]]; then
            missing_manifest+="$artifact_file -> missing $manifest_file"$'\n'
          fi
        done <<< "$matches"
      fi
      if [[ -n "$missing_manifest" ]]; then
        echo "[FAIL] $label"
        printf '%s' "$missing_manifest"
        echo ""
        FAIL=1
      fi
      ;;
    *)
      echo "[FAIL] Unknown hidden-runtime rule scope '$scope' in $HIDDEN_RULES_FILE"
      FAIL=1
      ;;
  esac
done < "$HIDDEN_RULES_FILE"

if [[ "$FAIL" -ne 0 ]]; then
  cat <<'MSG'
Governance validation failed.

Product/runtime business logic must live in:
- SurrealDB schema
- SurrealQL custom functions
- SurrealDB DEFINE API endpoints
- SurrealDB events and permissions
- AgentQL-generated SurrealQL
- SurrealML bindings

Outside SurrealDB/SurrealQL/SurrealML/AgentQL, TypeScript is browser-side only.
Validation must run on the user's/client's system before server submission.
README.md and AGENTS.md must have AgentQL source files with the same basename.
Design principles must be written in AgentQL.

Rule source:
  governance/
MSG
  exit 1
fi

echo "Governance validation passed."
